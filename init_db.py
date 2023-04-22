from database import Base, engine
import models.message  # Import additional models as needed

Base.metadata.create_all(bind=engine)