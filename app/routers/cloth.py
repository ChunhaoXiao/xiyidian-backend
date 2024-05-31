from fastapi import APIRouter
import requests
from config import settings
from dto.clothdto import PostCloth 

router = APIRouter(prefix="/api/cloth")

@router.post("/save")
def save(data:PostCloth):
    clothes = data.cloth
    print(clothes)
    return {"code":1}
    