from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Amount(BaseModel):
    total: int
    currency: str


class ProductList(BaseModel):
    productId: str
    name: str
    description: str
    price: int
    quantity: int
    imageUrl: Optional[str] = None

class UserModel(BaseModel):
    userId: Optional[str] = None
    userName: Optional[str] = None
    userMobile: Optional[str] = None
    userEmail: Optional[EmailStr] = None

class Product(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class Params(BaseModel):
    reference: str
    country: str
    amount: Amount
    callbackUrl: Optional[str] = None
    returnUrl: str
    productList: List[ProductList]
    cancelUrl: Optional[str] = None
    userClientIP: Optional[str] = None
    expireAt: Optional[int] = None
    userInfo: UserModel
    product: Optional[Product] = None
    payMethod: Optional[str] = None



class Status(Enum):
    INITIAL = "INITIAL"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
    CLOSE = "CLOSE"

class Error(BaseModel):
    code: str
    message: str

class Data(BaseModel):
    reference: str
    orderNo: str
    cashierUrl: str
    status: Status
    amount: Amount
    vat: Amount
class Response(BaseModel):
    code: str
    message: str
    data: Data








    



