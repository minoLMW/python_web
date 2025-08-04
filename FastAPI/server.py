from fastapi import FastAPI
from pydantic import BaseModel

users = {
    0: {"userid": "apple", "name": "김사과"},
    1: {"userid": "banana", "name": "반하나"},
    2: {"userid": "orange", "name": "오렌지"}
}

application = FastAPI()

@application.get("/users/{id}")
def find_user(id: int):
    user =users.get(id)
    if user is None:
        return {"error": "해당 id 없음"}
    return user

@application.get("/users/{id}/{key}")
def find_user_by_key(id: int, key: str):
    user = users.get(id)
    if user is None or key not in user:
        return {"error": "잘못된 id 또는 key"}
    return user[key]

@application.get("/id-by-name")
def find_user_by_name(name: str):
    for idx, user in users.items():
        if user["name"] == name:
            return user
    return {"error": "데이터를 찾기 못함"}

class User(BaseModel):
    userid: str
    name: str

@application.post("/users/{id}")
def create_user(id: int, user: User):
    if id in users:
        return {"error": "이미 존재하는 키"}
    users[id] = user.model_dump()
    return {"success": "ok"}

class UserForUpdate(BaseModel):
    userid: str | None = None
    name: str | None = None

@application.put("/users/{id}")
def update_user(id: int, user: UserForUpdate):
    if id not in users:
        return {"error": "id가 존재하지 않음"}
    
    if user.userid is not None:
        users[id]["userid"] = user.userid
    if user.name is not None:
        users[id]["name"] = user.name

    return {"success": "ok"}

@application.delete("/users/{id}")
def delete_user(id: int):
    if id not in users:
        return {"error": "존재하지 않는 사용자"}
    users.pop(id)
    return {"success": "ok"}