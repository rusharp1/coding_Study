import pandas as pd
import numpy as np

df = pd.read_excel('종목데이터.xlsx')
# 어제 오른 종목들만 골라보기
cond = df['change_rate'] > 0
print(df[cond])

# per가 0 인 종목들을 제거하기
cod = df['per'] !=0
print(df[cond])

# 순이익, 종가를 추가하기
df['earning'] = df['marketcap']/df['per']
df['close'] = df['eps']*df['per']
print(df)

# date 컬럼을 없애기
del df['date']

# `pbr < 1` & `시총 1조 이상` & `per < 20` 을 추려보기
cond = (df['pbr'] < 1)&(df['per']<20)& (df['marketcap']>=1000000000000)
df[cond]

df[cond]