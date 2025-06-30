import pymysql

def get_mysql_session():
    return pymysql.connect(
        host="mysql",
        port=3306,
        user="root",
        password="root",
        database="quitogo_db",
        cursorclass=pymysql.cursors.DictCursor
    )
