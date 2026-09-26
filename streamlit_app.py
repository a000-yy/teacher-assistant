import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="教师助手测试台", layout="wide")
st.title("教师助手 · 测试界面")
st.caption("前端通过 HTTP 调用 FastAPI 接口，需先启动后端 uvicorn app.main:app --reload")

tab_user, tab_doc = st.tabs(["用户管理", "文档管理"])

# ===================== 用户管理 =====================
with tab_user:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("创建用户")
        with st.form("create_user"):
            username = st.text_input("用户名")
            email = st.text_input("邮箱")
            if st.form_submit_button("创建"):
                try:
                    r = requests.post(f"{API}/users",
                                      json={"username": username, "email": email})
                    if r.ok:
                        st.success(f"创建成功：{r.json()}")
                    else:
                        st.error(f"{r.status_code}: {r.text}")
                except Exception as e:
                    st.error(f"请求失败：{e}")

    with col2:
        st.subheader("用户列表")
        if st.button("刷新用户列表"):
            st.rerun()
        try:
            users = requests.get(f"{API}/users", timeout=5).json()
            st.dataframe(users, use_container_width=True)
        except Exception as e:
            st.error(f"获取失败（后端启动了吗？）：{e}")

    st.divider()
    st.subheader("删除用户")
    del_uid = st.number_input("要删除的用户ID", min_value=1, step=1, key="del_uid")
    if st.button("删除该用户"):
        try:
            r = requests.delete(f"{API}/users/{del_uid}")
            if r.ok:
                st.success(r.json())
            else:
                st.error(f"{r.status_code}: {r.text}")
        except Exception as e:
            st.error(f"请求失败：{e}")

# ===================== 文档管理 =====================
with tab_doc:
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("上传文档")
        with st.form("upload_doc"):
            owner_id = st.number_input("所属用户ID", min_value=1, step=1)
            title = st.text_input("文档标题")
            subject = st.text_input("学科（可选）")
            file = st.file_uploader("选择文件")
            if st.form_submit_button("上传"):
                if file is None:
                    st.warning("请先选择文件")
                else:
                    try:
                        files = {"file": (file.name, file.getvalue())}
                        data = {"owner_id": str(owner_id),
                                "title": title,
                                "subject": subject}
                        r = requests.post(f"{API}/documents/upload",
                                          data=data, files=files)
                        if r.ok:
                            st.success(f"上传成功：{r.json()}")
                        else:
                            st.error(f"{r.status_code}: {r.text}")
                    except Exception as e:
                        st.error(f"请求失败：{e}")

    with col2:
        st.subheader("文档列表")
        if st.button("刷新文档列表"):
            st.rerun()
        try:
            docs = requests.get(f"{API}/documents", timeout=5).json()
            st.dataframe(docs, use_container_width=True)
        except Exception as e:
            st.error(f"获取失败：{e}")

    st.divider()
    st.subheader("按用户查询文档")
    q_uid = st.number_input("用户ID", min_value=1, step=1, key="q_uid")
    if st.button("查询该用户的文档"):
        try:
            r = requests.get(f"{API}/documents/user/{q_uid}")
            if r.ok:
                st.dataframe(r.json(), use_container_width=True)
            else:
                st.error(f"{r.status_code}: {r.text}")
        except Exception as e:
            st.error(f"请求失败：{e}")
