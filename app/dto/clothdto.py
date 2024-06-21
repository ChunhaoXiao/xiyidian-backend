from pydantic import BaseModel,Field, validator,field_validator

class Cloth(BaseModel):
    status:str
    openid:str

class ClothItem(BaseModel):
    type:int 
    quantity:int

    

class PostCloth(BaseModel):
    cloth:list[ClothItem]
    openid:str