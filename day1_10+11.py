#boolean operation : and ,or ,not

def age_chk(age):
    print(f"your {age}")
    if age < 18:
        print("u cant drink")
    elif age == 18:
        print("you are new to this")
    elif age > 20 and age < 25:  # 여러 조건이 포함된 and 연산자
        print("you are stil kind of young")
    else:
        print("u can drink")

age_chk(23)


##########

# for

days = ("mon","tue","wed","thu","fri")

for x in days:
    # x는 변수
    if x is "wed":
        break
    else:
        print(x)

for y in [1,2,3,4,5]:
    print(y)

#파이썬에서는 string도 일종의 배열이므로
for letter in "abafsdgasdg":
    print(letter)