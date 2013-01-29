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
    return datetime.datetime.strptime(ym_str, '%Y-%M').date()


def format_dict(json_dict):
    json_dict['pubdate'] = convert_str2date(json_dict['pubdate'])
    json_dict['author'] = ', '.join(json_dict['author'])
    json_dict['translator'] = ', '.join(json_dict['translator'])
    json_dict['image'] = json_dict['images']['large']
    dot = json_dict['price'].find('.')
    json_dict['price'] = float(json_dict['price'][0: dot+2])
    if json_dict['binding'] == '平装':
        json_dict['binding'] = '0'
    elif json_dict['binding'] == '精装':
        json_dict['binding'] = '1'
    else:
        json_dict['binding'] = '2'

    del json_dict['rating']
    del json_dict['tags']
    del json_dict['images']
    return json_dict


cnx = connect_db(db_conf)
cursor = cnx.cursor()
sql_add = ("INSERT INTO t_book "
        "(id, isbn10, isbn13, title, origin_title, "
        "alt_title, subtitle, url, image,"
        "author, translator, publisher, pubdate, binding, "
        "price, pages, author_intro, summary) "
        "VALUES ( "
        "%(id)s, %(isbn10)s, %(isbn13)s, %(title)s, %(origin_title)s,"
        "%(alt_title)s, %(subtitle)s, %(url)s, %(image)s, "
        "%(author)s, %(translator)s, %(publisher)s, %(pubdate)s, %(binding)s, "
        "%(price)s, %(pages)s, %(author_intro)s, %(summary)s)")
print(sql_add)
h = httplib2.Http('.cache')
bid = 1220562
resp, content = h.request('https://api.douban.com/v2/book/' + str(bid))
if resp.status == 200:
    b_str = content.decode('utf-8')
    b_dict = json.loads(b_str)
    b_dict = format_dict(b_dict)
    for x, y in b_dict.items():
#        if not isinstance(y, str):
        print('type:', x, type(y))
        print(x, y)
#            print()
    cursor.execute(sql_add, b_dict)
# Make sure datas is committed to the database
cnx.commit()
cursor.close()
cnx.close()


def save_db(b_disct):
    pass


# httplib2.debugslevel = 1
#h = httplib2.Http('.cache')
#bid = 1220562
#while bid < 1220600:
#    resp, content = h.request('https://api.douban.com/v2/book/' + str(bid))
#    if resp.status == 200:
#        b_str = content.decode('utf-8')
#        b_dict = json.loads(b_str)
#
#    bid = bid + 1

#cnx.close()
print('end')
