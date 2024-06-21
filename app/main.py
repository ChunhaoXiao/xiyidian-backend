from fastapi import FastAPI
import uvicorn
from routers import cate,login,cloth,wechat
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI()
app.include_router(cate.router)
app.include_router(login.router)
app.include_router(cloth.router)
app.include_router(wechat.router)
from database import engine
from models.clothe import Base

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    
    print(f"validation errorsssss:{str(exc)}")
    print(f"validation body:{exc.body}")
    return PlainTextResponse("数据验证失败", status_code=400)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    uvicorn.run("main:app", reload=True,port=8078)