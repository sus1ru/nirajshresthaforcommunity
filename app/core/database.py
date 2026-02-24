# app/core/database.py

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

# Create async engine
engine = create_async_engine(
    settings.database_url,
    echo=True,  # Set False in production
)

# Session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

# Base class for models
class Base(DeclarativeBase):
    pass


# Dependency
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session