from sqlalchemy import create_engine,column,String,Integer,DATETIME
from sqlalchemy.orm import declarative_base,sessionmaker
from datetime import datetime


#数据库引擎
DATABASE_URL="mysql+pymysql://root:123456@localhost:3306/tc?charset=utf8mb4"
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

#模型基类
Base = declarative_base()


#会话
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)


#FastAPI依赖，使用完自动关闭
def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()




