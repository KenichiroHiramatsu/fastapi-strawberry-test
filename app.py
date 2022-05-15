# from typing import Optional
# import streamlit as st
# import requests

# page = st.sidebar.selectbox("Choose your page", ['taskList', 'addTask'])

# if page == 'addTask':
#     st.title("APIテスト(addTask)")

#     with st.form(key='add'):
#         title: str = st.text_input("タスク名", max_chars=12)
#         description: Optional[str] = st.text_input("説明")
#         data = {
#             'title': title,
#             'description': description
#         }
#         submit_button = st.form_submit_button(label="送信")

#     if submit_button:
#         st.write("## 送信データ")
#         st.json(data)
#         st.write("## レスポンス結果")
#         url = 'http://127.0.0.1:8000/graphql'
#         headers = {
#             "Content-Type": "application/json",
#         }
#        # graphqlのqueryを記述
#         query = """
#         mutation($input:AddTaskInput!) {
#         taskAdd(taskInput:$input) {
#             id
#             title
#             description
#         }
#         }
#         """
#         variables = {
#             "input": data
#         }
#         response = requests.post(
#             url, json={"query": query, "variables": variables}, headers=headers
#         )
#         st.json(response.content.decode())

# elif page == 'taskList':
#     st.title("工事中")
#     # st.title("APIテスト(taskList)")
#     # url = 'http://127.0.0.1:8000/graphql'
#     # headers = {
#     #     "Content-Type": "application/json",
#     # }
#     # # graphqlのqueryを記述
#     # query = """
#     #     query() {
#     #     tasks() {title}
#     #     }
#     # """
#     # response = requests.get(
#     #     url, headers=headers
#     # )
#     # print(response.content)
#     # st.json(response.content)
