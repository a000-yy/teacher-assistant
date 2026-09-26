#schemas中写的是接口输入和输出的数据格式
from pydantic import BaseModel

class UserCreate(BaseModel):   #创建用户时的请求体
    username:str
    email:str
    age:int | None=None

class UserOut(BaseModel):
    user_id:int
    username: str
    email: str
    age: int | None = None

    class Config:
        from_attributes = True  # 允许从 ORM 对象读取属性（Pydantic v2 必需）


