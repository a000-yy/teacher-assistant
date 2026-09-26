from app.db.database import Base,engine
import app.models

Base.metadata.create_all(bind=engine)
print("建表完成")