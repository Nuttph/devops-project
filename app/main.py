from fastapi import FastAPI
from app.core.db import connect_to_mongo, close_mongo_connection, get_db # เพิ่ม get_db
from app.routes import user

app = FastAPI(title="My Pet Clinic API")

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()

# Endpoint พิเศษสำหรับ Test Database Connection
@app.get("/test-db-connection", tags=["System"])
async def test_db():
    try:
        db = get_db()
        # ลองส่งคำสั่ง ping ไปหา MongoDB
        await db.command("ping")
        count = await db.users.count_documents({})
        return {
            "status": "connected",
            "database": db.name,
            "current_user_count": count
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

app.include_router(user.router)