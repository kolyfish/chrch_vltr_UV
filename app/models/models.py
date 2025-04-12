from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, date
from typing import Optional, List


# 志工資料表
class Volunteer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    phone: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

    skills: List["VolunteerSkill"] = Relationship(back_populates="volunteer")
    availabilities: List["VolunteerAvailability"] = Relationship(back_populates="volunteer")
    schedules: List["VolunteerSchedule"] = Relationship(back_populates="volunteer")


# 服務類型資料表
class ServiceType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    required_volunteers: int  # 每日需要的志工數量

    volunteer_skills: List["VolunteerSkill"] = Relationship(back_populates="service_type")
    schedules: List["VolunteerSchedule"] = Relationship(back_populates="service_type")


# 志工技能資料表，多對多關聯志工與服務類型
class VolunteerSkill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    volunteer_id: int = Field(foreign_key="volunteer.id")
    service_type_id: int = Field(foreign_key="servicetype.id")

    volunteer: Volunteer = Relationship(back_populates="skills")
    service_type: ServiceType = Relationship(back_populates="volunteer_skills")


# 服務日期資料表
class ServiceDate(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    service_date: date = Field(sa_column_kwargs={"unique": True})
    note: Optional[str] = None

    schedules: List["VolunteerSchedule"] = Relationship(back_populates="service_date")


# 志工排班資料表，每次服務的排班紀錄
class VolunteerSchedule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    volunteer_id: int = Field(foreign_key="volunteer.id")
    service_type_id: int = Field(foreign_key="servicetype.id")
    service_date_id: int = Field(foreign_key="servicedate.id")
    status: str = "scheduled"  # 可用值例如 scheduled, cancelled, completed...

    volunteer: Volunteer = Relationship(back_populates="schedules")
    service_type: ServiceType = Relationship(back_populates="schedules")
    service_date: ServiceDate = Relationship(back_populates="schedules")


# 志工每週可用性資料表
class VolunteerAvailability(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    volunteer_id: int = Field(foreign_key="volunteer.id")
    day_of_week: int  # 0~6 對應週一~週日
    is_available: bool = True

    volunteer: Volunteer = Relationship(back_populates="availabilities")
