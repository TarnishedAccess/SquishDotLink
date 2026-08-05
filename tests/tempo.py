import asyncio
from database import engine, Base
import models  # important, explained below

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created!")

asyncio.run(main())