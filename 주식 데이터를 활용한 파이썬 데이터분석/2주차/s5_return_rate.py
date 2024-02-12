import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import pandas as pd

# 수익률 구하기 함수(일차별)
def make_rate(code):
    df = fdr.DataReader(code,'2017')
    # 원래 금액 : df[['Close']] 중 첫번째 값
    original = df[['Close']].iloc[0]
    df = df[['Close']]/original -1
    return df['Close']

# 최종 수익률 구하기
def Final_rate(code):
    # 최종 수익률을 연산하는 도중 에러가 있으면 -1000 반환.
    try:
        return make_rate(code).iloc[-1]
    except:
        return -1000


if __name__ == "__main__":
    df = pd.DataFrame()
    df['GOOG'] = make_rate('GOOG')
    df.plot()
    plt.show()




