from utils.exception import NotFoundError
from configs import config
import time
from utils.logger import logger
from service.post_service import IPostService
from schema.post_schema import PostRequestSchema
from dto.post_dto import PostDTO



class PostController:
    def __init__(self,service:IPostService):
        self.service=service
    
    async def getPosts(self):
        pass
    
    async def getPostById(self,post_id:int):
        pass
    
    async def createPost(self,post:PostRequestSchema):
        postDTO=PostDTO(title=post.title,content=post.content)
        return await self.service.createPost(postDTO)
        