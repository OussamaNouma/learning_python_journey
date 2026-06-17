#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


if __name__ == "__main__":
    spaceship: SpaceStation = SpaceStation(
        station_id="ISS001",
        name="Faucon millenium",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2009-06-30T21:29:29"
    )
    print(f"""Space Station Data Validation
========================================
Valid station created:
ID: {spaceship.station_id}
Name: {spaceship.name}
Crew: {spaceship.crew_size} people
Power: {spaceship.power_level}%
Oxygen: {spaceship.oxygen_level}%
Status: {"Operational" if spaceship.is_operational else "Offline"}

========================================
Expected validation error:
""", end='')
    try:
        spaceship: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="Faucon millenium",
            crew_size=21,
            power_level=85.5,
            oxygen_level=-92.3,
            last_maintenance="2009-06-30T21:29:29"
        )
    except ValidationError as err:
        for x in err.errors():
            print(f"{x['loc'][0]}: {x['msg']}")
