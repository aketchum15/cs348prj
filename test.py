from google.cloud.sql.connector import Connector
import sqlalchemy
import django

def getconn():
  connector = Connector();
  result = connector.connect(
    "cs348prj:us-central1:cs348prj",
    "pymysql",
    user="root",
    password="cs348",
    db="db1"
  )
  return result


if __name__ == '__main__':
  pool = sqlalchemy.create_engine( "mysql+pymysql://", creator=getconn,)
  
  data = [('asdf', 2), ('stuff', 3), ('jgrfhk', 4), ('rjrkj', 1), ('adam', 40), ('neha', 7), ('test', 69), ('data', 10)]
  print(django.get_version())

  with pool.connect() as db_conn:
    #db_conn.execute('CREATE TABLE test (data varchar(255), id int)')
    #for d in data:
    #  db_conn.execute(f'INSERT INTO test VALUE ("{d[0]}", {d[1]})')
    result = db_conn.execute("SELECT * FROM Performers").fetchall()

    for row in result:
      print(result)

  connector.close()
