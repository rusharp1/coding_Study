## 함수
def open_account():
    print("새 계좌가 생성되었습니다.")
# 함수호출해야지 작동함.

# balance : 잔액 / money : 입금할 금액
def deposit(balance, money):
    balance = balance+money
    print("입금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance))
    plus = input("추가 입금하사겠습니까? : ")
    if plus == 'y':
        money = input("입금할 금액을 입력하세요 : ")
        balance = deposit(balance, int(money))
    return balance

# balance : 잔액 / money : 출금할 금액
def withdraw(balance, money):
    if balance >= money:
        balance = balance-money
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance))
        plus = input("추가 출금하사겠습니까? : ")
        if plus == 'y':
            money = input("출금할 금액을 입력하세요 : ")
            balance = withdraw(balance, int(money))
    else : 
        print("잔액이 {}원 부족합니다. 출금 금액을 확인해주세요".format(money - balance))

    return balance

# balance : 잔액 / money : 출금할 금액
def withdraw_night(balance, money):
    commission = 100 # 수수료
    if balance >= money+commission:
        balance = balance-money-commission
        print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance))
        plus = input("추가 출금하사겠습니까? : ")
        if plus == 'y':
            money = input("출금할 금액을 입력하세요 : ")
            balance = withdraw_night(balance, int(money))
    else : 
        print("잔액이 {}원 부족합니다. 출금 금액을 확인해주세요".format(money+commission - balance))
    # 여러개의 변수를 함꼐 반환할 수 있음.
    return balance, commission

open_account()
balance = 10000

money = input("입금할 금액을 입력하세요 : ")
balance = deposit(balance, int(money))
print("balance : ",balance)

money = input("출금할 금액을 입력하세요 : ")
balance = withdraw(balance, int(money))
print("balance : ",balance)

money = input("(밤)출금할 금액을 입력하세요 : ")
balance, commission = withdraw_night(balance, int(money))
print("balance, commission : ",balance, commission)


## 기본값
def profile(name, age, main_lang):
    print("이름 : {} \t나이 : {}\t사용언어 : {}"\
          .format(name, age, main_lang))
    
profile("조희진", 29, "python")

# 함수명(변수, 변수 = 기본값) ... 을 사용할 수 있다.
# 다만 이 경우, 기본값이 있는 변수 뒤에는 무조건 기본값이 있어야 한다.
def default_profile(name, age=17, main_lang="파이썬"):
    print("이름 : {} \t나이 : {}\t사용언어 : {}"\
          .format(name, age, main_lang))

default_profile("조희진")
default_profile("조현서")

## 키워드값
# 함수에서 받는 변수값을 키워드를 통해 입력 시, 순서에 관계없이 잘 전달됨
profile("조희진", main_lang = "Java", age= 24)


## 가변인자
# 함수내 변수 앞에 *을 붙이면 넣고싶은만큼 값을 넣을 수 있다.
def changeable_profile(name, age, *lang):
    print("이름 : {} \t나이 : {}\t사용언어 : "\
          .format(name, age),end = "")
    for i in lang:
        print("{}".format(i),end = ",")
    print()
    # print안에 반복문을 사용하고 싶다면 list화 해야함.
    print("{}".format([i for i in lang]))

changeable_profile("조희진", 29,"java", "c", "python", "selenium")
changeable_profile("조현서", 29,"html", "xlm")

## 지역변수와 전역변수
# 지역변수 : 함수 내에서만 사용할 수 있는 변수
# 전역변수 : 함수 외에서도 사용할 수 있는 변수

apple = 10

def remind_apple(eat):
    # 해당 케이스일 때, apple은 초기화되지 않아 에러 발생.
    # 즉 아래에 있는 apple은 지역변수
    # apple = apple - eat
    print ("함수 내 남은 사과 : {}".format(apple))

# 전역변수 : global 변수 = 값
def g_remind_apple(eat):
    # 전역공간에 있는 apple을 사용
    # 함수 내 연산이 전역변수에도 영향을 미침.
    global apple
    apple = apple - eat
    print ("함수 내 남은 사과 : {}".format(apple))


def return_remind_apple(apple, eat):
    apple -= eat
    print ("함수 내 남은 사과 : {}".format(apple))
    return apple

g_remind_a`p`ple(3)
print ("함수 밖 남은 사과 : {}".format(apple))
apple = return_remind_apple(apple, 2)
print ("함수 밖 남은 사과 : {}".format(apple))


## 퀴즈
'''
표준 체중을 구하는 프로그램
1. 남자 : 키(m) x 키(m) x 22
2. 여자 : 키(m) x 키(m) x 21
-> 표준 체중은 소숫점 둘째자리까지 표시
'''

def std_weight(height, gender):
    print("키 {}cm {}의 표준 체중은, {} kg 입니다."\
          .format(int(height*100), gender, \
                  round(height*height*21 if gender == "여자" else height*height*22)))

std_weight(1.67 , "여자")