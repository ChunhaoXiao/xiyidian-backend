from fastapi import APIRouter, Depends,HTTPException
import requests
from config import settings
from dto.clothdto import PostCloth
from models.clothe import ClothOrder,ClothItem
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/cloth")


@router.post("/save")
def save(data:PostCloth, session:Session = Depends(get_db)):
    clothes = data.cloth
    print(clothes)
    order = ClothOrder(openid=data.openid,status=1)
    items = []
    for item in clothes:
        if item.quantity and item.type:
          items.append(ClothItem(cate_id=item.type,quantity=item.quantity))
    # if len(items) == 0:
    #     raise HTTPException(status_code=400, detail="数据不完整")
    order.items = items
    session.add(order)
    session.commit()
    return {
        "code":1
    }
    
    
   # order = Order(open_id=)
    # for item in clothes:
    #     print("-----------------")
    #     #if not item.quantity or not item.type
    #     cloth = Order(openid=data.openid,status="1")
    #     session.add(cloth)
    #     session.commit()
    #     return {"code":1}
    