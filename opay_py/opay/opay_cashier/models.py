from constants import CASHIER_ENDPOINTS
from pydantic import BaseModel, EmailStr
from typing import List, Optional


class Amount(BaseModel):
    total:int
    currency:str

class ProductList(BaseModel):
    productid:str
    name:str
    description:str
    price:int
    quantity:str 
    imageUrl: Optional[str]

class UserModel(BaseModel):
    userId: Optional[str]
    userName: Optional[str]
    userMobile: Optional[str]
    userEmail: Optional[EmailStr]

class Product(BaseModel):
    name: Optional[str]
    description: Optional[str]




class Params(BaseModel):
    reference:str
    country:str
    amount: Amount
    callbackUrl: Optional[str]
    returnUrl: str
    productList: List[ProductList] 
    cancelUrl: Optional[str]
    userClientIP: Optional[str]
    expireAt: Optional[str]
    payMethod: Optional[str]
    product: Product
    
    


