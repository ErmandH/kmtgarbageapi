from pydantic import BaseModel
from typing import Optional

class ContainerBase(BaseModel):
    """Base schema for Container data."""
    container_code: str
    name: str
    lang: float
    long: float
    occupancy_ratio: float = 0.0
    is_full: bool = False

class ContainerCreate(ContainerBase):
    """Schema for creating a new container."""
    pass

class ContainerUpdate(BaseModel):
    """Schema for updating an existing container."""
    container_code: Optional[str] = None
    name: Optional[str] = None
    lang: Optional[float] = None
    long: Optional[float] = None
    occupancy_ratio: Optional[float] = None
    is_full: Optional[bool] = None

class ContainerResponse(ContainerBase):
    """Schema for container responses, includes the ID."""
    id: int
    
    class Config:
        from_attributes = True 