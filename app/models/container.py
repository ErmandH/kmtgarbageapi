from sqlalchemy import Boolean, Column, Float, Integer, String

from app.database import Base

class Container(Base):
    """
    SQLAlchemy model for Container objects.
    """
    __tablename__ = "containers"

    id = Column(Integer, primary_key=True, index=True)
    container_code = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    lang = Column(Float)  # Latitude
    long = Column(Float)  # Longitude
    occupancy_ratio = Column(Float, default=0.0)
    is_full = Column(Boolean, default=False) 