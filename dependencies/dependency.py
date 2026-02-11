from repository.post_repository import IPostRepository,PostRepository
from fastapi import Depends
from service.post_service import PostService,IPostService
from controller.post_controller import PostController
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db

def getPostRepository(db:AsyncSession=Depends(get_db)) -> IPostRepository:
    return PostRepository(db)

def getPostService(repository:IPostRepository=Depends(getPostRepository)):
    return PostService(repository)

def getPostController(service:IPostService=Depends(getPostService)):
    return PostController(service)

