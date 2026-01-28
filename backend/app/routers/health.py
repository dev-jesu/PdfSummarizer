from fastapi import APIRouter
from app.database import get_db_connection

router = APIRouter()

@router.get("/db-test")
def db_test():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {
        "db_connection": "successful",
        "result": result
    }
