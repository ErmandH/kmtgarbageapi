import asyncio
import random
from datetime import datetime
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.db import get_containers, update_container
from app.schemas.container import ContainerUpdate

async def update_containers_randomly():
    """Update all containers except Kon1 with random values every 5 minutes."""
    while True:
        try:
            db: Session = SessionLocal()
            containers = get_containers(db)
            
            for container in containers:
                # Skip Kon1
                if container.container_code == "Kon1":
                    continue
                    
                # Generate random values
                new_occupancy = round(random.uniform(0.1, 1.0), 2)  # Random value between 0.1 and 1.0
                new_is_full = new_occupancy >= 0.7
                
                # Update container
                update_data = ContainerUpdate(
                    occupancy_ratio=new_occupancy,
                    is_full=new_is_full
                )
                update_container(db, container.id, update_data)
                
            print(f"[{datetime.now()}] Containers updated randomly")
            db.close()
            
        except Exception as e:
            print(f"Error updating containers: {str(e)}")
            if 'db' in locals():
                db.close()
                
        # Wait for 5 minutes
        await asyncio.sleep(300)  # 300 seconds = 5 minutes 