# Importa la clase ABC y el decorador abstractmethod para definir clases y métodos abstractos
from abc import ABC, abstractmethod

# Importa la entidad Package desde el módulo de entidades
from domain.entities.package import Package

# Define una interfaz abstracta que actúa como contrato para cualquier clase que implemente un repositorio de paquetes
class PackageRepository(ABC):
    @abstractmethod
    def create(self, package: Package):
        """
        Método abstracto para crear un nuevo paquete en el repositorio.
        Recibe una instancia de Package y debe implementar la lógica para almacenarla.
        """
        pass

    @abstractmethod
    def list_all(self):
        """
        Método abstracto para listar todos los paquetes almacenados en el repositorio.
        Debe devolver una colección de objetos Package.
        """
        pass
