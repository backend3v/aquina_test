Solucion para prueba tecnica Aquinas


**-💻Servir la aplicación:**


-Construccion de los servicios por medio de docker compose
```
docker-compose build --no-cache

```


-Subir los servicios con docker compose
```
docker-compose up

```


**🚀Endpoints disponibles:**


-GET /api/data: Obtener datos de un servicio externo.

-POST /api/data: Almacenar los datos obtenidos del servicio externo en una base de datos MySQL.

-GET /api/data/{id}: Obtener un registro de datos específico de la base de datos MySQL por su ID.


**🚀Ejecucion de websocket:**


-Ejecutar script send_socket_message.py ubicado en la raiz del proyecto para recibir la respuesta del server del socket
```
python send_socket_message.py

```