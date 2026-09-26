from sqlalchemy import Column,String,Integer,DATETIME
from app.db.database import Base  #从database中导入Base基类
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):    #继承基类
    __tablename__="users"   #定义表名

    user_id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,index=True)
    email=Column(String(100),unique=True,index=True)
    age=Column(Integer,nullable=True)
    created_at=Column(DATETIME,default=datetime.now)

    #与文件一对多关系  #级联删除(cascade="all,delete-orphan")：删除用户时自动删除用户的所有文档
    documents=relationship("Document",back_populates="owner",cascade="all,delete-orphan")


