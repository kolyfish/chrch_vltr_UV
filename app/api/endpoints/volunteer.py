from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.volunteer import Volunteer

router = APIRouter()


# 取得所有志工資料
@router.get("/", response_model=List[Volunteer])
def get_volunteers(session: Session = Depends(get_session)):
    volunteers = session.exec(select(Volunteer)).all()
    return volunteers


# 透過 id 取得志工資料
@router.get("/{volunteer_id}", response_model=Volunteer)
def get_volunteer(volunteer_id: int, session: Session = Depends(get_session)):
    volunteer = session.get(Volunteer, volunteer_id)
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")
    return volunteer


# 新增志工資料
@router.post("/", response_model=Volunteer)
def create_volunteer(volunteer: Volunteer, session: Session = Depends(get_session)):
    session.add(volunteer)
    session.commit()
    session.refresh(volunteer)
    return volunteer


# 更新志工資料
@router.put("/{volunteer_id}", response_model=Volunteer)
def update_volunteer(volunteer_id: int, volunteer_update: Volunteer, session: Session = Depends(get_session)):
    db_volunteer = session.get(Volunteer, volunteer_id)
    if not db_volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    volunteer_data = volunteer_update.dict(exclude_unset=True)
    for key, value in volunteer_data.items():
        setattr(db_volunteer, key, value)

    session.add(db_volunteer)
    session.commit()
    session.refresh(db_volunteer)
    return db_volunteer


# 刪除志工資料
@router.delete("/{volunteer_id}", response_model=dict)
def delete_volunteer(volunteer_id: int, session: Session = Depends(get_session)):
    volunteer = session.get(Volunteer, volunteer_id)
    if not volunteer:
        raise HTTPException(status_code=404, detail="Volunteer not found")

    session.delete(volunteer)
    session.commit()
    return {"status": "success", "message": f"Volunteer {volunteer_id} deleted"}
