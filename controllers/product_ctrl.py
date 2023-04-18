from fastapi import APIRouter,HTTPException

router = APIRouter()
from models.Product import *
from models.Category import *
from init_system import *
from schemas.product_shcema import *

#tested ok    
@router.get("/all_catagory")
async def all_catagory():
    return { "data": system.get_all_category() } 

#tested ok
@router.get("/all_catagory_name")
async def all_catagory_name():
    return { "data": system.get_category_name() }

#tested ok
@router.get("/catagory_by_name")
async def catagory_by_name(data:dict)->dict:
    c_name = data["cataname"]
    res=system.find_category_by_name(c_name)
    if not res :
        raise HTTPException(status_code=400, detail="No have this catagory name")
    return { "data":  res}

#tested ok
@router.post("/add_keyboard_to_catagory")
async def add_keyboard_to_catagory(data:dict)->dict:
    c_name = data["cataname"]
    p_id = data["id"]
    p_name = data["name"]
    p_price = data["price"]
    p_description = data["description"]
    p_image = data["image"]
    p_qty = data["qty"]
    p_last_update = data["last_update"]
    p_version = data["version"]
    p_type = data["type"]
    p_switches = data["switches"]
    p_color = data["color"]
    res=system.find_category_by_name(c_name)
    if not res :
        raise HTTPException(status_code=400, detail="No have this catagory name")
    else :
        add = res.products.append(Keyboard(p_id,p_name,p_price,p_description,p_image,p_qty,p_last_update,p_version,p_type,p_switches,p_color))
        raise HTTPException(status_code=200, detail="Add keyboard successful")
        
#tested ok
@router.post("/product_detail_by_id")
async def product_detail_by_id(data:dict)->dict:
    p_id = data["id"]
    product = system.find_product_by_id(p_id)
    if product:
        return { "data": product }
    raise HTTPException(status_code=400, detail="Can not find product")

#tested ok
@router.post("/product_detail_by_name")
async def product_detail_by_name(data:dict)->dict:
    p_name = data["name"]
    product = system.find_product_by_name(p_name)
    if product:
        return { "data": product }
    raise HTTPException(status_code=400, detail="Can not find product")

