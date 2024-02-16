from fastapi import FastAPI
from src.routes.PostRoute import RoutePost
from src.routes.UserRoute import RouteUser

app = FastAPI()

@app.get('/')
def root():
    return {"message" : "Welcome to my api CJ"}

app.include_router(RoutePost, prefix="/cj/post", tags=["Post"])
app.include_router(RouteUser, prefix="/cj/user", tags=["User"])