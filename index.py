from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import openpyxl

fundos = ['hglg11','mxrf11','xpml11','kncr11']
precos = []
driver = webdriver.Chrome()
for fundo in fundos:
    driver.get('https://www.fundsexplorer.com.br/funds/'+fundo)
    time.sleep(1)
    preco = driver.find_element(By.XPATH,"//div[@class='headerTicker__content__price']//p")
    preco = preco.text
    time.sleep(2)
    #pegar texto
    precos.append(preco)
    time.sleep(5)

planilha = openpyxl.load_workbook('Pasta1.xlsx')
guia = planilha['Planilha1']
time.sleep(2)

for i,linhas in enumerate(guia.iter_rows(min_row=2,max_row=5,min_col=3,max_col=3)):
    for linha in linhas:
        linha.value = precos[i]

planilha.save('Pasta1.xlsx')

planilha.close()
    

