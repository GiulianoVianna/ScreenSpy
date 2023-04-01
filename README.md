# Screen Spy
Espião de Tela.

## Definição da Aplicação
Esta aplicação é um visualizador de tela remoto que permite que você veja o que está sendo exibido em outro computador em tempo real. O código consiste em duas partes: o servidor e o cliente.

O servidor é responsável por capturar a tela do computador em que está sendo executado e enviá-la para o cliente. Ele usa bibliotecas como socket e mss para criar uma conexão com o cliente e enviar a imagem da tela.

O cliente, por outro lado, é responsável por exibir a captura de tela enviada pelo servidor. Ele usa a biblioteca PyQt5 para criar uma interface gráfica de usuário que exibe a imagem da tela capturada. Ele usa o protocolo TCP para se conectar ao servidor e receber a captura de tela.

A aplicação é útil para monitorar o que está sendo exibido em outro computador remotamente, como por exemplo, monitorar o trabalho de alguém ou ver o que está acontecendo em outro lugar.

## Bibliotecas
<ul>
  <li>socket</li>
  <li>threading</li>
  <li>pyautogui</li>
  <li>io</li>
  <li>struct</li>
  <li>PIL</li>
  <li>mss</li>
  <li>sys</li>
  <li>PyQt5</li>
</ul>

### Bibliotecas que precisam ser instaladas:
```bash
pip install socket
pip install pyautogui
pip install pillow
pip install mss
pip install PyQt5
```
## Imagem da Janela do Cliente
![image](https://user-images.githubusercontent.com/101942554/229306845-29b1ded9-ef7c-454c-8ac0-40bd952405f8.png)

## Vídeo
https://user-images.githubusercontent.com/101942554/229306900-974eac23-bd85-4329-abf0-97457ce7c4d4.mp4




