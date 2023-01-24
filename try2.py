import mysql as mysql
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="sanket",
  password="test123"
)

mycursor = mydb.cursor()