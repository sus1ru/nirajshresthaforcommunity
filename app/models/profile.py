from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.models.base import TimeStampedModel


class Profile(TimeStampedModel, Base):
    __tablename__ = "profile"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    bio: Mapped[str] = mapped_column(Text, nullable=True)

    facebook_url: Mapped[str] = mapped_column(String, nullable=True)
    twitter_url: Mapped[str] = mapped_column(String, nullable=True)
    linkedin_url: Mapped[str] = mapped_column(String, nullable=True)
    instagram_url: Mapped[str] = mapped_column(String, nullable=True)
    website_url: Mapped[str] = mapped_column(String, nullable=True)

    avatar_image: Mapped[str] = mapped_column(String, nullable=True)
