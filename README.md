# DSA-LAb3
## Docker Compose

- docker compose up -d --build   **To start all the services**
- docker compose ps              **To see all the started services**
- docker compose down <----->    **To down/stop any service**
- docker compose logs -f <___>   **To see the logs of a service**
- watch -n 1 'docker compose ps' **To see services every one second**

## Curl commands
- curl http://localhost:5000/health                           **To check the health status**
- curl -X POST -H "Content-Type: application/json" \          
       -d '{"name":"test item" }'\
       http://localhost:5000/items                            **To post an item**
- curl http://localhost:5000/items                            **To print out the list**
- curl -X POST http://localhost:5000/reset-breaker            **To reset the breaker**

## Virtual Enviroment
- python3 -m venv .venv  **To create**
- pip install virtualenv **To install** 

## Protobuf
- python -m grpc_tools.protoc -I. --python_out=./src --grpc_python_out=./src ./items.proto **To create**
