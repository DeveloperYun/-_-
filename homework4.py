import requests
from bs4 import BeautifulSoup

print("Hello, please choose select a country by number:")

result = requests.get("https://www.iban.com/currency-codes")
soup = BeautifulSoup(result.text, "html.parser")
tr = soup.find_all('tr')
tds = soup.find_all('td')

data = []

for tr in soup.find_all('tr'):
    tds = list(tr.find_all('td'))
    if tr.find_all('td'):
        country = tds[0].text
        currency = tds[1].text
        code = tds[2].text
        number = tds[3].text
        data.append([country,currency,code,number])

for i in range(len(data)):
    print(f"# {i+1}", data[i][0])
    i+=1

def answer():
    try:
        answer_1 = int(input("Where are you from? Choose a country by number.\n #:"))
        if 0 < answer_1 < 269:
            print(data[answer_1-1][0])
        elif answer_1 <1 or answer_1>268:
            print("Choose from a number list.")
            answer()
    except:
        print("This is not a number.")
        answer()

    return answer_1

answer()