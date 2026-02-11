from abc import ABC, abstractmethod
from dto.post_dto import PostDTO
from database.modals import Post
from sqlalchemy.ext.asyncio import AsyncSession

class IPostRepository(ABC):
    @abstractmethod
    async def get(self, post_id: int):
        pass
    
    @abstractmethod
    async def getById(self, post_id: int):
        pass
    
    @abstractmethod
    async def create(self, post):
        pass

class PostRepository(IPostRepository):
    def __init__(self, db:AsyncSession):
        self.db = db

    async def get(self, post_id: int):
        # Implement the logic to fetch a post by ID from the database
        pass  
    
    async def getById(self, post_id: int):
        # Implement the logic to fetch a post by ID from the database
        pass
    
    async def create(self, postDTO:PostDTO)->Post:
        # Implement the logic to create a new post in the database
        post = Post(
            title=postDTO.title,
            content=postDTO.content
            )
        self.db.add(post)
        await self.db.commit()
        await self.db.refresh(post)
        return post