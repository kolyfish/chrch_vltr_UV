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
