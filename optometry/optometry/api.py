from ninja import NinjaAPI

from genders.api import router as genders_router
from roles.api import router as roles_router

api = NinjaAPI()

api.add_router("genders/", genders_router, tags=["genders"])
api.add_router("roles/", roles_router, tags=["roles"])

@api.get("/ping")
def hello(request):
    return "pong"
