from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.models import VolunteerSchedule

router = APIRouter()


# 列出所有志工排班記錄
@router.get("/", response_model=List[VolunteerSchedule])
def get_schedules(session: Session = Depends(get_session)):
    schedules = session.exec(select(VolunteerSchedule)).all()
    return schedules


# 新增志工排班記錄
@router.post("/", response_model=VolunteerSchedule)
def create_schedule(schedule: VolunteerSchedule, session: Session = Depends(get_session)):
    session.add(schedule)
    session.commit()
    session.refresh(schedule)
    return schedule
