from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('/Users/vladyslavfilatov/PycharmProjects/python_desafio_web_scrapper/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://tempo.sapo.pt/Lisboa")

weather = driver.find_element(By.XPATH, '//*[@id="home"]/div/main-forecast/section/div/div[1]/div/div/div[1]/widget/div/div[2]/ul/li[1]/div[2]/div[1]/div[1]/span[1]')
dia = driver.find_element(By.XPATH, '//*[@id="home"]/div/main-forecast/section/div/div[1]/div/div/div[1]/widget/div/div[2]/ul/li[1]/div[1]/span[2]')
local = driver.find_element(By.XPATH, '//*[@id="home"]/div/main-forecast/section/div/div[1]/div/div/div[1]/widget/div/div[1]/div[1]')

temp_ = weather.text.replace('º', '')
temp = int(temp_)

if (temp >=0 and temp <=10 ):
    print(f"Hoje {dia.text} em {local.text} {temp}º. Recomendação: utilização de um casaco quente")
elif (temp >=11 and temp <=20 ):
    print(f"Hoje {dia.text} em {local.text} {temp}º. Recomendação: utilização de um casaco leve")
elif (temp >=21 and temp <=30 ):
    print(f"Hoje {dia.text} em {local.text} {temp}º. Recomendação: não é preciso casaco")
else:
    print(f"Hoje {dia.text} em {local.text} {temp}º. Recomendação: melhor ficar em casa e ver o filme")
input()