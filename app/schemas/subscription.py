from datetime import datetime

from pydantic import EmailStr, BaseModel, ConfigDict


class ContactBase(BaseModel):
    email: EmailStr


class ContactUpdate(BaseModel):
    is_active: bool


class ContactOut(ContactBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)