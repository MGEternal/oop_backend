from pydantic import BaseModel

class CateName(BaseModel):
    cate_name : str

class ProId(BaseModel):
    id: str
    
class ProName(BaseModel):
    name: str
    

    