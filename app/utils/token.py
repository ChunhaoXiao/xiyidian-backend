
import requests
from config import settings

def get_access_token():
    appid = settings.appid
    app_secret = settings.app_secret
    access_token_url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={app_secret}"
    res = requests.get(access_token_url)
    return res.json()['access_token']