import pymysql

def get_mysql_session():
    """
    Establece y devuelve una conexión a la base de datos MySQL.

    La función configura los parámetros de conexión, incluyendo:
    - host: Dirección del servidor MySQL (en este caso, 'mysql')
    - port: Puerto en el que escucha MySQL (por defecto 3306)
    - user: Usuario para autenticarse (en este caso, 'root')
    - password: Contraseña del usuario (en este caso, 'root')
    - database: Nombre de la base de datos a la que conectarse ('quitogo_db')
    - cursorclass: Tipo de cursor, en este caso, un cursor que devuelve resultados como diccionarios

    Retorna:
        Un objeto de conexión a la base de datos MySQL.
    """
    return pymysql.connect(
        host="mysql",               # Dirección del servidor MySQL
        port=3306,                  # Puerto estándar de MySQL
        user="root",                # Usuario de la base de datos
        password="root",            # Contraseña del usuario
        database="quitogo_db",      # Nombre de la base de datos
        cursorclass=pymysql.cursors.DictCursor  # Cursor que devuelve resultados como diccionario
    )
