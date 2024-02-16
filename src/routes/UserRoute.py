from fastapi import APIRouter
from src.schemas.UserSchema import SchemaUser
from src.schemas.PostSchema import SchemaPost
from src.services.UserService import *

RouteUser = APIRouter()

@RouteUser.get("/")
def obtenerTodos():
    return obtener()

@RouteUser.get("/{id}")
def obtenerUserPorId(id: str):
    return obtenerPorId(id)

@RouteUser.get("/userName/{userName}")
def obtenerUserPorUserName(userName: str):
    return obtenerPorUserName(userName)
    
@RouteUser.post("/crear")
def crearUser(User: SchemaUser):
    return crear(User)

@RouteUser.delete("/eliminar/{id}")
def eliminarUser(id: str):
    return eliminar(id)

@RouteUser.put("/actualizar/{id}")
def actualizarUser(id: str, User: SchemaUser):
    return actualizar(id, User)

@RouteUser.post("/{iduser}/post")
def crearRelacion(iduser: str, posts: list[SchemaPost]):
    return relacionar(iduser, posts)

@RouteUser.get("/{iduser}/posts")
def obtenerPostdeUser(iduser: str):
    return obtenerPostUser(iduser)