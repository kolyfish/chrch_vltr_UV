from sqlmodel import SQLModel, create_engine, Session

from app.models.models import Volunteer, ServiceType, VolunteerSkill, ServiceDate, VolunteerSchedule, \
    VolunteerAvailability

DATABASE_URL = "sqlite:///./volunteer_system.db"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)
    print("資料庫資料表建立成功！")

def get_session():
    with Session(engine) as session:
        yield session