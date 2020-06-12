

import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect("dbname='setlife'")
        conn.set_client_encoding('UTF8')
        # print(conn)
    except Exception as e:
        print("Unable to connect to the database")
    return conn

CONNECTION = connect()

"""
Using sqlalachemy
"""
from sqlalchemy import create_engine
db = create_engine('postgresql://tuanho:1234@localhost:5432/setlife')
CONNECTION2 = db.connect()



