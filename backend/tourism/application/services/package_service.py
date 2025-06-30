# Importa la clase Data Transfer Object (DTO) para paquetes
from domain.dto.package_dto import PackageDTO
# Importa la entidad Package que representa la estructura de un paquete
from domain.entities.package import Package
# Importa la función para registrar acciones de auditoría en MongoDB
from infrastructure.mongo.audit_logger import log_action

class PackageService:
    """
    Servicio que gestiona las operaciones relacionadas con paquetes, como creación, listado,
    actualización y eliminación. Utiliza un DAO (Data Access Object) para interactuar con la base de datos.
    """

    def __init__(self, factory):
        """
        Inicializa el servicio con una fábrica que crea el DAO de paquetes.
        
        :param factory: Objeto factory que tiene el método create_package_dao()
        """
        # Crea una instancia del DAO de paquetes usando la fábrica proporcionada
        self.package_dao = factory.create_package_dao()

    def create_package(self, dto: PackageDTO):
        """
        Crea un nuevo paquete en la base de datos a partir de un DTO.
        
        :param dto: Objeto PackageDTO que contiene los datos del paquete a crear
        """
        # Convierte el DTO en una instancia de la entidad Package usando model_dump()
        package = Package(**dto.model_dump())
        # Inserta el nuevo paquete en la base de datos mediante el DAO
        self.package_dao.create(package)
        # Opcional: registrar acción de creación en el log de auditoría
        # log_action("create", package)

    def list_packages(self):
        """
        Obtiene y devuelve una lista de todos los paquetes existentes en la base de datos.
        
        :return: Lista de objetos Package
        """
        # Llama al DAO para obtener la lista completa de paquetes
        return self.package_dao.list_all()

    def update_package(self, package_id: int, dto: PackageDTO):
        """
        Actualiza los datos de un paquete existente usando su ID y un DTO actualizado.
        
        :param package_id: Identificador del paquete a actualizar
        :param dto: Objeto PackageDTO con los datos actualizados del paquete
        :return: Diccionario con mensaje de confirmación
        """
        # Crea una instancia de Package con el ID proporcionado y los datos del DTO
        # exclude_unset=True asegura que solo se actualicen los campos proporcionados
        package = Package(id=package_id, **dto.model_dump(exclude_unset=True))
        # Actualiza el paquete en la base de datos mediante el DAO
        self.package_dao.update(package)
        # Opcional: registrar acción de actualización en el log de auditoría
        # log_action("update", package)
        return {"message": "Package updated"}

    def delete_package(self, package_id: int):
        """
        Elimina un paquete de la base de datos usando su ID.
        
        :param package_id: Identificador del paquete a eliminar
        :return: Diccionario con mensaje de confirmación
        """
        # Llama al DAO para eliminar el paquete con el ID especificado
        self.package_dao.delete(package_id)
        # Opcional: registrar acción de eliminación en el log de auditoría
        # log_action("delete", {"id": package_id})
        return {"message": "Package deleted"}
