import psycopg2
from datetime import datetime, timedelta


class GestorUsuariosDB:
    def __init__(
        self,
        dbname="prueba_db_gopass",
        user="gopass",
        password="gopass",
        host="localhost",
        port="5432",
    ):
        """
        Inicializa la conexión a la base de datos PostgreSQL.
        """
        self.conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.cur = self.conn.cursor()

    def insertar_usuario(self, nombre, correo):
        """
        Inserta un nuevo usuario solo si el correo no existe aún en la base de datos.
        """
        self.cur.execute("SELECT COUNT(*) FROM usuarios WHERE correo = %s", (correo,))
        if self.cur.fetchone()[0] > 0:
            print(f"[INFO] El usuario con correo '{correo}' ya existe. No se insertó.")
            return

        self.cur.execute(
            "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)", (nombre, correo)
        )
        self.conn.commit()
        print(f"[OK] Usuario '{nombre}' insertado.")

    def obtener_usuarios_recientes(self, dias=7):
        """
        Retorna los usuarios registrados en los últimos 'dias' días.
        """
        self.cur.execute(
            """
            SELECT id, nombre, correo, fecha_registro
            FROM usuarios
            WHERE fecha_registro >= %s
            """,
            (datetime.now() - timedelta(days=dias),),
        )
        return self.cur.fetchall()

    def cerrar_conexion(self):
        """
        Cierra cursor y conexión a la base de datos.
        """
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    db = GestorUsuariosDB()

    # Inserción segura (no se repite si ya existe el correo)
    db.insertar_usuario("Andres Muñoz", "aemunoz@gopass.com")

    # Consulta de usuarios recientes
    print("\n Usuarios registrados en los últimos 7 días:\n")
    print(f"{'ID':<4} {'Nombre':<35} {'Correo':<30} {'Fecha registro'}")
    print("-" * 90)

    for u in db.obtener_usuarios_recientes():
        print(f"{u[0]:<4} {u[1]:<35} {u[2]:<30} {u[3]}")

    db.cerrar_conexion()
