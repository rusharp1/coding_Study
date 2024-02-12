import yfinance as yf
import numpy as np
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

def get_return_sl(code, short, long):
    df = fdr.DataReader(code,'2018')
    df = df[['Close']]
    # 단기이평선, 장기이평선 구하기
    df['short'] = df.rolling(short).mean().shift(1)
    df['long'] = df['Close'].rolling(long).mean().shift(1)
    # 매수/매도 정하기
    df['action'] = np.where(df['short']>df['long'], '매수','매도')

    # 진짜 판매하는 날짜
    cond = (df['action'] == '매수') & (df['action'].shift(1) == '매도')
    # df_compare['real_buy'] = np.where(cond,'매수', '')
    df_buy = df[cond].reset_index()
    df_buy.columns = ['날짜(buy)','종가(buy)','단기 이평값(buy)','장기 이평값(buy)','액션(buy)']

    cond = (df['action'] == '매도') & (df['action'].shift(1) == '매수')
    # df_compare['real_sell'] = np.where(cond,'매도', '')
    # reset_index 를 통해 index 를 초기화함.
    df_sell = df[cond].reset_index()
    df_sell.columns = ['날짜(sell)','종가(sell)','단기 이평값(sell)','장기 이평값(sell)','액션(sell)']

    # 수익율 정하기
    df_result = pd.concat([df_buy, df_sell], axis=1)
    df_result['수익률'] = df_result['종가(sell)']/df_result['종가(buy)']
    df_result['누적곱'] = df_result[['수익률']].cumprod()

    df_final = (df_result[['누적곱']].tail(1) - 1)*100
    df_final['단기'] = short
    df_final['장기'] = long
    
    return df_final