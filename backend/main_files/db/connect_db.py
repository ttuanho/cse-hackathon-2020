# By
# ████████╗██╗   ██╗ █████╗ ███╗   ██╗    ██╗  ██╗ ██████╗ 
# ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║    ██║  ██║██╔═══██╗
#    ██║   ██║   ██║███████║██╔██╗ ██║    ███████║██║   ██║
#    ██║   ██║   ██║██╔══██║██║╚██╗██║    ██╔══██║██║   ██║
#    ██║   ╚██████╔╝██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝
#    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ 

# Email: ttuan.ho@outlook.com                                                         

import os
import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect("dbname='doctors' host='localhost'")
        # conn = psycopg2.connect("dbname='doctors' user='postgres' host='localhost')
        # conn = psycopg2.connect("dbname='tracking' user='postgres' host='/cloudsql/robotic-column-277322:us-central1:tracking' password='2907Tuan'")
        # conn = psycopg2.connect(os.environ['PSYCOPG2_POSTGRESQL_URI'])
        conn.set_client_encoding('UTF8')
        # print(conn)
    except Exception as e:
        print("Unable to connect to the database")
    return conn

CONNECTION = connect()

"""
Using sqlalachemy
"""
# from sqlalchemy import create_engine
# db = create_engine('postgresql://tuanho:1234@localhost:5432/setlife', echo=True)
# CONNECTION2 = db.connect()
# Session = sessionmaker(db)  
# session = Session()


