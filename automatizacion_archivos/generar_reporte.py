import os
from datetime import datetime


class ReporteArchivosTxt:
    """
    Esta clase permite generar un reporte con la cantidad de lineas que tiene cada archivo .txt
    en la carpeta donde se encuentra el script
    """

    def __init__(self, carpeta_base=None):
        """
        Inicializa la calse, definiendo rutas clave como:
        - Carpeta base donde buscar los archivos .txt
        - Carpeta donde se guardan los reportes
        - Nombre del archivo de reporte con fecha actual

        """
        self.carpeta_base = carpeta_base or os.path.dirname(os.path.abspath(__file__))
        self.carpeta_reportes = os.path.join(self.carpeta_base, "reportes")
        self.fecha_hoy = datetime.now().strftime("%Y%m%d")
        self.archivo_salida = os.path.join(
            self.carpeta_reportes, f"reporte_{self.fecha_hoy}.txt"
        )

    def contar_lineas(self, ruta_archivo):
        """
        Esta funcion esla que permite contar el numero de lineas que tiene un archivo de texto.
        Si ocurre un error al leer el archivo, retorna un mensaje con el error.

        """
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                return sum(1 for _ in f)
        except Exception as e:
            return f"Error leyendo el archivo: {e}"

    def obtener_archivos_txt(self):
        """
        Retorna una lista con los nombres de todos los archivos que tienen extensión .txt,
        sin importar si están en mayúsculas o minúsculas (por ejemplo: .txt, .TXT, .Txt, etc.).
        Solo se consideran archivos ubicados directamente en la carpeta base del script.
        """
        return [f for f in os.listdir(self.carpeta_base) if f.lower().endswith(".txt")]

    def crear_directorio_reportes(self):
        """
        Crea la carpeta 'reportes' si no existe.
        Allí se almacenarán los archivos de salida generados por el script.
        """
        os.makedirs(self.carpeta_reportes, exist_ok=True)

    def generar(self):
        """
        Método principal que genera el reporte:
        - Busca los archivos .txt
        - Cuenta las líneas de cada uno
        - Escribe la información en un archivo .txt dentro de la carpeta 'reportes'
        """
        self.crear_directorio_reportes()
        archivos_txt = self.obtener_archivos_txt()

        with open(self.archivo_salida, "w", encoding="utf-8") as reporte:
            if archivos_txt:
                for archivo in archivos_txt:
                    ruta = os.path.join(self.carpeta_base, archivo)
                    num_lineas = self.contar_lineas(ruta)
                    reporte.write(f"{archivo}: {num_lineas} líneas\n")
                reporte.write(f"\nTotal de archivos procesados: {len(archivos_txt)}\n")
            else:
                reporte.write("No se encontraron archivos de texto.\n")

        # Confirmación visual por consola
        print(f"Reporte generado: {self.archivo_salida}")


# Punto de entrada del script cuando se ejecuta directamente
if __name__ == "__main__":
    reporte = ReporteArchivosTxt()
    reporte.generar()
