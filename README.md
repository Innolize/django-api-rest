# Proyecto Django API REST


###Instrucciones

Se deberán instalar la siguientes dependencias:

```
$ pip install Django==3.1.7
$ pip install djangorestframework
```
Luego, correr los sigueintes comandos.

```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver
```

La aplicacion deberá estar lista para recibir request en el siguiente url:  http://127.0.0.1:8000/


### Rutas API
```
#GET domain/api/library/{id} //Obtiene librerias con id seleccionado
#POST domain/api/library/{id} // Crea libreria
#PUT domain/api/library/{id} // Modifica libreria seleccionada
#GET domain/api/library/{id}/books/{id} // Filtro de librerias por libro seleccionado
#GET domain/api/book/{id} // Obtiene libro seleccionado
#POST domain/api/book/{id} // Crea libro
#PUT domain/api/book/{id} // Modifica libro seleccionado
#GET domain/api/book/search?text=texto_ejemplo // Busca libros que contengan text query
#GET domain/api/author/{id} // Obtiene autor con id seleccionado
#POST domain/api/author/{id} // Crea autor
#PUT domain/api/author/{id} // Modifica autor seleccionado
#POST domain/api/lead //
```