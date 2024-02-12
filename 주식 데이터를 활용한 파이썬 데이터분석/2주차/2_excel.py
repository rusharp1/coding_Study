# pip install pandas numpy
import pandas as pd
import numpy as np

# 종목데이.xlsx 파일가져오기
df = pd.read_excel('종목데이터.xlsx')
print(df)
# 앞에서 5개의 셀을 출력하기
print(df.head())
# 뒤에서 10개의 셀을 출력하기
print(df.tail(10))
# 소숫점 2번째 자리까지만 출력
pd.options.display.float_format = '{:.2f}'.format
print(df)