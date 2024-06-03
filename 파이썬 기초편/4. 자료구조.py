
## 리스트

subway = ["a", "b", "c"]

# subway변수 내 b의 위치 찾기
print("subway.index(\"b\") : ", subway.index("b"))

# "d"를 subway 리스트 가장 뒤에 삽입함.
subway.append("d")
print("subway.append(\"d\") : ",subway)

# "e" 를 b와 c 사이에 삽입
subway.insert(2, "e")
print("subway.insert(2, \"e\") : ",subway)

# subway 리스트를 뒤에서 한개씩 꺼냄
print(subway.pop())
print("subway.pop() : ",subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway.append("c")
print("subway.count(\"c\") : ",subway.count("c"))

# 정렬 가능 sort : 정순 / reverse : 역순
subway.sort()
print("subway.sort() : ",subway)
subway.reverse()
print("subway.reverse() : ",subway)

# subway의 내용을 모두 지우기
subway.clear()
print("subway.clear() : ",subway)

# 다양한 자료형을 함께 사용 가능.
mix_list = ["조세호", 20, True]

# 리스트 확장
subway = ["a", "b", "c"]
subway.extend(mix_list)
print("subway.extend(mix_list) : ",subway)


## 사전(dictionary)
# 사전은 { } 를 사용한다, key : value 로 이루어져 있음.
cabinet = {3:"c", 2:"b"}

# cabinet변수에서 키값을 통해 value 찾기.
print(cabinet[3])
print(cabinet.get(3))

# 사전에 없는 키값을 검색 시,
# 변수[key]는 에러가 발생
# 변수.get(key)는 `None`을 출력한다.
# print(cabinet[5])
# (key , "대체값") 사용 시 `None` 대신 `대체값`출력
print(cabinet.get(5, "사용 가능"))


# key 가 cabinet안에 있으면 True / 없으면 False
print("3 in cabinet : ",3 in cabinet)

# 정수가 아닌 string으로도 출력할 수 있다.
cabinet = {"A-3":"조씨", "B-1":"차씨"}
print(cabinet["A-3"])

# cabinet안의 값 추가 / 변경
print(cabinet)
cabinet["A-3"] = "김씨"
cabinet["C-2"] = "변씨"
print(cabinet)

# cabinet의 값 제거
del cabinet["A-3"]
print(cabinet)

# key : key값만출력 / values : value값만 출력
print(cabinet.keys())
print(cabinet.values())
# items : key와 value를 매칭하여 출력
print(cabinet.items())

# cabinet 변수를 초기화
cabinet.clear()
print(cabinet)


## 튜플
# 튜플은 리스트와 다르게 리스트 변경이 되지 않지만 속도가 리스트보다 빠름
menu = ("돈까스", "치즈돈까스")
print(menu)

# 아래와 같이 추가할 수 없음
# menu.add("생선까스")

# 아래와 같이 선언하면 여러가지 변수를 한번에 선언할 수 있다.
(name, age, hobby) = ("조희진", "29", "게임")
print(name, age, hobby)


## 집합 (set)
# 중복 X , 순서 x
my_set = {1,2,3,4,5,4,3}
# 1,2,3,4,5 만 출력된다. 4,3은 중복이라서 제외됨
print(my_set)

# set 선언 2가지 방법.
set1 = {'a','b','c'}
set2 = set(["a","d"])

# set1과 set2의 교집합 구하기
print(set1&set2)
print(set1.intersection(set2))

# set1과 set2의 합집합 구하기
print(set1|set2)
print(set1.union(set2))

# set1에서 set2의 차집합 구하기
print(set1-set2)
print(set1.difference(set2))


# set2에 값을 추가하기
set1.add('f')
print(set1)
print(sorted(set1))

# set1에 값을 제거하기
set2.remove('d')
print(set2)


## 자료구조를 변경하기
# 처음 시작은 set
print(my_set, type(my_set))

# list로 변경
my_set = list(my_set)
print(my_set, type(my_set))

# tuple로 변경
my_set = tuple(my_set)
print(my_set, type(my_set))

# set 으로 변경
my_set = set(my_set)
print(my_set, type(my_set))


## 퀴즈4
'''
댓글 작성자중 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 뽑는 추첨프로그램 작성
1. 댓글은 20명이 작성했다고 가정하고 아이디는 1~20
2. 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
3. random 모듈의 suffle / sample 활용
'''

from random import *

# range를 통해 범위를 한번에 list에 작성.
comment = list(range(1,21))

print(comment, type(comment))

# 리스트 섞기
shuffle(comment)
print(comment)

# 나는 하나를 뽑고 제거했는데 선생님은 4개를 뽑고 1/4으로 나눔
# sample로 뽑았을때 list로 들어가는것도 확인하기
chicken = sample(comment,1)
comment.remove(chicken[0])
print("치킨 담청자 : ",chicken)

print(comment)
print("치킨 담청자 : ",sample(comment,3))
