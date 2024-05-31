from fastapi import FastAPI
import uvicorn
from routers import cate,login,cloth

app = FastAPI()
app.include_router(cate.router)
app.include_router(login.router)
app.include_router(cloth.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True,port=8088)