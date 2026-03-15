from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None

class UserResponse(UserBase):
    id: str = Field(..., alias="_id") # แปลง _id ของ MongoDB เป็น id ใน JSON

    class Config:
        populate_by_name = True # ช่วยให้ Pydantic อ่านค่าจาก _id ได้