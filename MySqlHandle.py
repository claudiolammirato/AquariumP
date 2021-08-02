import mysql.connector as mysql

def connection():
    # enter your server IP address/domain name
    HOST = "remotemysql.com" # or "domain.com"
    # database name, if you want just to connect to MySQL server, leave it empty
    DATABASE = "kcKWrZgF5e"
    # this is the user you create
    USER = "kcKWrZgF5e"
    # user password
    PASSWORD = "pBn3qUbnL3"
    # connect to MySQL server
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    print("Connected to:", db_connection.get_server_info())
    # enter your code here!)