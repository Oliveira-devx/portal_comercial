import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def concetar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME", "banco_v3"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSOWRD", "admin"),
        autocommit=False, # nada é gravado sem commit()
    )

def consultar(sql, parametros=()):
    with concetar() as con, con.cursor(dictionary=True) as cur:
        cur.execute(sql, parametros)
        return cur.fetchall()
    