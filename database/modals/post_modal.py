from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from database.modals.base import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    
    class Config:
        from_attributes = True