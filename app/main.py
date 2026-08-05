import asyncio
from database import get_db, async_session
from crud import create_url

async def main():
    async with async_session() as session:
        pass

asyncio.run(main())