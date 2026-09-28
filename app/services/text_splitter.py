def split_text(text:str,chunk_size:int=500,overlap:int=50) -> list[str]:
    chunks=[]
    start=0
    while start<len(text):
        end=start+chunk_size
        chunks.append(text[start:end])
        start=end-overlap
    return chunks
    """
    参数：
    text：要切分的原文
    chunk_size=500：每块最大长度（默认 500 字符）
    overlap=50：相邻块重叠的字符数（默认 50）
    返回 list[str]：文本块的列表
    执行过程（用例子演示）： 假设 text = "0123456789ABCDEFGHIJ"（20 字符），chunk_size=5，overlap=2：
    轮次	start	end=start+5	取出的块	下一轮 start=end-2
    1	0	5	01234	3
    2	3	8	34567	6
    3	6	11	6789A	9
    """
