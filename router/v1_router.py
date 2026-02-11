from fastapi import APIRouter
from router.v1.ping_router import pingRouter
from router.v1.post_router import postRouter


v1Router=APIRouter()

v1Router.include_router(pingRouter,prefix="/ping",tags=["Ping"])
v1Router.include_router(postRouter,prefix="/posts",tags=["Posts"])
