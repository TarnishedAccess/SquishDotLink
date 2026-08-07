from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import URL
from app.utils import base62_encode

async def create_url(db: AsyncSession, long_url: str) -> URL:
    new_url = URL(long_url=long_url)
    db.add(new_url)
    await db.flush()

    new_url.short_code = base62_encode(new_url.id)
    await db.commit()
    await db.refresh(new_url)

    return new_url

async def get_url_by_short_code(db: AsyncSession, short_code: str) -> URL:
    result = await db.execute(select(URL).where(URL.short_code == short_code))
    return result.scalars().first()