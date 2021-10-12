from flask import Flask #웹 어플리케이션 만드는 프레임 워크 flask
from flask import render_template, request

#앱을 만들기 위한 코드
app = Flask("SuperScrapper")

# @ = decorator...바로 아래에 있는 "함수"를 찾아서 decorate 해준다.
#  / 로 접속요청 시 파이썬 함수를 실행하도록 구축
# @app.route("/")
# def home():
#     return "Hello! welcome to my house"

# dynamic urls 사용 법
# <> 를 placeholder 라고 한다.
# 이렇게 쓸 경우 flask는 home2 함수를 username 인자와 함께 호출하려한다.
# @app.route("/<username>")
# def home2(username):
#     return f"Hello! your name is {username} "
      # 이런 dynamic urls 는 예를들어 instagram/developerYun 이렇게 입력하면
      # DB에서 username을 찾아서 결과를 띄워주는 방식이다.


# html을 보여줄 수도 있다.
# html 파일을 받아오기 위해서는 render_template를 import 해야한다.
@app.route("/")
def home3():
    return render_template("home3.html")

# 함수에 인자는 없지만, 사용자가 찾으려고 하는 단어는 가져오고싶다.
# 따라서 requests를 import한다. 데이터를 웹사이트에 보내느것도 가져오는것도 requests
@app.route("/report")
def report():
    #name='word'의 arguments를 request가 뽑아온다.
    word = request.args.get('word')
    #flask가 html 파일을 쭉 보고 있다가
    # 변수들을 쭉 보고, 변수를 {{}} 안에 넣어줘서 사용자에게 보여준다.
    # 이를 rendering 이라고 한다.
    return render_template("report.html", searchingBy=word)
     
#repl.it 에서 구동하는 서버
app.run(host='0.0.0.0')

