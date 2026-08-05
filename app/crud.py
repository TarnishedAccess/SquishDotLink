from sqlalchemy.ext.asyncio import AsyncSession
from models import URL
from utils import base62_encode

async def create_url(db: AsyncSession, long_url: str) -> URL:
    new_url = URL(long_url=long_url)
    db.add(new_url)
    await db.flush()

    new_url.short_code = base62_encode(new_url.id)
    await db.commit()
    await db.refresh(new_url)

    return new_url