from fastapi import FastAPI,Request,status,HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from utils.exception import AppError
from middlewares.add_process_time_middleware import ProfilerMiddleware
from middlewares.add_corelation_id_middleware import CorelationIDMiddleware
from utils.logger import logger


from router.v1_router import v1Router
app=FastAPI()

# adding middlewares
app.add_middleware(ProfilerMiddleware)
app.add_middleware(CorelationIDMiddleware)

app.include_router(v1Router,prefix="/api/v1")

# templates=Jinja2Templates(directory="templates")
# app.mount("/static",StaticFiles(directory="static"),name="static")



# @app.get("/",include_in_schema=False)
# def read_root(request:Request):
#     return templates.TemplateResponse(request,"index.html",{"posts":posts})


# @app.get("/posts/{post_id}")
# def get_post(post_id: int):
#     for post in posts:
#         if post.get("id")==post_id:
#             return post
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")


@app.exception_handler(AppError)
def AppExceptionHandler(request:Request,exc:AppError):
    logger.error(f"AppError: {exc.message} with status code: {exc.status_code}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "status_code": exc.status_code,
                "message": exc.message,
                "correlation_id": "cid"#TODO,
            }
        },
    )
    
@app.exception_handler(Exception)
def GlobalExceptionHandler(request:Request,exc:Exception):
    logger.error(f"Unhandled Exception: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": {
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "Internal server error",
            }
        },
    )   