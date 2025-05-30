import random
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.container import ContainerCreate
from app.db import create_container, get_container_by_code

# Initial locations dictionary
locations = {
    "Kon1": (40.9741, 28.8754),
    "Kon2": (40.9753, 28.8722),
    "Kon3": (40.9732, 28.8709),
    "Kon4": (40.9737, 28.8681),
    "Kon5": (40.9744, 28.8692),
    "Kon6": (40.9762, 28.8686),
    "Kon7": (40.9768, 28.8710),
    "Kon8": (40.9751, 28.8734),
    "Kon9": (40.9748, 28.8748),
    "Kon10": (40.9738, 28.8729),
}

# Additional 10 locations
additional_locations = {
    "Kon11": (40.9730, 28.8765),
    "Kon12": (40.9755, 28.8780),
    "Kon13": (40.9770, 28.8745),
    "Kon14": (40.9725, 28.8720),
    "Kon15": (40.9760, 28.8705),
    "Kon16": (40.9740, 28.8770),
    "Kon17": (40.9765, 28.8725),
    "Kon18": (40.9735, 28.8695),
    "Kon19": (40.9750, 28.8760),
    "Kon20": (40.9745, 28.8715),
}

# Combine both dictionaries
all_locations = {**locations, **additional_locations}

def seed_containers():
    """Seed the database with container data."""
    db = SessionLocal()
    try:
        created_count = 0
        already_exists_count = 0
        
        for code, (lang, long) in all_locations.items():
            # Check if container already exists
            existing = get_container_by_code(db, code)
            if existing:
                print(f"Container {code} already exists, skipping...")
                already_exists_count += 1
                continue
            
            # Generate random occupancy ratio
            occupancy_ratio = round(random.uniform(0.0, 1.0), 2)
            # Determine if full based on occupancy ratio
            is_full = occupancy_ratio > 0.9
            
            # Create container
            container = ContainerCreate(
                container_code=code,
                name=f"Container {code}",
                lang=lang,
                long=long,
                occupancy_ratio=occupancy_ratio,
                is_full=is_full
            )
            
            create_container(db, container)
            print(f"Created container {code} at coordinates ({lang}, {long})")
            created_count += 1
        
        print(f"\nSeeding completed: {created_count} containers created, {already_exists_count} already existed.")
    
    except Exception as e:
        print(f"Error seeding containers: {str(e)}")
    finally:
        db.close()

def create_from_dictionary(container_dict: dict, db: Session = None):
    """
    Create a container from a dictionary of values.
    Useful for manual creation of specific containers.
    
    Args:
        container_dict: Dictionary containing container data
        db: Database session (optional)
    
    Returns:
        Created container or None if error
    """
    if db is None:
        db = SessionLocal()
        should_close_db = True
    else:
        should_close_db = False
    
    try:
        # Check required fields
        required_fields = ['container_code', 'name', 'lang', 'long']
        for field in required_fields:
            if field not in container_dict:
                print(f"Error: Missing required field '{field}'")
                return None
        
        # Set default values for optional fields
        if 'occupancy_ratio' not in container_dict:
            container_dict['occupancy_ratio'] = 0.0
        
        if 'is_full' not in container_dict:
            container_dict['is_full'] = container_dict['occupancy_ratio'] > 0.9
        
        # Check if container already exists
        existing = get_container_by_code(db, container_dict['container_code'])
        if existing:
            print(f"Container {container_dict['container_code']} already exists")
            return existing
        
        # Create container
        container = ContainerCreate(**container_dict)
        created = create_container(db, container)
        print(f"Created container {container_dict['container_code']}")
        return created
    
    except Exception as e:
        print(f"Error creating container: {str(e)}")
        return None
    
    finally:
        if should_close_db:
            db.close()

if __name__ == "__main__":
    print("Seeding database with containers...")
    seed_containers()
    
    # Example of how to create a container from a dictionary
    print("\nExample of creating a custom container:")
    custom_container = {
        "container_code": "KustomKon",
        "name": "Custom Container",
        "lang": 40.9800,
        "long": 28.8800,
        "occupancy_ratio": 0.75,
        "is_full": False
    }
    create_from_dictionary(custom_container) 