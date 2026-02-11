from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from configs import config  

setting=config.get_settings()
DATABASE_URL = f"mysql+aiomysql://{setting.database_user}:{setting.database_password}@{setting.database_host}:{setting.database_port}/{setting.database_name}"

engine =create_async_engine(
    DATABASE_URL,
    echo=False,  # Set to True for SQL query logging
    pool_size=10,  # Adjust based on your needs
    max_overflow=20,  # Adjust based on your needs  
)