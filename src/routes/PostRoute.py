from fastapi import APIRouter
from src.schemas.PostSchema import SchemaPost
from src.services.PostService import *

RoutePost = APIRouter()

@RoutePost.get("/")
def obtenerTodos():
    return obtener()

@RoutePost.get("/{id}")
def obtenerPostPorId(id: str):
    return obtenerPorId(id)

@RoutePost.get("/title/{title}")
def obtenerPostPortitle(title: str):
    return obtenerPorTitle(title)
    
@RoutePost.post("/crear")
def crearPost(post: SchemaPost):
    return crear(post)

@RoutePost.delete("/eliminar/{id}")
def eliminarPost(id: str):
    return eliminar(id)

@RoutePost.put("/actualizar/{id}")
def actualizarPost(id: str, post: SchemaPost):
    return actualizar(id, post)