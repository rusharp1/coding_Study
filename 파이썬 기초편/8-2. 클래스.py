## 상속
class unit:
    def __init__(self,name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]"\
              .format(self.name, location, self.speed))

class AttackUnit(unit):
    def __init__(self, name, hp, damage, speed):
        # self.name ~ speed는 unit 클래스에서도 사용하고 있음.
        # unit 클래스 내용을 상속받아서 attackunit 만들 수 있음.
        '''
        self.name = name
        self.hp = hp
        self.speed = speed
        '''
        # unit 에서 만들어진 생성자를 호출해서 이름/체력 정의 가능.
        unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]"\
              .format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다."\
              .format(self.name,damage))
        self.hp -=damage
        print("{} : 현재 체력은 {} 입니다.". format(self.name, self.hp))
        if self.hp<=0:
            print("{} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16, 10)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


## 다중상속.
# 공중유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송 (공격X)
class flyable:
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
              .format(name, location, self.flying_speed))

# 공중 + 공격 유닛  
class Flyable_Attack_unit(AttackUnit, flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 스피드는 0
        flyable.__init__(self,flying_speed)
    # self.fly를 호출함으로서 move를 통해서도 fly함수를 호출하도록 함.
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

valkyrie = Flyable_Attack_unit("발키리",200,6,5)
# Flyable 의 fly 에는 초기화된 name, location 변수가 없어서 따로 지정
# 반면 flying_speed 정보는 포함되어있어 지정 X
valkyrie.fly(valkyrie.name,"3시")


## 메소드 오버라이딩
# 자식메소드에서 정의한 메소드를 부모 메소드에서 쓰고싶을 때, 쓰는방법.
vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = Flyable_Attack_unit("배틀크루저",500, 25, 3 )

# unit 함수의 move를 호출함
vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# 상속받은 AttackUnit>Unit>move 함수를 호출하는 것이 아니고
# Flyable_Attack_unit 에 재정의된 move함수를 호출함.
battlecruiser.move("9시")

## pass
class Building_Uint(unit):
    def __init__(self, name, hp, location):
        # 일단 아무것도 안하고 넘어감.
        pass

# 서플라이 디폿 : 건물, 1개 건물 = 8unit
supply_depot = Building_Uint("서플라이 디폿", 500, "7시") 

def game_start():
    print("[알림] 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

## super
class BuildingUint(unit):
    def __init__(self, name, hp, location):
        # super 을 사용하면 상속받는 부모클래스(unit) 초기화 가능.
        # unit.__init__(self, name, hp, 0) 와 동일하게 작동한다.
        # 다만 다중상속인 경우, 처음에 있는 class만 호출된다.
        super.__init__(name, hp, 0)
        self.location = location


## 퀴즈
'''
총 3개의 매물이 있습니다.
1. 강남아파트 매매 10억 2010년
2. 마포 오피스텔 전세 5억 2007년
3. 송파 빌라 월세 500/50 2000년
'''

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    def show_detail(self):
        print("{0} {1} {2} {3} {4}년".format(self.location, self.house_type,\
                         self.deal_type, self.price, self.completion_year))

# 클래스도... 리스트에 넣을수 있다니..!!
houses = []
house = House("강남", "아파트", "매매", "10억", "2010")
houses.append(house)
house = House("마포", "오피스텔", "전세", "5억", "2007")
houses.append(house)
house = House("송파", "빌라", "월세", "500/50", "2000")
houses.append(house)

print("총 {}개의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
