import pdfplumber #pdf解析库
def extract_text(pdf_path) -> str:
    text=""  #定义空字符串积累所有页面的文字
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text+=(page.extract_text() or "") +"\n"
    return text