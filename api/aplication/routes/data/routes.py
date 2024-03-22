from infraestructure.middleware import middleware
import requests
from infraestructure.services.events import Event_Service

def get_data_routes(app):
    @middleware
    @app.get("/api/data")
    def read_root():
        return Event_Service().get()
    
    @middleware
    @app.get("/api/data/{id}")
    def read_root(id):
        return Event_Service().single_get(id)
    


    @middleware
    @app.post("/api/data")
    def read_root():
        return Event_Service().post()
    