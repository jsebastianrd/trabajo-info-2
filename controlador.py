# por jaun sebastian rivillas y 
from PyQt5.QtWidgets import QFileDialog
import os
import rarfile
from PyQt5.QtWidgets import QApplication
import sys
from vista import VistaDicom
from modelo import ModeloDicom

class ControladorDicom:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        self.vista.modelo = self.modelo
        self.vista.conectar_eventos(self)

    def boton_login_clickeado(self):
        usuario = self.vista.entrada_usuario.text()
        contrasena = self.vista.entrada_contrasena.text()

        if self.modelo.autenticar_usuario(usuario, contrasena):
            ruta_archivo_rar = QFileDialog.getOpenFileName(None, 'Seleccionar Archivo RAR con Imágenes Dicom', '', 'RAR files (*.rar)')[0]
            if ruta_archivo_rar:
                ruta_carpeta_destino = self.descomprimir_archivo_rar(ruta_archivo_rar)
                if ruta_carpeta_destino:
                    if self.modelo.cargar_imagenes_desde_carpeta(ruta_carpeta_destino):
                        self.vista.layout_login().hide()
                        self.vista.layout_visualizador_imagen().show()
                        self.mostrar_imagen_actual()
                    else:
                        # Manejar error
                        pass
                else:
                    # Manejar error de descompresión
                    pass
            else:
                # El usuario canceló la selección del archivo RAR
                pass
        else:
            # Manejar error de autenticación
            pass

    def descomprimir_archivo_rar(self, ruta_archivo_rar):
        try:
            with rarfile.RarFile(ruta_archivo_rar, 'r') as archivo_rar:
                # Puedes especificar la carpeta de destino, por ejemplo, la carpeta actual
                carpeta_destino = os.path.join(os.getcwd(), 'imagenes_dicom')
                archivo_rar.extractall(carpeta_destino)
                return carpeta_destino
        except Exception as e:
            print(f"Error al descomprimir el archivo RAR: {e}")
            return None

    def boton_siguiente_clickeado(self):
        self.modelo.avanzar_a_siguiente_imagen()
        self.mostrar_imagen_actual()

    def boton_anterior_clickeado(self):
        self.modelo.retroceder_a_imagen_anterior()
        self.mostrar_imagen_actual()

    def slider_valor_cambiado(self):
        valor = self.vista.slider.value()
        # Manejar el cambio de valor


if __name__ == '__main__':
    app = QApplication(sys.argv)
    modelo = ModeloDicom()
    vista = VistaDicom()
    controlador = ControladorDicom(modelo, vista)
    vista.show()
    sys.exit(app.exec_())