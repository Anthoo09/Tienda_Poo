import os
import tempfile

class ArchivoTemporal:
    def __init__(self, contenido):
        """
        Constructor de la clase.
        Se ejecuta automáticamente al crear una instancia del objeto.
        Aquí se crea un archivo temporal y se escribe contenido en él.
        """
        self.nombre_archivo = tempfile.mktemp(suffix=".txt")
        self.archivo = open(self.nombre_archivo, "w")
        self.archivo.write(contenido)
        self.archivo.flush()
        print(f"[INIT] Archivo temporal creado: {self.nombre_archivo}")

    def leer_contenido(self):
        """
        Método para leer el contenido del archivo.
        """
        self.archivo.close()  # Cerramos para poder leer de nuevo desde el principio
        with open(self.nombre_archivo, "r") as f:
            return f.read()

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente cuando el objeto es eliminado o el programa finaliza.
        Aquí cerramos el archivo y lo eliminamos del sistema.
        """
        try:
            self.archivo.close()
            os.remove(self.nombre_archivo)
            print(f"[DEL] Archivo temporal eliminado: {self.nombre_archivo}")
        except Exception as e:
            print(f"[ERROR] No se pudo eliminar el archivo: {e}")

# --- Ejecución del Programa ---

if __name__ == "__main__":
    # Crear un objeto de tipo ArchivoTemporal
    archivo = ArchivoTemporal("Este es un contenido de prueba.")

    # Leer el contenido del archivo temporal
    contenido = archivo.leer_contenido()
    print(f"Contenido leído: {contenido}")

    # Eliminar manualmente el objeto (opcional, para activar el destructor)
    del archivo

    # Nota: el destructor también se llamará automáticamente al finalizar el programa si no se hace 'del' explícitamente.
