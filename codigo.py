# passo a passo do projeto

# Passo 1: acessar o sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
    
import pyautogui as pyp
import time

pyp.PAUSE = 0.88

# abrir o navegador

pyp.press("win")
pyp.write("chrome")
pyp.press("Enter")


# entrar no site

# pyp.click(x=197, y=62)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyp.write(link)
pyp.press("Enter")

# esperar um tempo após abrir para carre
time.sleep(3)

# Passo 2: fazer login
pyp.click(x=600, y=377)
pyp.write("pythonimpressionador@gmail.com")

# escrever a senha
pyp.press("tab")
pyp.write("sua07senha")

# logar
pyp.click(x=666, y=544)
time.sleep(3)


# Passo 3: importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: cadastrar um produto
# cadastrar cada linha da tabela 
for linha in tabela.index:
    # clicar no 1º campo
    pyp.click(x=549, y=254)
    # código
    pyp.write(tabela.loc[linha,"codigo"])
    pyp.press("tab")
    # marca
    pyp.write(tabela.loc[linha,"marca"])
    pyp.press("tab")
    # tipo
    pyp.write(tabela.loc[linha,"tipo"])
    pyp.press("tab")
    # categoria
    pyp.write(str(tabela.loc[linha,"categoria"]))
    pyp.press("tab")
    # preço
    pyp.write(str(tabela.loc[linha,"preco_unitario"]))
    pyp.press("tab")
    # custo
    pyp.write(str(tabela.loc[linha,"custo"]))
    pyp.press("tab")
    # obs
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyp.write(obs)
    pyp.press("tab")
    # enviar
    pyp.press("Enter")
    # pyp.scroll(5100)
# Passo 5: repetir o processo de cadastro até acabar
    pyp.scroll(5100)

# pyautogui.click --> clicar em algum lugar da tela 
# pyautogui.write --> escrever um texto
# pyautogui.press --> pressionar 1 tecla do teclado 