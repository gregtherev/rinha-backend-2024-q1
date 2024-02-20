from ninja import NinjaAPI
from ..app.api import router as api_router

router = NinjaAPI()

router.add_router("/clientes", api_router)