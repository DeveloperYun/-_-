#파이썬의 변수 개념
#변수에 저장할 수 있는 자료형

#1. 숫자,ㅇ
num1 = 2
num2 = 3
float1 = 3.233

#1++ 숫자도 정수형,실수형 등 타입이 다양
print(type(num1));
print(type(float1));

#2. 문자열은 따옴표나 쌍따옴표로 쌓여야한다.(형식일치)(string)
a_string = "abcd"

#3. boolean
a = True #true = 1
b = False #false = 0  문자열처럼 따옴표를 쓰지 않는다. 대소문자 구분 주의

#4. None (파이썬에만 존재, js의 null과 비슷)
none1 = None
print(type(none1))  #class 'NoneType'...존재하지 않는다는 의미. 그냥 "없다" 는 뜻
