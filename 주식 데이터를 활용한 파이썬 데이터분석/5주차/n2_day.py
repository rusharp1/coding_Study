import yfinance as yf
import numpy as np
import pandas as pd
import FinanceDataReader as fdr
def get_return_mf(code):
    df = fdr.DataReader(code, '2018')
    df = df.reset_index()
    df = df[['Date', 'Open']]

    # Date를 Datetype으로 변경
    df['Date'] = pd.to_datetime(df['Date'])
    # Date를 요일로 변경
    df['Day'] = df['Date'].dt.day_name()
    # 월, 금 라인만 노출하기
    df = df[(df['Day'] == 'Monday') | (df['Day'] == 'Friday')]

    # 처음 시작이 Friday 면 0번째 드랍
    if df.iloc[0,2] == 'Friday':
        df = df.drop(index=df.index[0])
        
    if df.iloc[-1,2] == 'Monday':
        df = df.drop(index=df.index[-1])

    # 월, 월 이렇게 되어있는 경우 앞에있는 월요일을 삭제함
    cond = (df['Day'] == df['Day'].shift(-1))&(df['Day'] == 'Monday')
    df = df.drop(index=df.index[cond])
    # 금, 금 이렇게 되어있는 경우, 뒤에있는 금요일을 삭제함.
    cond = (df['Day'] == df['Day'].shift(1))&(df['Day'] == 'Friday')
    df = df.drop(index=df.index[cond])

    # 다음날의 Open값을 가져온 뒤 Day 가 Monday 인 값만 정리함.
    df['Open_Fri'] = df['Open'].shift(-1)
    cond = df['Day'] == 'Monday'
    df = df[cond]

    # 테이블 정리
    df = df[['Open', 'Open_Fri']]
    df.columns = ['buy_at', 'sell_at']

    # 테이블에 0 값이 있는 경우, 제거
    cond = (df['buy_at']!=0)&(df['sell_at']!=0)
    df = df[cond]

    df['return'] = df['sell_at']/df['buy_at']
    return df[['return']].cumprod().iloc[-2, -1]-1