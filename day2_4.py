import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=Python&limit=50")

#페이지에 쓸 soup를 제작..페이지가 총 몇개인지 보기 위해서
#soup는 특정 데이터를 찾아주는 오브젝트
#html코드상에서 soup를 이용해서 데이터 탐색 및 추출이 가능함
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

#indeed soup에서 찾은걸 담아서 div를 찾은뒤 class명이 pagination인 요소를
#반환했음
#indeep_soup는 html을 통으로 긁어온 것..그걸 다듬어 div만 가져온것임
pagination = indeed_soup.find("div", {"class":"pagination"})

# pagination에서 링크만 모두 찾아줬음 div안에 링크들을 모음
links = pagination.find_all('a')
pages = []

# 이렇게 걸러낸 리스트 안에 d또 span이 있으므로 이를 리스트에 담아 추출.
for link in links[:-1]: #마지막 요소는 읽지 않겠다는 뜻
    #pages.append(link.find("span").string) # string만 가져오길 원함
    pages.append(int(link.string)) #string -> integer 변환

# print(spans[0:4])

#pages = pages[0:-1] # 파이썬의 배열에 음수..끝에서부터란 뜻
max_page = pages[-1]
print(max_page)

