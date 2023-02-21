from . import database
import os
from sqlalchemy import text


pool = database.connect_unix_socket()

def clear_db ():
    stmt = text("DELETE FROM test_product")
    pool.execute(stmt)

def add_row (row):
    if len(row) == 7:
      sql = "INSERT INTO test_product VALUES (%s, %s, %s, %s, %s, %s, %s)"
      stmt = text(sql)
    else:
      sql = "INSERT INTO test_product(brand,title,img_url,price,compare,link_pure) VALUES (%s, %s, %s, %s, %s, %s)"
      stmt = text(sql)
    val = tuple(row)  
     
    
    pool.execute(sql,val)

def get_all():
    final = []
    sql = text("SELECT * FROM test_product")
    results = pool.execute(sql).fetchall()
    for item in results:
      final.append(list(item))
    return final

print(get_all())