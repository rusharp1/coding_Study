
## 패키지
# 모듈들을 모아놓은 집합을 의미함.
# import ~ 마지막에 반드시모듈이나 패키지가 와야한다.
# 클래스나 함수는 import를 바로 할 수 없음.
# import travel.thailand.ThailandPackge X
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from~impor 구문에서는 모듈, 패키지, 함수, 클래스 모두  import 가능.
# from 패키지.모듈 import 클래스
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

# from 패키지 import 모듈.
from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()


## __all__
# travel 모듈안의 모든것을 import하겠다는 의미.
# 실제로는 개발자가 문법안에서 공개범위를 설정해야 함.
# 모듈 안의 __init__ 에 `__all__ = ["vietnam", "thailand"]`
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()


## 패키지, 모듈 위치
# 같은 경로에 있는 패키지 모듈 사용해왔음.
# 어느 위치에 있는지 확인할 방법

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

## pip installl
# 패키지를 설치할 수 있다.
# pip install 패키지명 : 패키지를 설치할 수 있음.
# pip list : 설치된 패키지 리스트를 받아올 수 있음.
# pip show 패키지명 : 패키지에 대한 정보를 보여줌.
# pip install --upgrade 패키지명 : 해당패키지를 업그레이드 진행함.
# pip uninstall  패키지명 : 패키지 설치 삭제함.

## 내장함수
# 따로 import할 필요 없이 바로 사용가능한 함수.
# ex) input, print, ...
# dir : 어떤 객체를 넘겨줬을 때, 그 객체가 어떤 변수와 함수를 가지고 있는지 표시.
import random
print(dir())
# random 모듈 내에서 쓸수 있는 것들을 출력함.
print(dir(random))

list = [1,2,3]
# list 모듈 내에서 쓸수 있는 것들이 출력됨
print(dir(list))

name = "조희진"
# string 에서 사용할 수 있는 것들을 출력함.
print(dir(name))


## 외장함수
# 내장함수와 달리 직접 import하여 사용해야하는 것들
# list of pythono modules 검색 후 확인 가능.

# glob : 경로 내 폴더/파일 목록 조회 (윈도우 dir)
import glob
# 확장자가 .py인 모든 파일 조회
print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본기능
import os
# 현재 디렉토리 표시
print(os.getcwd())
folder = "sample_dir"

# sample_dir 폴더가 있으면 진행.
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    # 폴더를 삭제.
    os.rmdir(folder)
    print("폴더를 삭제하였습니다.")
else:
    # 폴더 생성.
    os.makedirs(folder) # 폴더 생성.
    print(folder,"폴더를 생성하였습니다.")

# 현제 디렉토리 내 파일목록을 출력함.
print(os.listdir())

print("--------------import time--------------")
# time : 시간관련 함수
import time
print(time.localtime())
# 원하는 형태로 출력할 수 있음.
print(time.strftime("%Y-%m-%d %H:%M:%S "))

# datetime
import datetime
print("오늘 날짜는 :", datetime.date.today())
td = datetime.timedelta(days=100) # 100일을 저장함.
print("오늘 기준 100일 뒤는", datetime.date.today() + td)
print("오늘 기준 100일 전은", datetime.date.today() - td)


## 퀴즈
'''
프로젝트 내 나만의 시그니처를 남기는 모듈을 만들기.
'''
import byme
byme.sign()

