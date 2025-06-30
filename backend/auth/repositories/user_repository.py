class UserRepository:
    def __init__(self, db):
        self.db = db

    def find_by_email(self, email):
        with self.db.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            return cursor.fetchone()

    def create_user(self, email, hashed_password):
        with self.db.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (email, password) VALUES (%s, %s)",
                (email, hashed_password)
            )
        self.db.commit()
