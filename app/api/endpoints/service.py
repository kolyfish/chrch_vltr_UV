from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session, select
from app.db.database import get_session
from app.models.models import ServiceType

router = APIRouter()


# 列出所有服務類型
@router.get("/", response_model=List[ServiceType])
def get_service_types(session: Session = Depends(get_session)):
    services = session.exec(select(ServiceType)).all()
    return services


# 建立新服務類型
@router.post("/", response_model=ServiceType)
def create_service_type(service_type: ServiceType, session: Session = Depends(get_session)):
    session.add(service_type)
    session.commit()
    session.refresh(service_type)
    return service_type
