import uvicorn
from fastapi import FastAPI

app = FastAPI(title='Trading app')

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
]


@app.get('/users/{user_id}')
def hello(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
