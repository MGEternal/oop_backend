from pydantic import BaseModel
from typing import Optional

class ShipInfo(BaseModel):
  firstname: str
  lastname: str
  address: str
  phone: str
  zip_code: str

class PayInfo(BaseModel):
  card_number: str
  name_on_card: str
  expired_date: str
  code: str
  method: str

class Checkout(BaseModel):
  email: str
  pay_info: PayInfo
  ship_info: ShipInfo
  discount: Optional[float] = 1

class CheckDiscount(BaseModel):
  code: str