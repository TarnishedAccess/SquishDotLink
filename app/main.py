import asyncio
from fastapi import FastAPI, Depends, HTTPException
from app.database import get_db, async_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import RedirectResponse
from app.schemas import URLCreate, URLResponse
from app.crud import create_url, get_url_by_short_code

app = FastAPI()

@app.post("/urls", response_model=URLResponse)
async def shorten_url(in_data: URLCreate, db: AsyncSession = Depends(get_db)):
    new_url = await create_url(db, str(in_data.long_url))
    return new_url

@app.get("/{short_code}", response_model=URLResponse)
async def get_url(short_code: str, db: AsyncSession = Depends(get_db)):
    url = await get_url_by_short_code(db, short_code)
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=url.long_url)