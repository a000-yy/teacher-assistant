from http.client import responses
from fastapi import FastAPI,Path,Query,HTTPException
from fastapi.openapi.utils import status_code_ranges
from pyexpat.errors import messages
from pydantic import BaseModel
from starlette.responses import HTMLResponse, FileResponse
from app.api import users,documents


#创建FastAPI实例
app = FastAPI(title="教师助手 API")

app.include_router(users.router)
app.include_router(documents.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
