from pydantic import BaseModel

class PostRequestSchema(BaseModel):
    title: str
    content: str
    
class PostResponseSchema(BaseModel):
    id: int
    title: str
    content: str