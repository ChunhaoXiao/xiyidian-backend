import requests
from config import settings
from fastapi import APIRouter
from utils.token import get_access_token

import json

router = APIRouter(prefix="/api/wechat")

@router.get("/qrcode")
def get_qrcode():
    token = get_access_token()
    qrcode_api_url = f"https://api.weixin.qq.com/wxa/getwxacodeunlimit?access_token={token}"
    payload = {'scene':'ordernum=123'}
    res = requests.post(qrcode_api_url, json=payload)
    return {"code":1,"data":res.text}
    