from fastapi import APIRouter, HTTPException, Body
from app.models.user import UserCreate, UserUpdate, UserResponse
from app.core.db import get_db
from bson import ObjectId

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
async def get_users():
    db = get_db()
    # ดึงข้อมูลจากคอลเลกชัน users
    users_cursor = db.users.find()
    users = await users_cursor.to_list(length=100) # แนะนำให้เริ่มที่ 100 ก่อน
    
    # แปลง _id ให้เป็น string เพื่อให้ตรงกับ Pydantic Model
    for user in users:
        user["_id"] = str(user["_id"])
        
    return users

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    db = get_db()
    user_dict = user.model_dump()
    result = await db.users.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    db = get_db()
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["_id"] = str(user["_id"])
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_update: UserUpdate):
    db = get_db()
    update_data = {k: v for k, v in user_update.model_dump().items() if v is not None}
    
    if update_data:
        await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    
    return await get_user(user_id)