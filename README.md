# Django-Concesionario-Crud-APP

Aplicación web MVC con Django MariaDB y docker.
Registrate, haz login y controla el crud de un 
concesionario, agregando, modificando y eliminado vehículos


#RUN WITH ENV
Para arrancar el proyecto desde env (o en local)
 ### Run env
_Abre un terminal y ejecuta_
```
source /debain/env-concesionario/bin/activate
```
 ### Seeder
_Dirigite a ***/debian/crud_init*** y ejecuta_
```
python3 manage.py migrate
```
### Run App
```
python3 manage.py runserver
```
### App on localhost
```
http://localhost:8000
```

#RUN WITH DOCKER
Para arrancarla necesitarás tener docker instalado.
Y una termianal sobre el repositorio
### Build image and run containers
```
docker-compose build & docker-compose up
```
### Run application
_comprueba primero el nombre del contenedor con python_
```
docker ps
```
ejecuta una shell en el contenedor
```
docker exec -it [nombre o id] ./bin/bash
```
Dirigite a ***/home/crud-init/*** y ejecuta los seeders
```
python3 manage.py migrate
```
Arranca la aplicación
```
python3 manage.py runserver 0.0.0.0:8000
```
Abre en tú navegador ***http://localhost:8000***

---
_Developed with ❤️ by [infolojo](https://www.infolojo.es)_
