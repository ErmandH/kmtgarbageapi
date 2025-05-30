from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate
from app.models.container import Container
from app.schemas.container import ContainerCreate, ContainerUpdate

def get_items(db: Session) -> List[Item]:
    """Get all items from the database."""
    return db.query(Item).all()

def get_item(db: Session, item_id: int) -> Optional[Item]:
    """Get a specific item by ID."""
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, item: ItemCreate) -> Item:
    """Create a new item and return it."""
    db_item = Item(
        name=item.name,
        description=item.description,
        price=item.price,
        is_available=item.is_available
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: ItemUpdate) -> Optional[Item]:
    """Update an existing item."""
    db_item = get_item(db, item_id)
    if db_item:
        update_data = item.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    return None

def delete_item(db: Session, item_id: int) -> bool:
    """Delete an item by ID."""
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False

def get_containers(db: Session) -> List[Container]:
    """Get all containers from the database."""
    return db.query(Container).all()

def get_container(db: Session, container_id: int) -> Optional[Container]:
    """Get a specific container by ID."""
    return db.query(Container).filter(Container.id == container_id).first()

def get_container_by_code(db: Session, container_code: str) -> Optional[Container]:
    """Get a specific container by container_code."""
    return db.query(Container).filter(Container.container_code == container_code).first()

def create_container(db: Session, container: ContainerCreate) -> Container:
    """Create a new container and return it."""
    db_container = Container(
        container_code=container.container_code,
        name=container.name,
        lang=container.lang,
        long=container.long,
        occupancy_ratio=container.occupancy_ratio,
        is_full=container.is_full
    )
    db.add(db_container)
    db.commit()
    db.refresh(db_container)
    return db_container

def update_container(db: Session, container_id: int, container: ContainerUpdate) -> Optional[Container]:
    """Update an existing container."""
    db_container = get_container(db, container_id)
    if db_container:
        update_data = container.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_container, key, value)
        db.commit()
        db.refresh(db_container)
        return db_container
    return None

def delete_container(db: Session, container_id: int) -> bool:
    """Delete a container by ID."""
    db_container = get_container(db, container_id)
    if db_container:
        db.delete(db_container)
        db.commit()
        return True
    return False 