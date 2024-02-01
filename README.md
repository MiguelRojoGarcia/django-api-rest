# django-api-rest

Ejemplo sencillo de API REST bajo el framework Django.

### Despliegue
``` deploy ```

### Despliegue con docker
``` deploy-docker ```

### Entrar en el contenedor de la API
``` ssh-api ```

### Test unitarios
 ``` run-tests ```
 
### Documentación

Dentro de la carpeta docs puedes encontrar un fichero Postman para importarlo en tu local. Recuerda configurar la 
variable url.

### Arquitectura

En la carpeta **django_api/user_api/application** se encuentran los casos de uso de la aplicación junto con los repositorios.
Se ha tomado esta decisión para desacoplar la lógica de negocio del framework. 
