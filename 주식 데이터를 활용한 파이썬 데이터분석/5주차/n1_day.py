import yfinance as yf
yf.pdr_override()

import numpy as np
import pandas as pd

import FinanceDataReader as fdr

def get_return(code, k):
    df = fdr.DataReader(code,'2018')
    df['High2'] = df['High'].shift(1)
    # 오늘 사야하는 가격 출력
    df['buy_at'] = (df['High'].shift(1) - df['Low'].shift(1))*k + df['Open']
    # 구매 여부 체크
    df['is_buy'] = np.where(df['buy_at'] < df['High'], 'buy', '')
    # 판매 가격 출력
    df['sell_at'] = df['Open'].shift(-1)
    # 구매날짜만 정제하기
    df = df[df['is_buy']=='buy']
    # 수익률 구하기
    df['return'] = df['sell_at']/df['buy_at']
    df['누적곱'] = df[['return']].cumprod()
    return df[['누적곱']].iloc[-1,-1] -1

df = {
        'k' : [],
        'return' : []
}
# 최적의 K 정보 출력하기
for k in np.arange(0.4, 0.6, 0.01):
    df['k'].append(k)
    df['return'].append(get_return('005930', k))

df_result = pd.DataFrame(df)
print(df_result.sort_values(by = 'return', ascending = False))