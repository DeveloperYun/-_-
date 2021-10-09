import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=Python&limit={LIMIT}"

def get_last_page():
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

def extract_job(html):
    title = html.find("div", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class":"company"})

    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None

    location = html.find("div",{"class": "recJobLoc"})["data-rc-loc"] #div의 attribute를 가져옴
    job_id = html["data-jk"]

    return {
        'title': title, 
        'company': company, 
        'location': location,
        "link":f"https://www.indeed.com/viewjob?jk={job_id}"
    }

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        res = requests.get(f"{URL}&start={last_page*LIMIT}")
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})

        #print(results)
        for res in results:
            job = extract_job(res)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs