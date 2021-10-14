
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
```sh
# Start containers
docker-compose up --build
# Bash/Sh into running container
docker-compose exec myscript bash
docker-compose exec portainer sh
# If container is not running, start container and go into bash
docker-compose run myscript bash
```


### Developing inside VSCode

You will require the `Remote - Containers` plugin

[Now you can follow this guide](https://youtu.be/6azPqKxnGPo)


### Developing inside Pycharm

You will require the `Docker` plugin

[Now you can follow this guide](https://youtu.be/x0QbLLaZq5o)

You can run commands inside the container using `docker-compose run myscript bash`


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


