from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.database import get_db
from app.db import get_items, get_item, create_item, update_item, delete_item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Item not found"}},
)

@router.get("/", response_model=List[ItemResponse])
async def get_all_items(db_session: Session = Depends(get_db)):
    """Get all items."""
    items = get_items(db_session)
    return items

@router.get("/{item_id}", response_model=ItemResponse)
async def get_single_item(item_id: int, db_session: Session = Depends(get_db)):
    """Get a specific item by ID."""
    item = get_item(db_session, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_new_item(item: ItemCreate, db_session: Session = Depends(get_db)):
    """Create a new item."""
    new_item = create_item(db_session, item)
    return new_item

@router.put("/{item_id}", response_model=ItemResponse)
async def update_existing_item(item_id: int, item: ItemUpdate, db_session: Session = Depends(get_db)):
    """Update an existing item."""
    updated_item = update_item(db_session, item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return updated_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_item(item_id: int, db_session: Session = Depends(get_db)):
    """Delete an item by ID."""
    success = delete_item(db_session, item_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return None 