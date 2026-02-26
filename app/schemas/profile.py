from datetime import datetime

from pydantic import (
    BaseModel, ConfigDict, HttpUrl,
    EmailStr, field_validator
)


class ProfileBase(BaseModel):
    name: str
    email: EmailStr
    bio: str | None = None

    facebook_url: HttpUrl | None = None
    twitter_url: HttpUrl | None = None
    linkedin_url: HttpUrl | None = None
    instagram_url: HttpUrl | None = None
    website_url: HttpUrl | None = None

    avatar_image: str | None = None

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value):
        return value.lower()


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    bio: str | None = None

    facebook_url: HttpUrl | None = None
    twitter_url: HttpUrl | None = None
    linkedin_url: HttpUrl | None = None
    instagram_url: HttpUrl | None = None
    website_url: HttpUrl | None = None

    avatar_image: str | None = None


class ProfileOut(ProfileBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)