## 예외처리
# 에러가 발생했을 때 그에대해 처리해주는 것을 의미함.

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다.")
    # 에러문장을 그대로 출력할 수 있다.
    print(err)
# ValueError / ZeroDivisionError 이 아닌 다른 에러 발생 시, 동작함
except:
    print("알 수 없는 에러가 발생하였습니다.")


## 사용자 정의 예외처리

class BigNUmberError(Exception):
    # pass
    # 메시지를 같이 넣고싶을 때,
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

## 에러 발생시키기
try:
    print("한 자리 숫자 나누게 계산기입니다.")
    nums = []
    for i in range(2):
        nums.append(int(input("숫자를 입력하세요 : ")))
        # 입력숫자가 10보다 크면 VAlueError 발생시킴
        if nums[i] <=0:
            raise ValueError
        elif nums[i] >=10:
            # BigNUmberError 의 괄호안의 내용을 class의 msg로 던짐.
            raise BigNUmberError("{}번째 입력값 : {}".format(i+1, nums[i]))
    print("{} / {} = {}".format(nums[0], nums[1], int(nums[0]/nums[1])))
except ValueError:
    print("숫자가 너무 작습니다. 1~10 사이의 숫자를 입력하세요.")
# BingNumberError 의 self.msg 를 err 로 return함.
except BigNUmberError as err:
    print("숫자가 너무 큽니다. 1~10 사이의 숫자를 입력하세요.")
    print(err)

## finally
# 예외처리구문이 정상작동하든 오류가 나든 반드시 실행되는 구문
finally:
    print("계산기가 종료되었습니다.")

## 퀴즈
'''
1. 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
   출력 메시지 : "잘못된 값을 입력하였습니다."
2. 대기 손님이 주문할 수 있는 치킨양을 10마리로 한정.
   치킨 소진 시, 사용자 정의 에러 SoldoutError을 발생시킨 뒤 프로그램 종료
   출력 메시지 : "재고가 소진되어 더이상 주문을 받지 않습니다."
'''

chicken = 20
waiting = 1
class SoldoutError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg


while(True):
    try:
        if chicken == 0:
            raise SoldoutError("재고가 소진되어 더이상 주문을 받지 않습니다.")
        print("남은 치킨 : {}".format(chicken))
        order = int(input("치킨 몇마리를 주문하시겠습니까?"))

        if order < 1:
            raise ValueError
        elif order > 10:
            print("대기손님은 치킨을 10마리까지 주문 가능합니다.")
        elif order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {}] {}마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting +=1
            chicken -=order
        
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldoutError as err:
        print(err)
        break
