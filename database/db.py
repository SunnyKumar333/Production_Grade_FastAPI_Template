from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from configs.db import engine


LocalSession = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,  # Prevents objects from being expired after commit
    class_=AsyncSession
)


async def get_db():
    async with LocalSession() as session:
        yield session
        