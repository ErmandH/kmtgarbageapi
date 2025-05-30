from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.container import ContainerCreate, ContainerResponse, ContainerUpdate
from app.database import get_db
from app.db import (
    get_containers, get_container, get_container_by_code,
    create_container, update_container, delete_container
)

router = APIRouter(
    prefix="/containers",
    tags=["containers"],
    responses={404: {"description": "Container not found"}},
)

@router.get("/", response_model=List[ContainerResponse])
async def get_all_containers(db_session: Session = Depends(get_db)):
    """Get all containers."""
    containers = get_containers(db_session)
    return containers

@router.get("/{container_id}", response_model=ContainerResponse)
async def get_single_container(container_id: int, db_session: Session = Depends(get_db)):
    """Get a specific container by ID."""
    container = get_container(db_session, container_id)
    if container is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Container not found")
    return container

@router.get("/code/{container_code}", response_model=ContainerResponse)
async def get_container_by_container_code(container_code: str, db_session: Session = Depends(get_db)):
    """Get a specific container by container code."""
    container = get_container_by_code(db_session, container_code)
    if container is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Container not found")
    return container

@router.post("/", response_model=ContainerResponse, status_code=status.HTTP_201_CREATED)
async def create_new_container(container: ContainerCreate, db_session: Session = Depends(get_db)):
    """Create a new container."""
    # Check if a container with the same code already exists
    existing_container = get_container_by_code(db_session, container.container_code)
    if existing_container:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Container with code {container.container_code} already exists"
        )
    
    new_container = create_container(db_session, container)
    return new_container

@router.put("/{container_id}", response_model=ContainerResponse)
async def update_existing_container(container_id: int, container: ContainerUpdate, db_session: Session = Depends(get_db)):
    """Update an existing container."""
    # Check if the container exists
    updated_container = update_container(db_session, container_id, container)
    if updated_container is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Container not found")
    
    # If container code is being updated, check if new code already exists
    if container.container_code:
        existing = get_container_by_code(db_session, container.container_code)
        if existing and existing.id != container_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Container with code {container.container_code} already exists"
            )
    
    return updated_container

@router.delete("/{container_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_container(container_id: int, db_session: Session = Depends(get_db)):
    """Delete a container by ID."""
    success = delete_container(db_session, container_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Container not found")
    return None 