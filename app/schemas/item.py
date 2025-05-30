from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    """Base schema for Item data."""
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

class ItemCreate(ItemBase):
    """Schema for creating a new item."""
    pass

class ItemUpdate(BaseModel):
    """Schema for updating an existing item."""
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None

class ItemResponse(ItemBase):
    """Schema for item responses, includes the ID."""
    id: int
    
    class Config:
        from_attributes = True 