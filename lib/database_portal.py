from google.cloud.sql.connector import Connector
import pymysql
import os
import sqlalchemy
TESTARRAY = [1,2,3,4,5,6,7]
TESTARRAY_SHORT = [1,2,3,4,5,6]
# function to return the database connection
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
connector = Connector(
    enable_iam_auth=False,
    timeout=30,
)
def getconn() -> pymysql.connections.Connection:
    conn: pymysql.connections.Connection = connector.connect(
        "skifinder:us-central1:ski-finder-data",
        "pymysql",
        password=os.getenv("PASSWORD"),
        db="portal"
    )
    return conn

pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)


def clear_db ():
    stmt = sqlalchemy.text("DELETE FROM product")
    with pool.connect() as db_con:
      db_con.execute(stmt)

def add_row (row):
    if len(row) == 7:
      sql = "INSERT INTO product VALUES (%s, %s, %s, %s, %s, %s, %s)"
      
    else:
      sql = "INSERT INTO product(brand,title,img_url,price,compare,link_pure) VALUES (%s, %s, %s, %s, %s, %s)"
    
    val = tuple(row)  
     
    with pool.connect() as db_con:
      db_con.execute(sql,val)

def get_all():
    final = []
    with pool.connect() as db_con:
      results = db_con.execute("SELECT * FROM product").fetchall()
      for item in results:
        final.append(list(item))
    return final

clear_db()    


