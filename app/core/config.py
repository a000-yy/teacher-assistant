import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    LLM_API_KEY:str=os.getenv("LLM_API_KEY","")
    LLM_BASE_URL:str=os.getenv("LLM_BASE_URL","https://api.deepseek.com")
    LLM_MODEL:str=os.getenv("LLM_MODEL","deepseek-chat")
    LLM_TEMPERATURE:float=float(os.getenv("LLM_TEMPERATURE","0.7"))

setting = Settings()