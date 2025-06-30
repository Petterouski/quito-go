from domain.interfaces.repository_factory import RepositoryFactory
from infrastructure.mysql.package_dao import MySQLPackageDAO

# Fábrica concreta que crea DAOs para MySQL
class MySQLFactory(RepositoryFactory):
    def __init__(self, db):
        self.db = db    # Guarda la conexión a la base de datos

    def create_package_dao(self):     # Retorna una instancia del DAO MySQL
        return MySQLPackageDAO(self.db)

    
    