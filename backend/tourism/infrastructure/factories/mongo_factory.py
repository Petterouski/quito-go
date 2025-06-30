# Importación de la interfaz base para los repositorios
from domain.interfaces.repository_factory import RepositoryFactory

# Importación del Data Access Object (DAO) específico para reservas en MongoDB
from infrastructure.mongo.reservation_dao import MongoReservationDAO

class MongoFactory(RepositoryFactory):
    """
    Implementación concreta de la interfaz RepositoryFactory para crear 
    objetos DAO específicos de MongoDB.

    Este factory se encarga de producir instancias de DAOs que interactúan
    con la base de datos MongoDB, facilitando así la abstracción y desacoplamiento
    de las operaciones de persistencia.
    """

    def __init__(self, db):
        """
        Constructor de la clase MongoFactory.

        Args:
            db (object): La instancia de la conexión o cliente de la base de datos MongoDB.
        """
        self.db = db

    def create_reservation_dao(self):
        """
        Crea y devuelve una instancia del DAO para reservas en MongoDB.

        Returns:
            MongoReservationDAO: Objeto DAO para operaciones relacionadas con reservas.
        """
        return MongoReservationDAO(self.db)

    def create_package_dao(self):
        """
        Método no implementado, ya que este factory solo soporta reservas.

        Levanta una excepción si se intenta crear un DAO de paquetes.
        """
        raise NotImplementedError("Este factory es solo para reservas.")
