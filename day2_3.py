import requests
from bs4 import BeautifulSoup

from homework3 import set_url

indeed_result = requests.get("https://www.indeed.com/jobs?q=Python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all('a')
spans = []
for page in pages:
    spans.append(page.find("span"))

# print(spans[0:4])

spans = spans[:-1]