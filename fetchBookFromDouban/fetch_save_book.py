'''fentch book from douban.com and save into mysql'''
import httplib2
import json
import datetime
import random
import mysql.connector
from mysql.connector import errorcode


DB_CONF = {
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
    '''转换日期字符串'yyyy-mm-dd'或'yyyy-mm'为datetime.date'''
    try:
        return datetime.datetime.strptime(ym_str, '%Y-%m').date()
    except ValueError:
        return datetime.datetime.strptime(ym_str, '%Y-%m-%d').date()


def format_book_dict(book_dict):
    '''修改dict以适应自定义表结构'''
    book_dict['pubdate'] = convert_str2date(book_dict['pubdate'])
    book_dict['author'] = ', '.join(book_dict['author'])
    book_dict['translator'] = ', '.join(book_dict['translator'])
    book_dict['image'] = book_dict['images']['large']
    dot = book_dict['price'].find('.')
    book_dict['price'] = float(book_dict['price'][0: (dot + 1)])
    if '平装' in book_dict['binding']:
        book_dict['binding'] = '0'
    elif '精装' in book_dict['binding']:
        book_dict['binding'] = '1'
    else:
        book_dict['binding'] = '2'

    del book_dict['rating']
    del book_dict['tags']
    del book_dict['images']
    return book_dict


cnx = connect_db(DB_CONF)
cursor = cnx.cursor()   # 游标
sql_add = ("INSERT INTO t_book "
           "(id, isbn10, isbn13, title, origin_title, "
           "alt_title, subtitle, url, image, author, "
           "translator, publisher, pubdate, binding, "
           "price, pages, author_intro, summary) "
           "VALUES ( "
           "%(id)s, %(isbn10)s, %(isbn13)s, %(title)s, %(origin_title)s,"
           "%(alt_title)s, %(subtitle)s, %(url)s, %(image)s, %(author)s,"
           "%(translator)s, %(publisher)s, %(pubdate)s, %(binding)s,"
           "%(price)s, %(pages)s, %(author_intro)s, %(summary)s)")
#print(sql_add)

h = httplib2.Http('.cache')
for count in range(0, 200):
    bid = random.randint(1000001, 1899999)
    resp, content = h.request('https://api.douban.com/v2/book/' + str(bid))
    if resp.status == 403:
        print('Ouch!403，FORBIDDEN！')
        break
    elif resp.status == 200:    # SUCCESS
        b_str = content.decode('utf-8')
        b_dict = json.loads(b_str)
        b_dict = format_book_dict(b_dict)
#        for x, y in b_dict.items():
#           if not isinstance(y, str):
#           print('type:', x, type(y))
#           print(x, y)
#           print()
        cursor.execute(sql_add, b_dict)
        print('insert book id = ', bid)
# Make sure datas is committed to the database

cnx.commit()
cursor.close()
cnx.close()
print('End')
