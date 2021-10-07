# 모듈 import 하기
# 모듈의 쓸만한 일부만 import 할 수도 있다. 이게 낫다.
from math import ceil
#import math # 수학 기능 모아둔 모듈

# 모듈에서 가져올 함수의 이름을 바꿀 수도 있다.
# from math import ceil as sexy_upper   이런식으로

print(ceil(1.2)) # 값을 올림해주는 ceil
#print(math.fabs(-1.2)) # 절대값 출력

