'''fentch book from douban.com and save into mysql'''
import httplib2
import json
import datetime
import mysql.connector
from mysql.connector import errorcode


db_conf = {
    'user': 'root',
    'password': '`',
    'host': '127.0.0.1',
    'port': 3306,
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

def convert_str2date(ym_str):
    return datetime.datetime.strptime(ym_str,'%Y-%M').date()

cnx = connect_db(db_conf)
cursor = cnx.cursor()
sql_add = ("INSERT INTO t_book "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
emp_no = cursor.lastrowid
# Insert salary information
# data_salary = {
#   'emp_no': emp_no,
#   'salary': 50000,
#   'from_date': tomorrow,
#   'to_date': date(9999, 1, 1),
# }
cursor.execute(add_salary, data_salary)
# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()


def save_db(b_dict):
    pass


# httplib2.debuglevel = 1
h = httplib2.Http('.cache')
bid = 1220562
while bid < 1220600:
    resp, content = h.request('https://api.douban.com/v2/book/' + str(bid))
    if resp.status == 200:
        b_str = content.decode('utf-8')
        b_dict = json.loads(b_str)

    bid = bid + 1




cnx.close()
print('end')
