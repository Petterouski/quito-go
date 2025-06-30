# Importa la clase ABC y el decorador abstractmethod del módulo abc para crear clases abstractas
from abc import ABC, abstractmethod

# Define una clase abstracta que sirve como fábrica para crear objetos DAO relacionados con paquetes
class RepositoryFactory(ABC):
    @abstractmethod
    def create_package_dao(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        Debe devolver una instancia de un DAO que gestione los datos de paquetes.
        """
        pass  # La implementación concreta será proporcionada en las clases derivadas
