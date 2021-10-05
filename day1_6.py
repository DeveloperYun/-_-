def plus(a,b):
    return a+b

def print_plus(a,b):
    print(a+b)

r_res = plus(2,3) # return 에 의해 5가 저장
p_res = print_plus(2,3)
print(p_res, r_res) # p_res는 Node  r_res는 5 가 출력된다.
# return 값이 함수의 최종 결과값으로 치환된다.


def return_plus(a,b):
    return a+b
    print("kalkafdklsajflsdfjskdfjasdfjl",True)

return_res = return_plus(2,4)
print(return_res) # 함수 안의 print는 실행되지 않았다. return 하는 순간 함수는 종료되기 때문.
#오직 한번의 return만 존재할 수 있음. 따라서 리턴 아래는 무효화.