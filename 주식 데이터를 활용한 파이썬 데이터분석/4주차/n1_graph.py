# from pandas_datareader import data as pdr
import yfinance as yf
import numpy as np
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# 이평선 적용 후 매수/매도 적정 시기 지정 및 비교표 작성.


# yfinance 라이브러리를 사용하여 데이터 다운로드 설정
yf.pdr_override()
# FinanceDataReader를 사용하여 주식코드가 '005930' 종목(삼성전자) 의 2018년 이후 데이터 다운로드
df = fdr.DataReader('005930','2018')
# 다운로드한 데이터의 처음 5행 출력
print(df.head())

# 종가를 사용하여 그래프 생성
df.plot(y=['Close'])
plt.show()

# 그래프 크기 조절
df.plot(y=['Close'], figsize=[15,8])
plt.show()

# 격자선 생성
df.plot(y=['Close'],grid=True)
plt.show()

# 시작가, 종가 그래프로 생성
df.plot(y=['Open','Close'])
plt.show()

# df 내 모든 그래프를 출력함.
df.plot()
plt.show()

# 삼성전자와 LG전자의 종가 그래프 생성.
df_1 = fdr.DataReader('066570', '2018')

df_result = pd.DataFrame()
df_result['Samsung'] = df['Close']
df_result['LG 전자'] = df_1['Close']

df_result.plot(figsize=[15,8])
plt.show()

# 최근 100일의 변동률 그래프로 생성.

df_result = pd.DataFrame()
df_result['Samsung'] = df['Change']
df_result['LG 전자'] = df_1['Change']

df_result.tail(100).plot(figsize=[15,8])
plt.show()

