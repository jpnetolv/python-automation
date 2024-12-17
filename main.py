# Importação das bibliotecas necessárias
import time  # Biblioteca para manipulação de tempo e pausas
import pyautogui  # Biblioteca para automação de interações com a interface gráfica do usuário
import pandas  # Biblioteca para manipulação de dados (não está sendo utilizada neste código)

# Definir o tempo de pausa entre as ações do PyAutoGUI
pyautogui.PAUSE = 0.5

# PASSO 1 - ENTRAR NO EMAIL
# Abrir o Google no sistema operacional
pyautogui.press("win")  # Pressiona a tecla "Windows"
pyautogui.write("google")  # Digita "google" na busca do menu iniciar
pyautogui.press("enter")  # Pressiona "Enter" para abrir o navegador

# Entrar na aba de login utilizando um link encurtado
link = "https://l1nk.dev/B3DVu"  # Link encurtado para a página de login
pyautogui.write(link)  # Digita o link na barra de endereço
pyautogui.press("enter")  # Pressiona "Enter" para acessar o link

time.sleep(5)  # Pausa de 5 segundos para garantir que a página carregue

""" 
# PASSO 2 - FAZER LOGIN (comentado para não expor dados pessoais)
# A parte de login foi comentada devido à presença de dados sensíveis, mas segue a lógica abaixo:

# Selecionar a caixa de texto do email
pyautogui.click(x=1095, y=464)  # Clica nas coordenadas da caixa de email

# Escrever o email
email = "email_teste@gmail.com"  # Email fictício
pyautogui.write(email)  # Digita o email na caixa de texto
pyautogui.press("enter")  # Pressiona "Enter"

# Escrever a senha
pyautogui.write("senha_teste")  # Senha fictícia

# Realizar o login
pyautogui.press("enter")  # Pressiona "Enter" para efetuar login

time.sleep(5)  # Pausa para garantir que a página carregue
"""

# PASSO 3 - CLICAR NO BOTÃO ESCREVER
pyautogui.click(x=95, y=217)  # Clica no botão "Escrever" para abrir a tela de composição de e-mail

# PASSO 4 - PREENCHER DESTINATÁRIO
email_desti = "email@email.com"  # Endereço de e-mail fictício do destinatário
pyautogui.write(email_desti)  # Digita o endereço de e-mail do destinatário
pyautogui.press("enter")  # Pressiona "Enter"
pyautogui.press("tab")  # Move para o próximo campo (assunto)
pyautogui.write("Assuntos Pertinentes")  # Escreve o assunto do e-mail
pyautogui.press("tab")  # Move para o próximo campo (corpo da mensagem)

# PASSO 5 - CORPO DA MENSAGEM
# Definindo o conteúdo da mensagem
mensagem = """Bom dia! Esse programa foi feito com a finalidade de automatizar tarefas com Python!
Fico feliz que esteja colaborando com meu aprendizado, participando por meio do recebimento desse e-mail!"""
pyautogui.write(mensagem)  # Escreve a mensagem no corpo do e-mail

# PASSO 6 - ENVIAR MENSAGEM
pyautogui.click(x=1209, y=979)  # Clica no botão de envio para enviar o e-mail
