import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=Python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"pagination"})

    # pagination에서 링크만 모두 찾아줬음 div안에 링크들을 모음
    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]: #마지막 요소는 읽지 않겠다는 뜻
        pages.append(int(link.string)) #string -> integer 변환

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    for page in range(last_page):
        res = requests.get(f"{URL}&start={page*LIMIT}")
        print(res.status_code)