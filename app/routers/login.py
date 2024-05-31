from fastapi import APIRouter
import requests
from config import settings

router = APIRouter(prefix="/api")

@router.get("/login")
def login(code:str):
    appid = settings.appid
    app_secret = settings.app_secret
    url = f"https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={app_secret}&js_code={code}&grant_type=authorization_code" 
    response = requests.get(url)
    return {"code":1, "data":response.json()}

