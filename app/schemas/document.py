from pydantic import BaseModel


class DocumentCreate(BaseModel):
    title:str
    subject:str | None = None
    file_path:str | None = None
    owner_id:int


class DocumentOut(BaseModel):
    document_id: int
    title: str
    subject: str | None = None
    file_path: str | None = None
    owner_id: int

    class Config:
        from_attributes = True