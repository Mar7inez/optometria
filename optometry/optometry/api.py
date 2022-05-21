from ninja import NinjaAPI

from genders.api import router as genders_router

api = NinjaAPI()

api.add_router("genders/", genders_router, tags=["genders"])

@api.get("/ping")
def hello(request):
    return "pong"
