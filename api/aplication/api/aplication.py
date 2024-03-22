from fastapi import FastAPI
from infraestructure.middleware import middleware
from aplication.routes.data.routes import get_data_routes


class Aplication:
    def __init__(self):
        self.app = FastAPI()
        self.get_routes()

    def get_routes(self):
        get_data_routes(self.app)