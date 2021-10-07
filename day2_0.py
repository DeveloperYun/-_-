# web scrapping 실습..웹상의 데이터 추출하기
# url 로부터 제목과 상단 첫 이미지를 가져와서 보여준다.
# 원하는 정보를 자유롭게 추출해올 수 있다.

# 스택오버플로우와 indeed에서 가져온 구직 정보를 리스트해서 엑셀로 정리한다.

# 요청을 만드는 기능을 모아둔 모듈
import requests

indeed_resul = requests.get("https://www.indeed.com/jobs?q=Python&limit=50")

print(indeed_resul.text) # html의 모든 text 내용을 가져왔다.

# html에서 정보를 추출하기에 유용한 BeautifulSoup 패키지