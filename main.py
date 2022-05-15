import os
from typing import List
import strawberry
import uvicorn
from tasks.models import Task

from tasks.resolvers import add_task, delete_task, get_tasks, get_task, update_task
from tasks.types import TaskType

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from typing import Optional
import streamlit as st
import requests


@strawberry.type
class Query:
    task: TaskType = strawberry.field(resolver=get_task)
    tasks: List[TaskType] = strawberry.field(resolver=get_tasks)


@strawberry.type
class Mutation:
    task_add: TaskType = strawberry.field(resolver=add_task)
    task_update: TaskType = strawberry.field(resolver=update_task)
    task_delete: TaskType = strawberry.field(resolver=delete_task)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(
    schema=schema, graphiql=False)  # graphiqlは本番環境ではFalseに
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def index():
    # return {"Hello": "World from FastAPI"}

    page = st.sidebar.selectbox("Choose your page", ['taskList', 'addTask'])

    if page == 'addTask':
        st.title("APIテスト(addTask)")
        with st.form(key='add'):
            title: str = st.text_input("タスク名", max_chars=12)
            description: Optional[str] = st.text_input("説明")
            data = {
                'title': title,
                'description': description
            }
            submit_button = st.form_submit_button(label="送信")

        if submit_button:
            st.write("## 送信データ")
            st.json(data)
            st.write("## レスポンス結果")
            url = 'http://127.0.0.1:8000/graphql'
            headers = {
                "Content-Type": "application/json",
            }
        # graphqlのqueryを記述
            query = """
            mutation($input:AddTaskInput!) {
            taskAdd(taskInput:$input) {
                id
                title
                description
            }
            }
            """
            variables = {
                "input": data
            }
            response = requests.post(
                url, json={"query": query, "variables": variables}, headers=headers
            )
            st.json(response.content.decode())

    elif page == 'taskList':
        st.title("工事中")
        # st.title("APIテスト(taskList)")
        # url = 'http://127.0.0.1:8000/graphql'
        # headers = {
        #     "Content-Type": "application/json",
        # }
        # # graphqlのqueryを記述
        # query = """
        #     query() {
        #     tasks() {title}
        #     }
        # """
        # response = requests.get(
        #     url, headers=headers
        # )
        # print(response.content)
        # st.json(response.content)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=os.getenv(
        "PORT", default=5000), log_level="info")
