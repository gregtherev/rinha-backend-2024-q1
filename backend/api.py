from ninja import NinjaAPI
from app.api import router

api_router = NinjaAPI() 

api_router.add_router("/clientes", router)