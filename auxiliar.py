# Importação das bibliotecas necessárias
import pyautogui  # Biblioteca para automação de interações com a interface gráfica do usuário
import time  # Biblioteca para manipulação de tempo e atrasos

# Aguarda 5 segundos antes de executar o código
time.sleep(5)

# Imprime a posição atual do cursor do mouse
print(pyautogui.position())
