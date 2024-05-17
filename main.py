import time
import pyautogui
import pandas 
pyautogui.PAUSE = 0.5

# PASSO 1 - ENTRAR NO EMAIL
# abrir o google
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")

#entrar na aba de login
link = "https://l1nk.dev/B3DVu" # com encurtador de link
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5) # pausa para abrir a página

""" # PASSO 2 - FAZER LOGIN
# devido conter informações pessoais, irei codificar a forma adequada de fazer o procedimento em forma de comentário, com dados fictícios

"# selecionar a caixa de texto
pyautogui.click(x=1095, y=464)

# escrever email
email = "email_teste@gmail.com"
pyautogui.write(email)
pyautogui.press("enter")

# escrever senha
pyautogui.write("senha_teste")

# realizar login
pyautogui.press("enter")

time.sleep(5) #pausa para abrir a página """

# PASSO 3 - CLICAR NO BOTÃO ESCREVER
pyautogui.click(x=95, y=217)

# PASSO 4 - PREENCHER DESTINATÁRIO
email_desti = "email@email.com"
pyautogui.write(email_desti)
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.write("Assuntos Pertinentes")
pyautogui.press("tab")

# PASSO 5 - CORPO DA MENSAGEM 
# a mensagem pode ser implementada de forma diferente, até mesmo realizando o envio de um arquivo.
mensagem = """Bom dia! Esse programa foi feito com a finalidade de automatizar tarefas com Python!
Fico feliz que esteja colaborando com meu aprendizado, partincipando por meio do recebimento desse email!"""
pyautogui.write(mensagem)

# PASSO 6 - ENVIAR MENSAGEM
pyautogui.click(x=1209, y=979)