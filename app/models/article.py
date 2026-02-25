from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from app.core.database import Base
from app.models.base import TimeStampedModel


class Article(TimeStampedModel, Base):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)

    content: Mapped[str] = mapped_column(Text, nullable=False)
    image: Mapped[str] = mapped_column(String, nullable=True)
