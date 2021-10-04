# 2. 열거형 타입 : 튜플,,

# 앞서 봤던 리스트와 달리 immutable...수정 불가능하다.
# list와는 다르게 common sequence operation만 사용 가능

# 리스트의 대괄호를 소관호로 바꿔주면 그게 튜플이다.
days = ("mon","tue","wed","thur","fri")
print(type(days)) # class 'tuple'

# 리스트처럼 add reverse delete 이런걸 원하지 않을 때, 아무도 변경할 수 없도록
# 하는 sequence를 써야할 때 튜플을 쓴다.

# common 연산은 모두 쓸 수 있다. in, +, item 추출, len 등등

##############################

# 딕셔너리
# 키와 value로 이뤄진 구조.

charactor = {
    "name" : "magician",
    "age" : 14,
    "korean" : True,
    "fav_food" : ["kimchi","bulgogi"]  #딕셔너리 내부에 리스트, 튜플 등도 저장 가능
}
print(charactor)
print(charactor["name"]) 

# 딕셔너리에 키,값 추가하기
charactor["pretty"] = True
print(charactor)