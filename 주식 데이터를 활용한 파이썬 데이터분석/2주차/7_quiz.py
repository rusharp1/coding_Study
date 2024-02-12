# S&p 500 기업 중 수익률 best 10 기업을 찾고, 바 그래프로 그리기.

import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd

df = fdr.StockListing('S&P500')
rate_list = []
for Symbol in df['Symbol']:
    df_fdr = fdr.DataReader(Symbol,'2017')
    # 시작가 지정
    try:
        original = df_fdr['Open'][0]
        # 수익률 표 생성 (df_rate)
        df_rate = df_fdr['Close']/original -1
        rate_list.append(df_rate[-1])
    except:
        rate_list.append(-1000)
# df['rate'] 에 수익률 마지막 값 추가.
df['rate'] = rate_list
df = df[['Symbol','rate']]

# rate 를 내림차순으로 지정, idx 값을 Symbol 로 지정.
df = df.sort_values(by='rate', ascending=False).head(10)
df.set_index('Symbol',inplace=True)
df.plot(kind='bar')
plt.show()


