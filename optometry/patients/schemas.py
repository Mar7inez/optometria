from ninja import Field, Schema

from genders.schemas import GenderOut


class PatientBase(Schema):
    first_name: str = Field(..., title="First name")
    last_name: str = Field(..., title="Last name")
    email: str = Field(..., title="Email")


class PatientIn(PatientBase):
    gender: int = Field(..., gt=0, title="Gender", example=1)


class PatientOut(PatientBase):
    id: int
    gender: GenderOut