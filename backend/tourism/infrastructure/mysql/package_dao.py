def create(self, package: Package):
    # Inserta un nuevo paquete en la base de datos
    cursor = self.db.cursor()
    sql = self._insert_sql()  # Obtiene la sentencia SQL de inserción
    # Define los valores a insertar: destino, duración, precio y capacidad
    values = (package.destination, package.duration_days, package.price, package.capacity)
    cursor.execute(sql, values)  # Ejecuta la consulta con los valores
    self.db.commit()  # Confirma la transacción

def list_all(self):
    # Lista todos los paquetes almacenados
    cursor = self.db.cursor()
    sql = self._select_all_sql()  # Consulta SQL para obtener todos los registros
    cursor.execute(sql)
    return cursor.fetchall()  # Retorna todos los registros encontrados

def update(self, package: Package):
    # Actualiza los datos de un paquete existente
    cursor = self.db.cursor()
    sql = self._update_sql()  # Consulta SQL para actualizar
    # Define los valores a actualizar y el id del paquete
    values = (package.destination, package.duration_days, package.price, package.capacity, package.id)
    cursor.execute(sql, values)
    self.db.commit()  # Confirma los cambios

def delete(self, package_id: int):
    # Elimina un paquete por su ID
    cursor = self.db.cursor()
    sql = self._delete_sql()  # Consulta SQL para eliminar
    cursor.execute(sql, (package_id,))  # Ejecuta la eliminación
    self.db.commit()  # Confirma la eliminación

# ------------------------------
# Métodos privados que devuelven las sentencias SQL
# ------------------------------

def _insert_sql(self):
    # Sentencia SQL para insertar un paquete
    return """
    INSERT INTO packages (destination, duration_days, price, capacity)
    VALUES (%s, %s, %s, %s)
    """

def _select_all_sql(self):
    # Sentencia SQL para seleccionar todos los paquetes
    return "SELECT * FROM packages"

def _update_sql(self):
    # Sentencia SQL para actualizar un paquete existente
    return """
    UPDATE packages
    SET destination=%s, duration_days=%s, price=%s, capacity=%s
    WHERE id=%s
    """

def _delete_sql(self):
    # Sentencia SQL para eliminar un paquete por ID
    return "DELETE FROM packages WHERE id = %s"
