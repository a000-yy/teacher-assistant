from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut

router = APIRouter(prefix="/users",tags=["用户"])   #prefix：前缀，tags：标签

#增:创建用户
@router.post("",response_model=UserOut)
def create_user(data:UserCreate,db:Session = Depends(get_db)):
    new_user = User(username=data.username,email=data.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#查询：用户列表
@router.get("",response_model=list[UserOut])
def list_users(db:Session=Depends(get_db)):
    return db.scalars(select(User)).all()


#查询：单个用户
@router.get("/{user_id}",response_model=UserOut)
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="用户不存在")
    return user


#改：更新用户
@router.put("/{user_id}",response_model=UserOut)
def update_user(user_id:int,data:UserCreate,db:Session=Depends(get_db)):
    user=db.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="用户不存在")
    user.username=data.username
    user.email=data.email
    user.age=data.age
    db.commit()
    db.refresh(user)
    return user


#删：删除用户
@router.delete("/{user_id}")
def delete_user(user_id:int,db:Session = Depends(get_db)):
    user=db.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="用户不存在")
    db.delete(user)
    db.commit()
    return {"message":"删除成功"}
