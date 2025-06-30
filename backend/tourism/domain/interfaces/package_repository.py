# Define una interfaz abstracta que actúa como contrato para cualquier clase DAO
from abc import ABC, abstractmethod   # Para definir clases abstractas
from domain.entities.package import Package   # Importa la entidad Package

class PackageRepository(ABC):
    @abstractmethod
    def create(self, package: Package): pass

    @abstractmethod
    def list_all(self): pass
