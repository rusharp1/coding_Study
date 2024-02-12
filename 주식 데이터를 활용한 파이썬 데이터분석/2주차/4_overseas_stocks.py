# pip install finance-datareader
# https://github.com/FinanceData/FinanceDataReader/wiki

import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd

# 금융 상품에 대한 상장 정보 가져옴
# S&P500에 상장된 종목 목록 가져오기
df_spx = fdr.StockListing('S&P500')
print(df_spx)

# 애플 2017-01-01 ~ 현재까지 주식 가져오기
# 금융 데이터를 쉽게 수집할 수 있게 해줌
# fdr.DataReader(코드, 시작 날짜)
df = fdr.DataReader('AAPL', '2017')
print(df)

# 애플 2017-01-01 ~ 2018-12-31 주식 가져오기
df = fdr.DataReader('AAPL', '2017', '2019')
print(df)

# 종가만 가져오기
df['Close'].plot()
plt.show()

# 종가와 시작가를 그래프로 출력
df[['Close', 'Open']].plot()
plt.show()


# 비어있는 pd 만든 뒤, 아마존/애플 주식값을 넣어 그래프로 만듬.
empty_df = pd.DataFrame()
empty_df['AMZN'] = fdr.DataReader('AMZN', '2017')['Close']
empty_df['AAPL'] = fdr.DataReader('AAPL', '2017')['Close']
empty_df.plot()
plt.show()


