from domain.dto.package_dto import PackageDTO
from domain.entities.package import Package
from infrastructure.mongo.audit_logger import log_action

class PackageService:
    def __init__(self, factory):
        self.package_dao = factory.create_package_dao()

    def create_package(self, dto: PackageDTO):
        package = Package(**dto.model_dump())
        self.package_dao.create(package)

    def list_packages(self):
        return self.package_dao.list_all()

    def update_package(self, package_id: int, dto: PackageDTO):
        package = Package(id=package_id, **dto.model_dump(exclude_unset=True))
        self.package_dao.update(package)
        return {"message": "Package updated"}

    def delete_package(self, package_id: int):
        self.package_dao.delete(package_id)
        return {"message": "Package deleted"}
