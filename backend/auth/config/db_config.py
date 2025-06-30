# Importamos la librería pymysql, que permite conectar y trabajar con bases de datos MySQL desde Python
import pymysql

def get_mysql_session():
    """
    Establece y devuelve una conexión a la base de datos MySQL.

    La función configura la conexión con los siguientes parámetros:
        - host: Dirección del servidor MySQL (en este caso, un contenedor o servidor llamado "mysql")
        - port: Puerto en el que escucha el servidor MySQL (por defecto 3306)
        - user: Usuario de la base de datos (en este caso, "root")
        - password: Contraseña del usuario (en este caso, "root")
        - database: Nombre de la base de datos a la que se conectará ("quitogo_db")
        - cursorclass: Clase de cursor utilizada; en este caso, DictCursor para obtener resultados como diccionarios

    Esto permite realizar consultas y operaciones en la base de datos de manera sencilla.

    Returns:
        pymysql.connections.Connection: Objeto de conexión a la base de datos MySQL
    """
    return pymysql.connect(
        host="mysql",             # Dirección del servidor MySQL
        port=3306,                # Puerto del servidor MySQL
        user="root",              # Usuario de la base de datos
        password="root",          # Contraseña del usuario
        database="quitogo_db",    # Nombre de la base de datos a utilizar
        cursorclass=pymysql.cursors.DictCursor  # Cursor que devuelve resultados como diccionarios
    )
