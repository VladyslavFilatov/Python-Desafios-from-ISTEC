import requests
from bs4 import BeautifulSoup

url = 'https://www.tempo.pt/lisboa.htm'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

temp_ = soup.find('span', {'class': 'dato-temperatura changeUnitT'}).get_text().replace('°', '')
dia_ = soup.find('span', {'class': 'cuando'}).get_text().replace('Hoje', 'Hoje ')
local_ = soup.find('h1', {'class': 'titulo'}).get_text()

temp = int(temp_)

if (temp >=0 and temp <=10 ):
    print(f"{dia_} {local_} é {temp}º. Recomendação: utilização de um casaco quente")
elif (temp >=11 and temp <=20 ):
    print(f"{dia_} {local_} é {temp}º. Recomendação: utilização de um casaco leve")
elif (temp >=21 and temp <=30 ):
    print(f"{dia_} {local_} é {temp}º. Recomendação: não é preciso casaco")
else:
    print(f"{dia_} {local_} é {temp}º. Recomendação: melhor ficar em casa e ver o filme")
input()