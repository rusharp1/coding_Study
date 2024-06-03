## 클래스
'''
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음.
name = "마린"
hp = 40
damage = 5

print("{}유닛이 생성되었습니다.".format(name))
print("체력 {}, 공격력 {}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 대포를 쓸수 있음 (일반/시즈모드)
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
이런식으로 매번 만들 수 없음.
'''

# 공격 함수
def attack(name, location, damage):
    print("{}:{} 방향으로 적군을 공격합니다. [공격력{}]"\
          .format(name, location, damage))

# class : 붕어빵 기계로 많이 묘사된다.
class unit:
    # __init__ : python 에서 쓰이는 생성자, 객채가 생성될때 자동으로 호출되는 부분
    # __init__ 은 특정 초기상태로 커스터마이즈된 인스턴스 객체로 생각하면 된다.
    # class로부터 만들어지는 요소들을 객체라고 표현함.
    def __init__(self,name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{}유닛이 생성되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}\n".format(self.hp, self.damage))

# marine1~tank : unit 클래스의 instance
# 객체가 생성될 때에는 기본적으로 self를 제외한 개수와 동일하게 작성.
marine1 = unit("마린", 40, 5)
marine2 = unit("마린", 40, 5)
tank = unit("탱크", 150, 35)

## 멤버변수
# 클래스 내에 정의된 변수로, 변수를 사용할 수 있음.
wraith1 = unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = unit("빼앗긴 레이스", 80, 5)
# Unit 클래스에 clocking이라는 변수는 없음
# wraith2 에 clocking이라는 변수를 추가로 할당 후 true를 입력.
wraith2.clocking = True
if wraith2.clocking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

## 메소드
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    # 메소드 : 객체에 속하는 함수, 즉 attack, damaged 등이다.
    def attack(self, location):
        # self.~ 는 자기자신에게 있는 멤버변수 값을 출력하는것.
        # self 없는 변수는 전달받은 값을 출력하는것.
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]"\
              .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다."\
              .format(self.name,damage))
        self.hp -=damage
        print("{} : 현재 체력은 {} 입니다.". format(self.name, self.hp))
        if self.hp<=0:
            print("{} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

