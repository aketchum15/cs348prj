from google.cloud.sql.connector import Connector
import sqlalchemy
import pymysql

# initialize Connector object
connector = Connector()

def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "cs348prj:us-central1:cs348prj",
        "pymysql",
        user="root",
        password="cs348",
        db="db1"
    )
    return conn

    # create connection pool
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


with pool.connect() as db_conn:
    # insert into database
    db_conn.execute("SELECT * from test")

