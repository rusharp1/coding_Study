print("hello world")

## 숫자형 자료 출력
print(5)
print(10)
print(3.14)
print(5+4)
print(5*2)
print(5*(2+6))

## 문자형 자료 출력
print('풍선')
print("나비")
print("ㅋ"*10)

## boolean
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5<10))


## 변수
name = "해피"
animal = "고양이"
age = 2
hobby = "낮잠"
is_adult = age>=3


# + 사용 시, 무조건 str 변수로 변경해야함
print("우리집"+animal+"의 이름은 " +name+"에요")
print(name+"는"+str(age)+"살이며"+hobby+"를 좋아해요")
print(name+"는 어른일까요?"+str(is_adult))


# , 사용 시, 무조건 스페이스가 추가됨
print("우리집",animal,"의 이름은 " ,name,"에요")
print(name,"는",age,"살이며",hobby,"를 좋아해요")
print(name,"는 어른일까요?",is_adult)


## 주석이란? 코드에 작성되어있지만 실행되지 않는 범위
# 여러문장에 대한 주석처리는 ''' 으로 작성함.
'''
ctrl + / 를 사용하여 여러줄 주석처리 및 해제가 가능함.
'''

## 퀴즈
station = "사당", "신도림", "인천공항"
for stations in station:
    print(stations+"행 열차가 들어오고 있습니다.")

print(type(station))