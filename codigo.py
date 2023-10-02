# AUTOMAÇÂO DE TAREFAS COM PYTHON#

#Passo 01: Entrar no sistema da empresa
#Passo 02: Fazer login
#Passo 03: Cadastrar 01 produto
#Passo 04: Repetir o cadastro para todos os produtos 

#BIBLIOTECAS UTILIZADAS
import pyautogui # pip install pyautogui para (instalar o pyautogui)
import time
import pandas as pd #pip install pandas numpy openpyx1

# pyautogui.click -> Clicar com o mouse
# pyautogui.write -> Escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho (Combinação de teclas)

#Passo 01: Entrar no sistema da empresa

    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
pyautogui.PAUSE = 0.5

    # Abrir o Chrome
    # precisei utilizar o chrome no modo anônimo pois fora dele o site da hastag não funciona ????

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1903, y=55)
pyautogui.click(x=1669, y=126)

    #Entrar no link

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

    #esperar o site carregar

time.sleep(3)

#Passo 02: Fazer login

pyautogui.click(x=991, y=394)
pyautogui.write("origomqatester@gmail.com")

pyautogui.click(x=1005, y=494)
pyautogui.write("origomqatester@gmail.com")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

    # Apenas para testar o Pandas
tabela = pd.read_csv(r'C:/Users/rodri/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.11/Python/Python PowerUp/Automacao de Tarefas com Python/produtos.csv')
#print(tabela)

for linha in tabela.index:

#Passo 04: Cadastrar 01 produto

    pyautogui.click(x=834, y=279)

    # Modo 01
    # a busca na tabela pode ser atribuida em variaveis
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]
        
    #Modo 02
    # ou adicionar a busca no próprio comando de preenchimento do pyautogui 
    
    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"] 
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    # apertar para enviar
#Passo 05: Repetir o cadastro para todos os produtos 
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)



