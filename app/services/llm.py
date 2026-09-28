from openai import OpenAI
from app.core.config import setting


client = OpenAI(api_key=setting.LLM_API_KEY,base_url=setting.LLM_BASE_URL)

def chat(prompt:str,system:str = "你是一个教学助手") -> str:
    resp = client.chat.completions.create(
        model=setting.LLM_MODEL,#模型名称
        messages=[    #对话列表消息
            {"role":"system","content":system},#系统提示：设定角色
            {"role":"user","content":prompt},#用户输入
        ],
        temperature=setting.LLM_TEMPERATURE,#随机性，0稳定，1发散
        max_tokens=1024#最多生成的token数
    )
    return resp.choices[0].message.content#取第一条回复的文本