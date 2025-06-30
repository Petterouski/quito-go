from domain.entities.package import Package
from domain.interfaces.package_repository import PackageRepository

class MySQLPackageDAO(PackageRepository):
    def __init__(self, db):
        self.db = db

    def create(self, package: Package):
        cursor = self.db.cursor()
        sql = self._insert_sql()
        values = (package.destination, package.duration_days, package.price, package.capacity)
        cursor.execute(sql, values)
        self.db.commit()

    def list_all(self):
        cursor = self.db.cursor()
        sql = self._select_all_sql()
        cursor.execute(sql)
        return cursor.fetchall()

    def update(self, package: Package):
        cursor = self.db.cursor()
        sql = self._update_sql()
        values = (package.destination, package.duration_days, package.price, package.capacity, package.id)
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, package_id: int):
        cursor = self.db.cursor()
        sql = self._delete_sql()
        cursor.execute(sql, (package_id,))
        self.db.commit()

    # ------------------------------
    # Métodos privados con SQL
    # ------------------------------

    def _insert_sql(self):
        return """
        INSERT INTO packages (destination, duration_days, price, capacity)
        VALUES (%s, %s, %s, %s)
        """

    def _select_all_sql(self):
        return "SELECT * FROM packages"

    def _update_sql(self):
        return """
        UPDATE packages
        SET destination=%s, duration_days=%s, price=%s, capacity=%s
        WHERE id=%s
        """

    def _delete_sql(self):
        return "DELETE FROM packages WHERE id = %s"
