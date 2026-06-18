#!/usr/bin/env python3
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing_extensions import Self
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_report(self) -> Self:
        err_msg: list[str] = []
        if self.contact_id.startswith("AC") is False:
            err_msg.append("Contact ID must start with "
                           "'AC' (Alien Contact)")

        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                err_msg.append("Telepathic contact requires "
                               "at least 3 witnesses")
        if self.contact_type == ContactType.PHYSICAL:
            if self.is_verified is False:
                err_msg.append("Physical contact reports"
                               " must be verified")

        if self.signal_strength > 7.0:
            if self.message_received is None:
                err_msg.append("Strong signals (> 7.0) should"
                               " include received messages")
        if len(err_msg) != 0:
            raise ValueError(err_msg)
        return self


if __name__ == "__main__":
    report: AlienContact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.fromisoformat("2090-12-16T12:44:32"),
        contact_type=ContactType.TELEPATHIC,
        location="Firelink shrine",
        signal_strength=7.5,
        duration_minutes=10,
        witness_count=3,
        message_received="GitGUd Sunbro"
    )
    print(f"""Alien Contact Log Validation
======================================
Valid contact report:
ID: {report.contact_id}
Type: {report.contact_type.value}
Location: {report.location}
Timestamp: {report.timestamp}
Signal: {report.signal_strength}/10
Duration: {report.duration_minutes} minutes
Witnesses: {report.witness_count}
Message: {report.message_received}

========================================
Expected validation error:
""", end='')
    try:
        report_bis: AlienContact = AlienContact(
            contact_id="HC_2024_001",
            timestamp=datetime.fromisoformat("2090-12-16T12:44:32"),
            contact_type=ContactType.PHYSICAL,
            location="Firelink shrine",
            signal_strength=7.5,
            duration_minutes=10,
            witness_count=2,
        )
    except ValidationError as err:
        for x in err.errors():
            for msg in x['ctx']['error'].args[0]:
                print(msg)
