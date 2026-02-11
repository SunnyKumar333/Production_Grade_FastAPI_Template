# router in fast apo
from fastapi import APIRouter

from controller.ping_controller import PingController



pingRouter=APIRouter()
ping_controller=PingController()

@pingRouter.get("/")
def ping():
    return ping_controller.ping()