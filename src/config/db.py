from dotenv import load_dotenv
import os
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv("NEO4J_URI")
AUTH = (os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))

def conexionDB():
    try:
        driver = GraphDatabase.driver(uri=URI, auth=AUTH)
        return driver
    except Exception as e:
        print(e)
        return None
    finally:
        driver.close()