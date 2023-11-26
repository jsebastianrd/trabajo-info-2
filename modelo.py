import os
import pydicom

class ModeloDicom:
    def __init__(self):
        self.autenticado = False
        self.ruta_actual = None
        self.imagenes_actuales = []
        self.indice_imagen_actual = 0
        self.metadatos_imagen = {}

    def autenticar_usuario(self, usuario, contrasena):
        if usuario == "medicoAnalitico" and contrasena == "bio12345":
            self.autenticado = True
            return True
        else:
            return False

    def cargar_imagenes_desde_carpeta(self, ruta_carpeta):
        try:
            self.ruta_actual = ruta_carpeta
            self.imagenes_actuales = [os.path.join(ruta_carpeta, archivo) for archivo in os.listdir(ruta_carpeta) if archivo.endswith('.dcm')]
            self.indice_imagen_actual = 0
            self.actualizar_metadatos_imagen()
            return True
        except Exception as e:
            print(f"Error al cargar imágenes desde la carpeta: {e}")
            return False

    def actualizar_metadatos_imagen(self):
        if self.indice_imagen_actual < len(self.imagenes_actuales):
            ruta_imagen_actual = self.imagenes_actuales[self.indice_imagen_actual]
            datos_imagen = pydicom.dcmread(ruta_imagen_actual)
            self.metadatos_imagen['Nombre del Paciente'] = datos_imagen.PatientName
            self.metadatos_imagen['Fecha del Estudio'] = datos_imagen.StudyDate
            # Agregar más campos de metadatos según sea necesario

    def obtener_ruta_imagen_actual(self):
        return self.imagenes_actuales[self.indice_imagen_actual]

    def avanzar_a_siguiente_imagen(self):
        if self.indice_imagen_actual < len(self.imagenes_actuales) - 1:
            self.indice_imagen_actual += 1
            self.actualizar_metadatos_imagen()

    def retroceder_a_imagen_anterior(self):
        if self.indice_imagen_actual > 0:
            self.indice_imagen_actual -= 1
            self.actualizar_metadatos_imagen()

