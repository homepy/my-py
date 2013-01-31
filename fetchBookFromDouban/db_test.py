'''Test mysql connector'''
import mysql.connector
from mysql.connector import errorcode


db_conf = {
    'user': 'root',
    'password': '`',
    'host': 'localhost',
    'port':3306,
    'database': 'library',
    'raise_on_warnings': True,
}


def connect_db(config):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exists")
        else:
            print(err)
    return cnx

cnx = connect_db(db_conf)

#cnx.close()
print('end')
