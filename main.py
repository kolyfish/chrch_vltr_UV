from fastapi import FastAPI
from app.api.endpoints import volunteer, service, schedule
from app.models.models import ServiceType

from app.db.database import init_db
from typing import Optional
# 建立 FastAPI 應用程式
app = FastAPI(title="Volunteer Management System")

# 載入 API 路由
app.include_router(volunteer.router, prefix="/volunteers", tags=["Volunteers"])
app.include_router(service.router, prefix="/services", tags=["Services"])
app.include_router(schedule.router, prefix="/schedules", tags=["Schedules"])


@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")  # 定義根路徑的 GET 方法
def read_root():
    return {"Hello": "World"}

@app.get("/users/{user_id}")  # 定義動態路徑的 GET 方法
def read_user(user_id: int, q: Optional[str] = None):
    return {"user_id": user_id, "q": q}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

