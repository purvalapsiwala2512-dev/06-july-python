import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="your_password"
    )
    print("Connection successful")
    connection.close()
except pymysql.MySQLError as e:
    print("Connection error:",e)