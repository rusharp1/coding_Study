import yfinance as yf
import numpy as np
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

def get_return(code, n):
    df = fdr.DataReader(code,'2018')
    df_compare = df[['Close']]
    # 이동평균값 구하기 (n일)
    df_compare['ma'] = df_compare.rolling(n).mean()
    # 이동평균값을 뒤로 한칸 shift 하기
    df_compare['ma_shift'] = df[['Close']].rolling(3).mean().shift(1)
    df_compare['action'] = np.where(df_compare['Close']>df_compare['ma_shift'], '매수', '매도')

    cond = (df_compare['action'] == '매수') & (df_compare['action'].shift(1) == '매도')
    # df_compare['real_buy'] = np.where(cond,'매수', '')
    df_buy = df_compare[cond].reset_index()

    cond = (df_compare['action'] == '매도') & (df_compare['action'].shift(1) == '매수')
    # df_compare['real_sell'] = np.where(cond,'매도', '')
    # reset_index 를 통해 index 를 초기화함.
    df_sell = df_compare[cond].reset_index()

    # axis = 1 : 가로로 뭍음
    df_result = pd.concat([df_buy, df_sell], axis=1)
    df_result.columns = ['날짜(buy)','종가(buy)','이평값(buy)', 'ma_shift','액션(buy)','날짜(sell)','종가(sell)','이평값(sell)', 'ma_shift','액션(sell)']

    df_result = df_result[['날짜(buy)','종가(buy)','이평값(buy)','액션(buy)','날짜(sell)','종가(sell)','이평값(sell)','액션(sell)']]
    df_result['수익률'] = df_result['종가(sell)']/df_result['종가(buy)']

    df_result['누적곱'] = df_result[['수익률']].cumprod()
    # 마지막은 아직 모름
    return df_result[['누적곱']].iloc[-2, -1]-1