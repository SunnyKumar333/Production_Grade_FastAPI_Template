from fastapi import APIRouter,status,Depends
from controller.post_controller import PostController
from utils.exception import NotFoundError
from schema.post_schema import PostRequestSchema,PostResponseSchema
from dependencies.dependency import getPostService
from dependencies.dependency import getPostController
from service.post_service import IPostService
from fastapi.responses import JSONResponse


postRouter=APIRouter()

PostControllerDependency=Depends(getPostController)

@postRouter.get("/")
async def getPosts(controller:PostController=PostControllerDependency):
    return controller.getPosts()


@postRouter.get("/{post_id}")
async def getPost(controller:PostController=PostControllerDependency):
    # post=await controller.getPost(post_id)
    pass
    

@postRouter.post("/",status_code=status.HTTP_201_CREATED,response_model=PostResponseSchema)
async def createPost(postData:PostRequestSchema,controller:PostController=PostControllerDependency):
    print(postData)
    postResponse= await controller.createPost(postData)
    content={
        "id": postResponse.id,
        "title": postResponse.title,
        "content": postResponse.content
    }
    return JSONResponse(
        content=content,
        status_code=status.HTTP_201_CREATED   
    )