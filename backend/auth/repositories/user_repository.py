class UserRepository:
    """
    Repositorio de usuarios responsable de manejar las operaciones relacionadas con la base de datos
    para la entidad User, como buscar y crear usuarios.
    """

    def __init__(self, db):
        """
        Inicializa el repositorio con una conexión a la base de datos.

        Args:
            db: Objeto de conexión a la base de datos que soporta el método cursor().
        """
        self.db = db

    def find_by_email(self, email):
        """
        Busca un usuario en la base de datos por su dirección de correo electrónico.

        Args:
            email (str): La dirección de correo electrónico del usuario a buscar.

        Returns:
            dict o None: Un diccionario con los datos del usuario si se encuentra, o None si no.
        """
        # Abre un cursor para realizar operaciones en la base de datos
        with self.db.cursor() as cursor:
            # Ejecuta una consulta SQL parametrizada para evitar inyección SQL
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            # Obtiene el primer resultado de la consulta
            user_record = cursor.fetchone()
            return user_record

    def create_user(self, email, hashed_password):
        """
        Crea un nuevo usuario en la base de datos con el email y la contraseña cifrada.

        Args:
            email (str): La dirección de correo electrónico del nuevo usuario.
            hashed_password (str): La contraseña cifrada del usuario.

        Nota:
            Después de realizar la inserción, se confirma la transacción con self.db.commit().
        """
        # Abre un cursor para realizar operaciones en la base de datos
        with self.db.cursor() as cursor:
            # Ejecuta una sentencia SQL parametrizada para insertar el nuevo usuario
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (%s, %s)",
                (email, hashed_password)
            )
        # Confirma los cambios en la base de datos
        self.db.commit()
