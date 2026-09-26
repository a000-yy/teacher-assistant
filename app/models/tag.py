from sqlalchemy import Table,Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

#中间表
document_tag = Table(
    "document_tag",#表名
    Base.metadata,#注册到Base
    Column("document_id",ForeignKey("documents.document_id"),primary_key=True),#指向文档
    Column("tag_id",ForeignKey("tags.tag_id"),primary_key=True)#指向标签
)

class Tag(Base):
    __tablename__="tags"

    tag_id=Column(Integer,primary_key=True,index=True)
    name=Column(String(30),unique=True,index=True)

    documents=relationship("Document",secondary=document_tag,back_populates="tags")