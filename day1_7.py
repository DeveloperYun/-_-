# keyword argument : 인자가 위치에 따라 정해지는게 아닌 이름으로 쌍을 이룸
# 인자 개수가 많아질 때 유용하다.

def plus(a,b):
    return a-b

result = plus(b=30, a=1) #인자 위치가 아닌, 이름에 따라 결정되었음
print(result)

####
#string 안에 변수를 포함시키고 싶다면 f(format)를 앞에 붙이고 변수를 {}감싼다
def say_hello(name, age):
    return f"hello {name} u are {age} years old"

hello = say_hello(age="14",name="david") #키워드 인자
print(hello)

#혹은 + 연산자로 string을 이어주는 방법도 있다.
def say_hola(name, age):
    return "hello " + name + " u are " + age + " years old"

hola = say_hola("lucy","29")
print(hola)