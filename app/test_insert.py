import asyncio
from database import get_db, async_session
from crud import create_url

async def main():
    async with async_session() as session:
        result = await create_url(session, "https://github.com")
        print(result.id, result.short_code, result.long_url)    
        
asyncio.run(main())
