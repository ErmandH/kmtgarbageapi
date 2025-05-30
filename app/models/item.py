from sqlalchemy import Boolean, Column, Float, Integer, String

from app.database import Base

class Item(Base):
    """
    SQLAlchemy model for Item objects.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float, default=0.0)
    is_available = Column(Boolean, default=True) 