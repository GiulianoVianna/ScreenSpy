import socket
import threading
import pyautogui
import io
import struct
from PIL import Image
from mss import mss

# Função para tratar cada cliente conectado
def tratar_cliente(conexao, endereco):
    print(f"Nova conexão estabelecida: {endereco}")
    try:
        # Usar a biblioteca mss para capturar a tela
        with mss() as sct:
            while True:
                tela = sct.grab(sct.monitors[0])
                imagem = Image.frombytes("RGB", tela.size, tela.bgra, "raw", "BGRX")
                
                # Redimensionar a imagem no servidor
                imagem_redimensionada = imagem.resize((800, 400), Image.ANTIALIAS)
                buffer = io.BytesIO()
                imagem_redimensionada.save(buffer, format="JPEG", quality=200)
                
                bytes_tela = buffer.getvalue()

                # Enviar o tamanho da imagem em bytes
                conexao.sendall(struct.pack(">I", len(bytes_tela)))
                # Enviar a imagem em si
                conexao.sendall(bytes_tela)

                # Aguardar um momento para não sobrecarregar o servidor
                pyautogui.time.sleep(0.1)

    except Exception as erro:
        print(f"Conexão encerrada: {endereco}, Erro: {erro}")
    finally:
        conexao.close()

# Função principal do programa
def main():
    # Criar um socket
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Vincular o endereço IP e a porta
    servidor.bind(('192.168.0.123', 12345))
    # Escutar por novas conexões
    servidor.listen(5)
    print("Servidor iniciado...")

    while True:
        # Aceitar uma nova conexão
        conexao, endereco = servidor.accept()
        # Criar uma nova thread para tratar o cliente
        thread = threading.Thread(target=tratar_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    main()
