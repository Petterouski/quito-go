# Importa la interfaz base para la fábrica de repositorios
from domain.interfaces.repository_factory import RepositoryFactory
# Importa la implementación concreta del DAO para paquetes en MySQL
from infrastructure.mysql.package_dao import MySQLPackageDAO


class MySQLFactory(RepositoryFactory):
    """
    Implementación concreta de la fábrica de repositorios para bases de datos MySQL.

    Esta clase se encarga de crear instancias de los Data Access Objects (DAOs)
    específicos para MySQL, como el DAO de paquetes.
    """

    def __init__(self, db):
        """
        Inicializa la fábrica con una conexión a la base de datos MySQL.

        Args:
            db (object): Objeto de conexión a la base de datos MySQL.
        """
        self.db = db  # Almacena la conexión a la base de datos

    def create_package_dao(self):
        """
        Crea y devuelve una instancia del DAO de paquetes para MySQL.

        Returns:
            MySQLPackageDAO: Instancia del DAO para acceder a los datos de paquetes en MySQL.
        """
        return MySQLPackageDAO(self.db)
