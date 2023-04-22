from app.database import Base
from app.database import engine

Base.metadata.create_all(engine)