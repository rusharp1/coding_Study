# 남녀 평균 급여 차이가 가장 안나는 회사를 찾아보기.

import dart_fss as dart_fss
import pandas as pd
import matplotlib.pyplot as plt
def salary_info(corp_name):
    # 코드정보 가져오기
    corp_code = df_listed[df_listed['corp_name'] == corp_name].iloc[0,0]
    data = dart_fss.api.info.emp_sttus(corp_code, '2021', '11011', api_key=None)['list']
    df = pd.DataFrame(data)
    # 회사명, 성별, 연봉으로 정제하기
    df = df[['corp_name', 'sexdstn','jan_salary_am' ]]
    # 결과를 원하는 타입으로 DICT 타입으로 수정
    result[key[0]].append(corp_name)
    # 남자인 연봉의 마지막 값
    result[key[1]].append(df[df['sexdstn'] == '남'].iloc[-1,-1])
    # 여자의 연봉의 마지막 값
    result[key[2]].append(df[df['sexdstn'] == '여'].iloc[-1,-1])

api_key = '96223be2acd5a167991115ba3c80e66a18cb44c1'
dart_fss.set_api_key(api_key=api_key)
# 전체 회사 정보를 가져옴
all = dart_fss.api.filings.get_corp_code()
# 위 정보를 pandas 를 통해 dataframe화 함.
df_all = pd.DataFrame(all)
# 상장한 회사 목록 가져옴
df_listed = df_all[df_all['stock_code'].notnull()]

# 원하는 스타일로 정제함
result = {'기업명':[], '연봉(남)':[] , '연봉(여)':[]}
key = list(result.keys())

# 10개의 샘플 회사명 가져옴.
names = list(df_listed.sample(10)['corp_name'])
for corp_name in names:
    try:
        salary_info(corp_name)
    except:
        print(f"errop - {corp_name}")

df_result = pd.DataFrame(result)
for i in range(1,3):
    df_result[key[i]] = df_result[key[i]].str.replace(',','')
    df_result[key[i]] = pd.to_numeric(df_result[key[i]].str.replace('-',''))

df_result['차이(남-여)'] = df_result['연봉(남)'] - df_result['연봉(여)']
df_result['평균'] = df_result[['연봉(남)', '연봉(여)']].mean(axis=1)

print(df_result.sort_values(by='차이(남-여)', key=lambda x: abs(x),ascending=True))




from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override()

import numpy as np
import pandas as pd

import FinanceDataReader as fdr

df = fdr.DataReader('005930','2018')

df.head()