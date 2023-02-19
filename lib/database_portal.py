import database
import os
from sqlalchemy import text

def getconn():
    with Connector() as connector:
        conn = connector.connect(
            "skifinder:us-central1:ski-finder-data", # Cloud SQL Instance Connection Name
            "mysql",
            user="root",
            password=os.getenv("PASSWORD"),
            db="portal",
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

print(get_all())