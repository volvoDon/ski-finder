import mysql.connector
TESTARRAY = [1,2,3,4,5,6,7]
TESTARRAY_SHORT = [1,2,3,4,5,6]
mydb = mysql.connector.connect(
  host='localhost',
  user="root",
  database="portal",
)

mycursor = mydb.cursor()

def clear_db ():
    mycursor.execute("DELETE FROM product")
    mydb.commit()

def add_row (row):
    if len(row) == 7:
      sql = "INSERT INTO product VALUES (%s, %s, %s, %s, %s, %s, %s)"
      
    else:
      sql = "INSERT INTO product(brand,title,img_url,price,compare,link_pure) VALUES (%s, %s, %s, %s, %s, %s)"
    
    val = tuple(row)  
     
    mycursor.execute(sql,val)
    mydb.commit()

def get_all():
    final = []
    mycursor.execute("SELECT * FROM product")
    results = mycursor.fetchall()
    for item in results:
      final.append(list(item))
    return final


