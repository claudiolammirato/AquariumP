import mysql.connector as mysql
import Pass

def connection():
    # enter your server IP address/domain name
    HOST = "remotemysql.com" # or "domain.com"
    # database name, if you want just to connect to MySQL server, leave it empty
    DATABASE = Pass.database
    # this is the user you create
    USER = Pass.username
    # user password
    PASSWORD = Pass.password
    # connect to MySQL server
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    print("Connected to:", db_connection.get_server_info())
    # enter your code here!)