from fastapi import FastAPI

app = FastAPI(title="教师助手 API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "教师助手 API 运行中"}
