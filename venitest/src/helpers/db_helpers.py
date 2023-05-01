import pymysql
import pdb

def read_from_db(sql):
    # connect to db
    connection = pymysql.connect(host='localhost', port=10006, user='root', password='root')
    connection.select_db('local')
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()
    # read from db
    return db_data
    # return the result
def get_order_from_db_by_order_no(order_no):
    sql = f"SELECT* FROM wp_posts WHERE ID={order_no} AND post_type = 'shop_order';"
    db_order = read_from_db(sql)
    pdb.set_trace()
    print(db_order)


get_order_from_db_by_order_no(89)