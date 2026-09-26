from sqlalchemy import Column,String,Integer,DATETIME,ForeignKey
from datetime import datetime
from app.db.database import Base
from sqlalchemy.orm import relationship

class Document(Base):
    __tablename__="documents"

    document_id=Column(Integer,primary_key=True,index=True)
    subject=Column(String(50))
    title=Column(String(100),nullable=False)
    file_path=Column(String(255))
    owner_id=Column(Integer,ForeignKey("users.user_id"))
    created_at=Column(DATETIME,default=datetime.now)
    #与用户一对多关系,back_populates让两个关系互相知道对方
    owner=relationship("User",back_populates="documents")
    #与标签多对多关系
    tags=relationship("Tag",secondary="document_tag",back_populates="documents")