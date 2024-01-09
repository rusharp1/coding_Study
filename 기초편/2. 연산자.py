## 기본 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3 
print(5%3) # 5/3의 나머지
print(5//3) # 5/3의 몫

print(10>3)
print(4>=7) # 4는 7보다 크거나 같다.
print(3==3) # 3은 3과 같다.
print(3+4 == 7)

# not 연산
print(1!=3) # 1과 3은 같지않다.
print(not(1!=3)) # 위의 반대값

# 여러가지 연산자 합치기
print((3>0)and(3<5)) # True and True
print((3>0)&(3<5)) # & == and

print((3<0)or(3<5)) # True or True
print((3<0)|(3<5)) # | == or
print(5>3>2)
print(5>4>7)


## 간단한 수식
print(2+3*4)
print((2+3)*4)

number = 2+3*4
print(number) # 14

# 두개가 동일하다
number = number+2 # 16
number +=2 # 18

number *=2 # 36
number /=2 # 18
number -=2 # 16
number %=5 # 1


## 숫자처리함수
print(abs(-5)) # absolute 값 , 절대값을 출력함.
print(pow(4,3)) # 4^3, 4**3과 동일하다.
print(max(5, 12)) # 더 큰 값이 출력됨
print(min(5, 12)) # 더 작은 값이 출력됨
print(round(3.14)) # 반올림 : 3
print(round(3.84)) # 반올림 : 4

from math import *  # math library를 이용.
print(floor(4.99)) # 내림 : 4
print(ceil(3.14)) # 올림 : 4
print(sqrt(16)) # 제곱근 : 4


## 랜덤함수
from random import * 
print(random()) # 0.0~1.0 사이의 임의값 생성
print(random()*10) # 0.0~10.0 사이의 임의값 출력
print(int(random()*10)) # 0~10 미만의 임의의 값 생성(정수형)

print(int(random()*45)+1) # 1~46 사이의 임의의 값 생성
print(randrange(1,46)) # 1~45 사이의 임의의 값 생성 (마지막 값은 포함X)
print(randrange(1,46,5)) # 1~45 사이의 임의의 값 생성 (5 단위로 출력, 1,6,11 ... )
print(randint(1,45)) # 1~45 사이의 임의의 값 생성 (양쪽 끝의 값 포함)


## 퀴즈
'''
월 4회 스터디를 하는데 3번은 온라인 1회는 오프라인으로 하기로 함.
1. 랜덤으로 날짜를 뽑음
2. 월별 날짜는 다름을 감안하여 최소 일주일 28 이내로 정함
3. 매월 1~3일은 스터디를 준비해야하므로 제외
'''



# 3~28 사이의 랜덤 숫자를 중복되지 않게 4개 뽑기
num =sample(range(3,29),4)

# import random 을 사용했을 땐 함수 앞에 random.~을 써야한다.
# import random
# num = random.sample(range(3, 29),4)
print(num)


# print 뒤에 `end = str` 을 넣어 마지막이 줄바꿈 되신 str이 들어감.
print("온라인 스터디 모임 날짜는 매월", end = " ")

# for문의 경우, range와 함께 사용한다 (나중에....)
# i를 0부터 num의 크기인 4-1 미만의 값까지 입력 후 반복문 지정
for i in range(len(num)-1):
    print(num[i], end = ",")

# \b를 사용하여 앞의 `,`를 삭제하려는 의도.
print("\b일로 선정되었습니다.")

print("오프라인 스터디 모임 날짜는 매월",num[3],"일로 선정되었습니다.")