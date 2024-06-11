from database import Base, engine
from models import Quiz, Question

# Create all tables in the database
Base.metadata.create_all(engine)

print("Database initialized and tables created successfully!")
