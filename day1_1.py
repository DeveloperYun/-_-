# sequence type : 열거형
# 파이썬 standard library 를 애용

# 1. 열거형 타입 : 리스트
days = ["mon","tue","wed","thur","fri"] # 대괄호로 리스트 선언 후 요소들을 , 로 구분
# 총 5개의 개별 스트링 값을 대괄호 안에 갖게 됨.
# classs 'list'

# common and mutable sequence operations 사용 가능

# common 하다
print("mon" in days) #true 출력
print("oops" in days) #false 출력
print(days[0]) # mon 출력
print(len(days)) # 5 출력

# mutable하다 = 값을 변경할 수 있다.
days.append("sat")
print(days) # 토요일이 추가
#이 외에도 insert, clear, pop, remove, reverse 등 다양하다

# 2. 열거형 타입 : 튜플...day1_2에
