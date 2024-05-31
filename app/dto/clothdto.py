from pydantic import BaseModel

class Cloth(BaseModel):
    type:int
    quantity:int
    
class PostCloth(BaseModel):
    cloth:list[Cloth]
    openid:str