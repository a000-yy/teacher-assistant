from fastapi import APIRouter,Depends,HTTPException,File,Form,UploadFile
from fastapi.params import Depends
from multipart import file_path
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.database import get_db
from app.models import Document
from app.models.user import User
from app.schemas.document import DocumentOut, DocumentCreate
import os #操作系统接口，这里用于处理路径（如 os.path.join、os.makedirs 创建目录、os.remove 删除文件）
import shutil #高层文件操作，用于保存上传的文件

router = APIRouter(prefix="/documents",tags=["文档"])

UPLOAD_DIR = "data/uploads"#定义文件上传后存放的相对路径
os.makedirs(UPLOAD_DIR,exist_ok=True) # 创建目录，若已存在也不报错

#上传文件
@router.post("/upload",response_model=DocumentOut)
def upload_document(
        owner_id:int=Form(...),
        title:str=Form(...),
        subject:str=Form(None),
        file:UploadFile=File(...),
        db:Session=Depends(get_db),
):
    owner=db.get(User,owner_id)
    if not owner:
        raise HTTPException(status_code=404,detail="用户不存在")

    #1.保存文件到本地
    file_path=os.path.join(UPLOAD_DIR,file.filename)#拼接路径
    with open(file_path,"wb") as f:#wb表示二进制写
        shutil.copyfileobj(file.file,f)
    #2.存数据库记录
    doc = Document(title=title,subject=subject,file_path=file_path,owner_id=owner_id)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


 #创建文档
@router.post("",response_model=DocumentOut)
def create_document(data:DocumentCreate,db:Session=Depends(get_db)):
    owner=db.get(User,data.owner_id)
    if not owner:
        raise HTTPException(status_code=404,detail="用户不存在")
    doc =Document(title=data.title,subject=data.subject,file_path=data.file_path,owner_id=data.owner_id)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

#查询文档列表
@router.get("",response_model=list[DocumentOut])
def list_documents(db:Session=Depends(get_db)):
    return db.scalars(select(Document)).all()

#查询某个用户的文档
@router.get("/user/{user_id}",response_model=list[DocumentOut])
def list_user_documents(user_id:int,db:Session=Depends(get_db)):
    user = db.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="用户不存在")
    return user.documents

#查询单个文档
@router.get("/{document_id}",response_model=DocumentOut)
def get_document(document_id:int,db:Session=Depends(get_db)):
    doc=db.get(Document,document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="文档不存在")
    return doc