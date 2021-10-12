from flask import Flask #웹 어플리케이션 만드는 프레임 워크 flask

#앱을 만들기 위한 코드
app = Flask("SuperScrapper")

# @ = decorator...바로 아래에 있는 "함수"를 찾아서 decorate 해준다.
#  / 로 접속요청 시 파이썬 함수를 실행하도록 구축
@app.route("/")
def home():
    return "Hello! welcome to my house"

# url 끝에 /contact 를 붙여서 접속하면 아래 함수 실행
@app.route("/contact")
def home2():
    return "Hello! nice contact"


    
#repl.it 에서 구동하는 서버
app.run(host="0.0.0.0")

