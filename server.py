import grpc
from concurrent import futures
import items_pb2
import items_pb2_grpc
import logging
import os
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from grpc_health.v1 import health_pb2, health_pb2_grpc

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# MongoDB connection setup
mongo_host = os.environ.get("MONGO_HOST", "localhost")
mongo_port = int(os.environ.get("MONGO_PORT", "27017"))
mongo_db = os.getenv("MONGO_DB", "itemsdb")
mongo_user = os.getenv("MONGO_USER", "root")
mongo_pass = os.getenv("MONGO_PASSWORD", "example")

try:
    client = MongoClient(
        f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}",
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=2000,
        socketTimeoutMS=5000
    )
    client.admin.command('ping')  # Test connection
    db = client[mongo_db]
    collection = db["items"]
    collection.create_index("id", unique=True)
    logging.info(f"Connected to MongoDB at {mongo_host}:{mongo_port}")
except PyMongoError as e:
    logging.error(f"Failed to connect to MongoDB: {e}")
    client = db = collection = None

class HealthServicer(health_pb2_grpc.HealthServicer):
    def Check(self, request, context):
        if client is None:
            return health_pb2.HealthCheckResponse(
                status=health_pb2.HealthCheckResponse.NOT_SERVING)
        try:
            client.admin.command('ping')
            return health_pb2.HealthCheckResponse(
                status=health_pb2.HealthCheckResponse.SERVING)
        except PyMongoError:
            return health_pb2.HealthCheckResponse(
                status=health_pb2.HealthCheckResponse.NOT_SERVING)

class ItemServiceServicer(items_pb2_grpc.ItemServiceServicer):
    def _check_db(self, context):
        if collection is None:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details("Database unavailable")
            return False
        return True

    def GetItemById(self, request, context):
        if not self._check_db(context):
            return items_pb2.ItemResponse()
        
        try:
            doc = collection.find_one({"id": request.id})
            if not doc:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Item not found")
                return items_pb2.ItemResponse()
            return items_pb2.ItemResponse(id=doc["id"], name=doc["name"])
        except PyMongoError as e:
            logging.error(f"Error retrieving item {request.id}: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Database error")
            return items_pb2.ItemResponse()

    def ListAllItems(self, request, context):
        if not self._check_db(context):
            return
        
        try:
            for doc in collection.find():
                yield items_pb2.ItemResponse(id=doc["id"], name=doc["name"])
        except PyMongoError as e:
            logging.error(f"Error listing items: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Database error")

    def AddItem(self, request, context):
        if not self._check_db(context):
            return items_pb2.ItemResponse()
        
        try:
            if request.id > 0 and collection.find_one({"id": request.id}):
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details("Item exists")
                return items_pb2.ItemResponse()
            
            new_id = request.id if request.id > 0 else self._get_next_id()
            collection.insert_one({"id": new_id, "name": request.name})
            return items_pb2.ItemResponse(id=new_id, name=request.name)
        except PyMongoError as e:
            logging.error(f"Error creating item: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Database error")
            return items_pb2.ItemResponse()

    def _get_next_id(self):
        last_item = collection.find_one(sort=[("id", -1)])
        return (last_item["id"] + 1) if last_item else 1

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    items_pb2_grpc.add_ItemServiceServicer_to_server(ItemServiceServicer(), server)
    health_pb2_grpc.add_HealthServicer_to_server(HealthServicer(), server)
    server.add_insecure_port('[::]:50051')
    logging.info("gRPC Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()