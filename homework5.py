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


# import os
# import requests
# from bs4 import BeautifulSoup
# from babel.numbers import format_currency

# os.system("clear")


# code_url = "https://www.iban.com/currency-codes"
# currency_url = "https://transferwise.com/gb/currency-converter/"


# countries = []

# codes_request = requests.get(code_url)
# codes_soup = BeautifulSoup(codes_request.text, "html.parser")

# table = codes_soup.find("table")
# rows = table.find_all("tr")[1:]

# for row in rows:
#   items = row.find_all("td")
#   name = items[0].text
#   code =items[2].text
#   if name and code:
#     if name != "No universal currency":
#       country = {
#         'name':name.capitalize(),
#         'code': code
#       }
#       countries.append(country)


# def ask_country(text):
#   print(text)
#   try:
#     choice = int(input("#: "))
#     if choice >= len(countries) or choice < 0:
#       print("Choose a number from the list.")
#       return ask_country(text)
#     else:
#       print(f"{countries[choice]['name']}")
#       return countries[choice]
#   except ValueError:
#     print("That wasn't a number.")
#     return ask_country(text)


# def ask_amount(a_country, b_country):
#   try:
#     print(f"\nHow many {a_country['code']} do you want to convert to {b_country['code']}?")
#     amount = int(input())
#     return amount
#   except ValueError:
#     print("That wasn't a number.")
#     return ask_amount(a_country, b_country)
  
# ask_country(text) 함수 (Line 34 ~ 46)
# 지난 시간에 완성했던 ask() 함수와 거의 비슷하나 43번째 줄에서 countries[choice] 값을 리턴해주는 부분이 추가되었습니다.
# user_country, target_country 값 구하기 (Line 64 ~ 65)
# ask_country(text) 함수를 불러와 사용자가 고른 나라의 이름과 통화 코드를 저장 시켜줍니다.
# user_country, target_country 모두 같은 방식으로 동작합니다.
# amount 값 구하기 (Line 68)
# 사용자가 얼마만큼의 돈을 환전할지 알아내야 합니다.
# 그러기 위해선 ask_amount 함수를 작성하여 인자 값으로 user_country, target_country 를 보내야합니다.
# ask_amount(a_country, b_country) 함수 (Line 49 ~ 56)
# 사용자가 선택한 두 나라의 정보를 인자 값으로 받아왔습니다.
# 두 나라의 정보는 오로지 사용자에게 질문을 던지는 출력문에만 쓰입니다.
# amount = int(input()) 을 사용하여 사용자에게 환전할 돈의 양을 묻습니다.
# 돈은 숫자이므로 반드시 int() 로 감싸서 형변환 시켜줍니다.
# 그리고 amount 값을 리턴 시켜줍니다.
# 사용자가 만약 숫자가 아닌 문자를 입력했을 경우를 대비하여 try-except문을 사용하여 예외처리를 해줍니다.
# 사용자가 선택한 두 나라의 통화 코드(from_code, to_code) 가져오기 (Line 70 ~ 71)
# 2번에서 구한 user_country, target_country 값을 이용하여 간단히 통화 코드를 가져올 수 있습니다.
# 각각의 새로운 변수에 user_country['code'] , target_country['code'] 를 넣어주시면 오로지 통화 코드만 저장되는 것을 볼 수 있습니다.
# 홈페이지에서 환전 결과를 가져오기 (Line 73 ~ 80)
# 스크래핑을 하기에 앞서, requests 라이브러리를 이용하여 Transfer Wise 홈페이지에 HTTP 요청을 보내야합니다.
# 사용자로부터 입력을 받은 정보들을 URL에 포맷팅하여 GET 방식으로 HTTP 요청을 아래와 같은 코드로 보냅니다.
# currency_request = requests.get(f"{currency_url}{from_code}-to-{to_code}-rate?amount={amount}")
# beautifulSoup 라이브러리를 사용하여 해당 홈페이지의 html 코드들을 가져옵니다.
# 위의 사진은 환전 결과 값을 가져오기 위해 크롬 개발자 도구에서 inspect한 결과입니다.
# 홈페이지의 코드 변경으로 인해 환전 결과의 value 값을 가져올 수 없습니다.
# 그러므로 환전 결과 값을 가져오는 것이 아니라 다른 방법으로 접근하여야 됩니다.
# 홈페이지 하단에 보시면 1 COP = 0.30937 KRW 이라는 값이 있는데 초록색 글씨로 되어있는 0.30937 을 긁어와서 amount 값이랑 곱해주는 것으로 환전 결과 값을 얻을 수 있습니다.
# 저 초록색 값을 가져오기 위해 rate = currency_soup.find("span", {"class":"text-success"}).get_text() 이라는 코드를 작성해줍니다.
# 혹시 rate 값이 존재하지 않을 경우도 생각하여 if rate: 를 사용하여 rate 값이 존재할 때만 환전 값을 구하도록 코드를 작성합니다.
# 위에서 구한 rate 값을 float 형식으로 변환한 다음 amount 값이랑 곱하여 환전 값을 구하기 위해 아래와 같이 작성합니다.
# result = float(rate) * amount
# 마지막으로 환전할 돈의 양(amount) , 환전 결과(result) 를 format_currency() 를 이용하여 통화 형식으로 포맷 시켜줍니다.