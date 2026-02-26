from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, field_validator


class ContactBase(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value):
        return value.lower()


class ContactCreate(ContactBase):
    pass


class ContactOut(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)