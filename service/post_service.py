from abc import ABC, abstractmethod
from dto.post_dto import PostDTO

class IPostService(ABC):
    @abstractmethod
    async def getPosts(self):
        pass
    
    @abstractmethod
    async def getPostById(self, post_id: int):
        pass
    
    @abstractmethod
    async def createPost(self, post):
        pass
    
class PostService(IPostService):
    def __init__(self, repository):
        self.repository = repository
    
    async def getPosts(self):
        return self.repository.get()
    
    async def getPostById(self, post_id: int):
        return self.repository.getById(post_id)
    
    async def createPost(self, postDTO:PostDTO):
        return await self.repository.create(postDTO)