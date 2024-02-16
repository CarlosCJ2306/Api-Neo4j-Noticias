from src.config.db import conexionDB
from src.schemas.PostSchema import SchemaPost

def obtener():
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Post) RETURN n"
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
        query = "MATCH (n:Post {id: $id}) RETURN n"
        resultado = session.run(query, parameters = {"id" : id})
        return resultado.value()[0]
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def obtenerPorTitle(title: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Post {title: $title}) RETURN n"
        resultado = session.run(query, parameters = {"title" : title})
        return resultado.value()[0]
    except Exception as e:
        print(e)
    finally:
        driver.close()

def crear(post: SchemaPost):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "CREATE (n: Post { id: $id, title: $title, description: $description, content: $content, summary: $summary, publishedDate: $publishedDate })"
        session.run(query, parameters = {
            "id" : post.id,
            "title" : post.title,
            "description" : post.description,
            "content" : post.content,
            "summary" : post.summary,
            "publishedDate" : str(post.publishedDate)
        })
        return {"message" : "Post creado correctamente"}
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def verificarRelacion( idpost: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Post {id: $id})--() RETURN COUNT(n) > 0 AS tieneRelacion"
        resultado = session.run(query, parameters={"id": idpost})
        return resultado.value()[0]
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def eliminarRelacion(idpost: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Post {id: $id})-[r]-(m:user) DELETE r"
        session.run(query, parameters = {"id" : idpost})
        return {"message" : "Relacion eliminada correctamente"}
    except Exception as e:
        print(e)
    finally:
        driver.close()

        
def eliminar(id: str):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Post {id: $id}) DELETE n"
        if(verificarRelacion(id)):
            eliminarRelacion(id)
        session.run(query, parameters = {"id" : id})
        return {"message" : "Post eliminado correctamente"}
    except Exception as e:
        print(e)
    finally:
        driver.close()
        
def actualizar(id: str, post: SchemaPost):
    try:
        driver = conexionDB()
        session = driver.session()
        query = "MATCH (n:Post {id: $id}) SET n.title = $title, n.description = $description, n.content = $content, n.summary = $summary, n.publishedDate = $publishedDate"
        session.run(query, parameters = {
            "id" : id,
            "title" : post.title,
            "description" : post.description,
            "content" : post.content,
            "summary" : post.summary,
            "publishedDate" : str(post.publishedDate)
        })
        return {"message" : "Post actualizado correctamente"}
    except Exception as e:
        print(e)
    finally:
        driver.close()