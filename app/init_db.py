from app.database import Base, engine
from app.models.item import Item
from app.models.container import Container

def init_db():
    """Create database tables."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.") 