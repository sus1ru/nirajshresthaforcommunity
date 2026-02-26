from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.utils.generate_slug import generate_slug


async def create_unique_slug(
    title: str,
    db: AsyncSession,
    table: DeclarativeBase,
) -> str:
    base_slug = generate_slug(title)
    slug = base_slug
    counter = 1

    while True:
        result = await db.execute(
            select(table).where(table.slug == slug)
        )
        existing = result.scalar_one_or_none()

        if not existing:
            return slug

        slug = f"{base_slug}-{counter}"
        counter += 1