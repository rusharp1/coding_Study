import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd
from s5_return_rate import *


# 유망 기업을 찾기 위해서 S&P 500 기업 전체 주식 데이터를 가져와 봅시다.

df = fdr.StockListing('S&P500')
df = df[['Symbol', 'Name']].head(100)
# df['rate'] 에 df의 Symbol 로 Final_rate함수를 통해 추가함.
df['rate'] = df['Symbol'].apply(Final_rate)
# ('S&P500')


# 에러가 있는 행 처리하기
cond = df['rate'] != -1000
df = df[cond]

# rate를 기준으로 내림치순으로 정렬
df = df.sort_values(by='rate', ascending=False)

# index 값을 Name 으로 변경.
df.set_index('Name',inplace=True)
# bar 그래프로 만들어짐.
df.plot(kind = 'bar')
print(df)
# 어떤 회사의 최종 수익률을 구하려면?
# S&P 지수 전체에 값을 붙여볼까요?
# `head(10)` 이 아니라 `head(100)`으로 했더니 안되네요?
