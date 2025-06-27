# DSA-LAb3
## Docker Compose

- docker compose up -d --build &emsp;&nbsp;&nbsp;&nbsp;   ***#To start all the services***
- docker compose ps            &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;  ***#To see all the started services***
- docker compose down <----->  &nbsp;&nbsp;&nbsp;&emsp;   ***#To down/stop any service***
- docker compose logs -f <___> &nbsp;&nbsp;&nbsp;&emsp;  ***#To see the logs of a service***
- watch -n 1 'docker compose ps' &nbsp;&nbsp;&nbsp; ***#To see services every one second***

## Curl commands
- curl http://localhost:5000/health &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; ***#To check the health status***
- curl -X POST -H "Content-Type: application/json" \          
       -d '{"name":"test item" }'\
       http://localhost:5000/items                 &emsp;&emsp;&emsp;&emsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;          ***#To post an item***
- curl http://localhost:5000/items                 &emsp;&emsp;&nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;           ***#To print out the list***
- curl -X POST http://localhost:5000/reset-breaker &emsp; ***#To reset the breaker***

## Virtual Enviroment
- python3 -m venv .venv  &emsp;&emsp;***#To create***
- pip install virtualenv &emsp;&emsp;&emsp;***#To install***

## Protobuf
- python -m grpc_tools.protoc -I. --python_out=./src --grpc_python_out=./src ./items.proto &emsp;&emsp;***#To create***
