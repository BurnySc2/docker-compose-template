
## Access portainer
Access docker gui (portainer):
http://localhost:9000

## Access pgadmin
Access postgres through pgadmin:
http://localhost:5050

Log in with password: "admin"

Link pgadmin to postgres by "adding server" postgres with password "changeme"

## Start containers
```
docker-compose up --build
```
## Shut down containers
``` 
docker-compose down
```

## Other
### Inspect a docker container by attaching to it interactively:
``` 
docker-compose exec -it containername
```

### Run main.py script locally

Installation
``` 
pip install poetry 
poetry install
```
Running
``` 
poetry run python main.py
```


