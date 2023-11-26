from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QSlider
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class VistaDicom(QWidget):
    def __init__(self):
        super().__init__()

        self.modelo = None

        self.layout_login()
        self.layout_visualizador_imagen()

        self.setWindowTitle("Visor Dicom")
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def layout_login(self):
        self.etiqueta_usuario = QLabel("Usuario:")
        self.entrada_usuario = QLineEdit(self)
        self.etiqueta_contrasena = QLabel("Contraseña:")
        self.entrada_contrasena = QLineEdit(self)
        self.boton_login = QPushButton("Login", self)

        layout_login = QVBoxLayout()
        layout_login.addWidget(self.etiqueta_usuario)
        layout_login.addWidget(self.entrada_usuario)
        layout_login.addWidget(self.etiqueta_contrasena)
        layout_login.addWidget(self.entrada_contrasena)
        layout_login.addWidget(self.boton_login)

        self.setLayout(layout_login)

    def layout_visualizador_imagen(self):
        self.etiqueta_imagen = QLabel(self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.boton_siguiente = QPushButton("Siguiente", self)
        self.boton_anterior = QPushButton("Anterior", self)

        layout_visualizador = QVBoxLayout()
        layout_visualizador.addWidget(self.etiqueta_imagen)
        layout_visualizador.addWidget(self.slider)
        layout_visualizador.addWidget(self.boton_siguiente)
        layout_visualizador.addWidget(self.boton_anterior)

        self.setLayout(layout_visualizador)

    def actualizar_etiqueta_imagen(self, ruta_imagen):
        pixmap = QPixmap(ruta_imagen)
        self.etiqueta_imagen.setPixmap(pixmap)
        self.etiqueta_imagen.show()

    def conectar_eventos(self, controlador):
        self.boton_login.clicked.connect(controlador.boton_login_clickeado)
        self.boton_siguiente.clicked.connect(controlador.boton_siguiente_clickeado)
        self.boton_anterior.clicked.connect(controlador.boton_anterior_clickeado)
        self.slider.valueChanged.connect(controlador.slider_valor_cambiado)
