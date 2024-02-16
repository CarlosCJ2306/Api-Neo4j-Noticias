from src.config.db import conexionDB
from src.schemas.UserSchema import SchemaUser
from src.schemas.PostSchema import SchemaPost

def obtener():
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:user) RETURN n"
        resultado = session.run(query)
        return resultado.value()
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def obtenerPorId(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:user {id: $id}) RETURN n"
        resultado = session.run(query, parameters = {"id" : id})
        return resultado.value()[0]
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def obtenerPorUserName(userName: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:user {username: $username}) RETURN n"
        resultado = session.run(query, parameters = {"username" : userName})
        return resultado.value()[0]
    except Exception as e:
        print(e)
    finally:
        driver.close()

def crear(user: SchemaUser):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "CREATE (n: user { id: $id, name: $name, lastName: $lastName, username: $username, email: $email, password: $password, access: $access })"
        session.run(query, parameters = {
            "id" : user.id,
            "name" : user.name,
            "lastName" : user.lastName,
            "username" : user.username,
            "email" : user.email,
            "password" : user.password,
            "access" : user.access
        })
        return {"message" : "user creado correctamente"}
    except Exception as e:
        print(e)
    finally:
        driver.close() 
        
def eliminar(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:user {id: $id}) DELETE n"
        session.run(query, parameters = {"id" : id})
        return {"message" : "user eliminado correctamente"}
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def actualizar(id: str, user: SchemaUser):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:user {id: $id}) SET n.name = $name, n.lastName = $lastName, n.username = $username, n.email = $email, n.password = $password, n.access = $access RETURN n"
        resultado = session.run(query, parameters = {
            "id" : id,
            "name" : user.name,
            "lastName" : user.lastName,
            "username" : user.username,
            "email" : user.email,
            "password" : user.password,
            "access" : user.access
        })
        return resultado.value()[0]
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def verificarRelacion(idUser: str, idPost: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = query = """MATCH (p:Post)-[:HAS_EDITED]->(u:user)
                           WHERE p.id = $idPost AND u.id = $idUser
                           RETURN COUNT(*) > 0 AS postEditUser"""
        resultado = session.run(query, parameters = {
            "idUser" : idUser,
            "idPost" : idPost
        })
        return resultado.value()[0]
    except Exception as e:
        print(e)
    finally:
        driver.close()

def relacionar(idUser: str, posts: list[SchemaPost]):
    try:
        driver = conexionDB()
        session = driver.session()
        for post in posts:
            query = "MATCH (u:user {id: $idUser}), (p:Post {id: $idPost}) CREATE (u)-[:HAS_EDITED]->(p)"
            if(verificarRelacion(idUser, post.id) == False):
                session.run(query, parameters = {
                    "idUser" : idUser,
                    "idPost" : post.id
                })
        return {"message" : "Relacion creada correctamente"}
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def obtenerPostUser(idUser: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (u:user {id: $idUser})-[:HAS_EDITED]->(p:Post) RETURN p"
        resultado = session.run(query, parameters = {"idUser" : idUser})
        return resultado.value()
    except Exception as e:
        print(e)
    finally:
        driver.close()