# function 정의하기

def say_hello(): #파이썬은 : 들여쓰기로 함수를 표현한다.
    print("hello")

say_hello() #함수 실행

# 함수 인자 전달하기(positional argument : 의존적인 인자)
def say_bye(who):
    print("bye", who)

say_bye("mr_kim")
say_bye(True)
say_bye(33)
say_bye("3")

# 인자 복수개 전달하기
def plus(a,b):
    print(a+b)

def minus(a,b):
    print(a-b)

plus(2,4)
minus(2,4)

# 인자 중 하나에 상수 전달하기..dafault value
def plus2(a,b=2):
    print(a+b)
plus2(2)

def hola(name = "docker1"):
    print("hello", name)

hola()
hola("doctor kim") # 디폴트 값 덮어쓰기 가능