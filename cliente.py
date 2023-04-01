import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QTimer
import socket
import struct
from PIL import Image
import io

# Classe para o cliente
class Cliente(QWidget):
    def __init__(self):
        super().__init__()

        self.inicializar_interface()

        # Criar um socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conectar ao endereço IP e porta especificados
        self.socket.connect(('192.168.0.123', 12345))

        # Criar um timer para atualizar a captura de tela
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_captura_tela)
        self.timer.start(100)

    def inicializar_interface(self):
        # Configurar a posição, tamanho e título da janela
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Screen SPY - Visualizador de Tela')

        # Criar uma QLabel para exibir a captura de tela
        self.label = QLabel(self)
        self.label.setScaledContents(True)  # Adiciona o redimensionamento suave à QLabel
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)


    def atualizar_captura_tela(self):
        try:
            # Receber o tamanho da imagem em bytes
            tamanho = struct.unpack(">I", self.socket.recv(4))[0]

            dados = b''
            while len(dados) < tamanho:
                dados_recebidos = self.socket.recv(min(tamanho - len(dados), 4096))
                if not dados_recebidos:
                    break
                dados += dados_recebidos

            if len(dados) != tamanho:
                print("Dados incompletos recebidos")
                return

            imagem = Image.open(io.BytesIO(dados))

            qimage = QImage(imagem.tobytes("raw", "RGB"), imagem.size[0], imagem.size[1], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)

            # Remova a linha que redimensiona a imagem usando QPixmap
            # pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio)

            self.label.setPixmap(pixmap)

        except Exception as e:
            print(f"Erro ao atualizar a captura de tela: {e}")
            self.timer.stop()
            self.socket.close()

def main():
    app = QApplication(sys.argv)
    cliente = Cliente()
    cliente.show()
    cliente.setFixedSize(800,400)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()  