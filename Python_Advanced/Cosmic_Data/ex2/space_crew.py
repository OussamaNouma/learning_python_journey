#!/usr/bin/env python3
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing_extensions import Self
from enum import Enum
from space_missions import SPACE_MISSIONS


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=300)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_mission(self) -> Self:
        err_msg: list[str] = []
        exp_list: list[int] = []
        rank_check: int = 0
        active: int = 1
        if self.mission_id.startswith("M") is False:
            err_msg.append("Mission ID must start with 'M'")
        for member in self.crew:
            if member.years_experience >= 5:
                exp_list.append(member.years_experience)
            if member.rank == Rank.CAPTAIN\
               or member.rank == Rank.COMMANDER:
                rank_check = 1
            if member.is_active is False:
                active = 0
        if rank_check == 0:
            err_msg.append("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            if len(exp_list) < (len(self.crew) / 2):
                err_msg.append("Long missions (> 365 days) need "
                               "50'%' experienced crew (5+ years)")
        if active == 0:
            err_msg.append("All crew members must be active")

        if len(err_msg) != 0:
            raise ValueError(err_msg)
        return self


if __name__ == "__main__":
    mission: SpaceMission = SpaceMission(**SPACE_MISSIONS[0])
    print(mission)
    print(f"""Space Mission Crew Validation
=========================================
Valid mission created:
Mission: Mars Colony Establishment
ID: {mission.mission_id}
Destination: {mission.destination}
Duration: {mission.duration_days} days
Budget: ${mission.budget_millions}M
Crew size: {len(mission.crew)}
""")
    for x in mission.crew:
        print(f"{x.name} ({x.rank.value}) - {x.specialization}")
