print(abs(-5))                  # 절대값 5
print(pow(4,2))                 # 4^2 = 4*4 = 16
print(max(5,12))                # 최대값 12
print(min(5,12))                # 최소값 5
print(round(3.14))              # 반올림 3

from math import *              # math 라이브러리 활용

print(floor(4.99))              # 내림 4
print(ceil(3.14))               # 올림 4
print(sqrt(16))                 # 16의 제곱근 4

from random import *            # random 라이브러리 활용

print(random())                 # 0.0이상 1.0미만의 랜덤값(난수) 출력
print(random() * 10)            # 0.0이상 10.0미만
print(int(random() * 10))       # 0이상 10미만의 임의의 정수출력

#로또 값 출력
print(int(random() * 45) + 1)   # 1이상 45이하의 임의의 정수출력

print(randrange(1, 46))         # 1이상 45이하의 임의의 정수출력

print(randint(1, 45))           # 1이상 45이하의 임의의 정수출력