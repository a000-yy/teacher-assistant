# 教师助手（Teacher Assistant）

基于大模型的 AI 教学助手，面向中学教师，提供备课、出卷、答疑、作业批改四大功能。

## 功能
- [ ] 备课助手：上传教材，AI 生成教案
- [ ] 出卷助手：输入知识点，自动生成试卷
- [ ] 答疑助手：学生提问，多轮对话 + 答案溯源
- [ ] 作业批改：上传作业图片，OCR + AI 评语评分

## 技术栈
- 后端：FastAPI
- 数据库：MySQL + SQLAlchemy
- 大模型：DeepSeek / 通义千问
- 向量库：Chroma
- 部署：Docker

## 快速开始
```bash
# 1. 创建并激活虚拟环境
python -m venv .venv
# Windows
.venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动服务
uvicorn app.main:app --reload
```

启动后访问：
- 接口文档：http://127.0.0.1:8000/docs
- 健康检查：http://127.0.0.1:8000/health

## 项目结构
```
teacher-assistant/
├── app/
│   ├── main.py        # FastAPI 入口
│   ├── api/           # 路由
│   ├── core/          # 配置
│   ├── models/        # 数据库模型
│   ├── schemas/       # Pydantic 模型
│   ├── services/      # 业务逻辑（RAG、LLM 调用）
│   └── db/            # 数据库连接
├── tests/             # 测试
├── data/              # 教材、向量库等本地数据
├── .env.example       # 环境变量样例
├── requirements.txt
└── README.md
```
