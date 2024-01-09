## 모듈
# 필요한 기능끼리 부품처럼 잘 만들어진 파일을 의미함.
# 유지보수 및 코드의 재사용이 편리해짐.

import theater_module
# 3명이서 영화를 보러갔을 때 가격 
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)


# theater_module의 내용을 mv로 호출할 수 있음
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# from random import *
# theater_module을 작성할 필요없이 모든것을 import하겠다는 의미.
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# theater_module 에서 필요한 몇몇개의 함수만 쓰겠다는 의미.
# price_soldier 을 호출할 수 없다.
from theater_module import price, price_morning
price(3)
price_morning(4)
try:
    price_soldier(5)
except NameError:
    print("해당 함수는 정의되지 않았습니다.")

# price_soldier 에 price라는 별명을 붙임.
from theater_module import price_soldier as price
# price_soldier이 호출됨
price(3)