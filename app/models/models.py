from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime, date
from typing import Optional, List

from sqlmodel import Session

from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


# 志工技能表 (VolunteerSkill) 用於記錄技能類型
class VolunteerSkill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # 技能名稱，例如 "司琴"
    description: Optional[str] = None  # 技能的描述或補充說明

    # 關聯
    volunteers: List["Volunteer"] = Relationship(back_populates="skills")
    service_types: List["ServiceType"] = Relationship(back_populates="related_skills")


# 志工表 (Volunteer)
class Volunteer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # 志工姓名

    # 與技能的多對多關聯
    skills: List[VolunteerSkill] = Relationship(back_populates="volunteers")

    # 與排班表的關聯
    schedules: List["Schedule"] = Relationship(back_populates="volunteer")


# 服侍類表 (ServiceType)
class ServiceType(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)  # 服侍名稱，例如 "司琴"
    description: Optional[str] = None  # 服侍類型的描述

    # 與技能的多對多關聯
    related_skills: List[VolunteerSkill] = Relationship(back_populates="service_types")

    # 與排班表的關聯
    schedules: List["Schedule"] = Relationship(back_populates="service_type")


# 排班表 (Schedule)
class Schedule(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: str = Field(index=True)  # 排班日期

    # 與志工的多對一關聯
    volunteer_id: Optional[int] = Field(default=None, foreign_key="volunteer.id")
    volunteer: Optional[Volunteer] = Relationship(back_populates="schedules")

    # 與服侍類的多對一關聯
    service_type_id: Optional[int] = Field(default=None, foreign_key="servicetype.id")
    service_type: Optional[ServiceType] = Relationship(back_populates="schedules")
