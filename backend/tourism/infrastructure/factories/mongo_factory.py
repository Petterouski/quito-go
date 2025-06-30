from domain.interfaces.repository_factory import RepositoryFactory
from infrastructure.mongo.reservation_dao import MongoReservationDAO

class MongoFactory(RepositoryFactory):
    def __init__(self, db):
        self.db = db

    def create_reservation_dao(self):
        return MongoReservationDAO(self.db)

    def create_package_dao(self):
        raise NotImplementedError("Este factory es solo para reservas.")
