from pymongo import MongoClient

def get_mongo_client():
    """
    Establece y devuelve una conexión a la base de datos MongoDB.

    La función crea un cliente de MongoDB que se conecta a la instancia de MongoDB en
    la dirección 'mongodb://mongo:27017/'. Luego, accede y devuelve la base de datos
    llamada 'quitogo_reservations_db'.

    Returns:
        Database: Objeto que representa la base de datos 'quitogo_reservations_db'.
    """
    # Crear un cliente de MongoDB apuntando al servidor en la URL especificada
    client = MongoClient("mongodb://mongo:27017/")

    # Acceder a la base de datos 'quitogo_reservations_db' mediante el cliente
    db = client["quitogo_reservations_db"]

    # Devolver la referencia a la base de datos
    return db
