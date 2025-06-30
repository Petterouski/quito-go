# Define una fábrica abstracta que debe saber cómo crear DAOs para paquetes
from abc import ABC, abstractmethod

class RepositoryFactory(ABC):
    @abstractmethod
    def create_package_dao(self): pass  # Método que debe devolver un objeto DAO de paquetes
