## if
weather = input("오늘 날씨는 어때요? : ")
if weather == "비"or"눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else :
    print("준비할 필요 없어요.")

# input은 무조건 string type으로 들어가기 때문에 int형으로 변경 필요.
temp = int(input("기온은 어때요? : "))
if temp >= 30:
    print("너무 더워요. 나가지 마세요")
elif temp < 30 and temp >=10:
    print("날씨가 좋아요")
# temp < 10 and temp >=0 대신 하나로 합쳐 사요할 수 있다.
elif 0 <= temp <10 : 
    print("외투를 챙기세요")
else :
    print("너무 추워요. 나가지 마세요.")


## for
# range(n,m) > n~m-1까지의 범위
# range(n) > 0~n-1까지의 범위
for waiting_no in range(5):
    print("대기번호 : {}".format(waiting_no))

# customer 에 'a'~'z'까지 리스트로 입력.
# 대문자로 입력하고 싶은 경우, ascii_uppercase 사용.
from string import ascii_lowercase
customers = list(ascii_lowercase)
print(customers)

for customer in customers:
    print(f"{customer} 님, 커피가 준비되었습니다.")

## while
# 손님을 5회호출 후 커피 폐기
index = 5
# index 가 1보다 크거나 같을때까지 반복함.
while index>=1:
    print(f"{customer}님, 커피가 준비되었습니다. {index}번 남았어요.")
    # 만약 v 가 없으면 무한루프로 들어간다.
    # 무한루프로 들어갔을때 터미널에서 ctrl+c를 통해 종료 가능.
    index -=1
print("커피는 폐기되었습니다.")

person = "null"
while person != customer:
    print(f"{customer}님, 커피가 준비되었습니다.")
    person = input("이름이 어떻게 되세요? : ")


## continue와 break
absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        # continue : 남은 문장을 실행하지 않고, 다음 분기 실행.
        continue
    elif student in no_book:
        # break : 남은 문장을 실행하지 않고 반복문 종료.
        print("오늘 수업은 여기까지 {}는 교무실로 따라와".format(student))
        break
    else:
        print("{}번, 책을 읽으세요".format(student))


## 한줄 for
# 출석번호가 1,2,3,4 > 100을 더함
students = list(range(1,6))
print(students)
students = [i+100 for  i in students]
print(students)

# 이름을 길이로 변환
students = ["ironman", "spiderman", "thor", "i am groot"]
students = [len(i) for i in students]
print(students)

# 이름을 대문자로 변환
students = ["ironman", "spiderman", "thor", "i am groot"]
students = [i.upper() for i in students]
print(students)

# 2단 for문 한줄쓰기
list = []
for i in range(4):
    for j in range(4):
        list.append(j)
print(list)

# 들어갈 변수명 for문1 for문2
list = [j for i in range(4) for j in range(4)]
print(list)

# print문 안에 if문
# 결과1 if 조건1 else 결과2
int_a = 5
if int_a > 3:
    print("over")
else:
    print("under")

print("over" if int_a > 3 else "under")

# 2단 if문 활용
int_a = 3
if int_a > 3:
    print("over")
elif int_a ==3:
    print("same")
else:
    print("under")

# 결과1 if 조건1 else 결과2 if 조건2 else 결과3
int_a = 3
print("over" if int_a > 3 else "same" if int_a ==3 else "under")

# for/if문 혼합
list2 = []
for i in list:
    if i >= 2:
        list2.append(i)
print(list2)

list2 = [i for i in list if i >= 2]
print(list2)


## 퀴즈
'''
50명의 승객과 매칭 기회가 있을 때 총 탑승 승객 수를 구하는 프로그램
1. 승객별 운행 소요 시간은 5~50분
2. 나는 5~15분 사이의 승객만 매칭해야 합니다.
'''

from random import *

index = 0
for customer in range(1,51):
    time = randint(5,50)
    if 5<=time<=15:
        print("[o] {}번째 손님 (소요시간 : {}분)"\
          .format(customer, time))
        index +=1
    else:
        print("[x] {}번째 손님 (소요시간 : {}분)"\
          .format(customer, time))
    # print문 안에 if문을 삽입하는 방법 : 참 if 조건 else 거짓
    # print("[{}] {}번째 손님 (소요시간 : {}분)".format('0' if 5<=time<=15 else 'x', customer, time))


print("총 탑승 승객 : {}분".format(index))

