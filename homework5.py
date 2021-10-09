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

def answer2():
    try:
        answer_2 = int(input("\nNow choose another country. \n"))
        if 0 < answer_2 < 269:
            print(data[answer_2-1][0])
        elif answer_2 < 1 or answer_2 > 268:
            print("Choose from a number list.")
            answer2()
    except:
        print("This is not a number.")
        answer2()

    return answer_2

def convert():
    from_country = answer()
    to_country = answer2()

    answer_3 = int(input(f"\nHow many {data[from_country-1][1]} do you want to convert to {data[to_country-1][1]}?\n"))

    tw = requests.get(f"https://wise.com/gb/currency-converter/{data[from_country][2]}-to-{data[to_country-1][2]}-rate?amount={answer_3}")
    tw_soup = BeautifulSoup(tw.text, "html.parser")
    converting = float(tw_soup.find('span',{"class":"text-success"}).text)
    result = float(converting*answer_3)
    print(f"{data[from_country-1][1]} {answer_3} is {data[to_country-1][1]} {result}")
    return result

convert()