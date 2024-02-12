# https://dart-fss.readthedocs.io/en/latest/

import dart_fss as dart_fss
import pandas as pd
import matplotlib.pyplot as plt

api_key = '96223be2acd5a167991115ba3c80e66a18cb44c1'
dart_fss.set_api_key(api_key=api_key)
# 전체 회사 목록을 출력
corp_list = dart_fss.get_corp_list()
corp_list.corps

# DART에 등록되어있는 공시대상회사의 고유번호,회사명,대표자명,종목코드, 최근변경일자 다운로드
all = dart_fss.api.filings.get_corp_code()
# 위 정보를 pandas 를 통해 dataframe화 함.
df = pd.DataFrame(all)

# df 에서 stock_code 가 null 이 아닌 목록만 가져옴 (상장주식).
df_stock = df[df['stock_code'].notnull()]
# df 에서 stock_code 가 null인 목록만 가져옴 (비상장주식).
df_none_stock= df[df['stock_code'].isnull()]

# 해당 목록을 excel로 다운로드 함.
df_stock.to_excel('상장종목.xlsx')
df_stock.to_excel('비상장종목.xlsx')

# 특정 회사의 corp_code 찾음
corp_code = df_stock[df_stock['corp_name']=='엔에이치엔'].iloc[0,0]
# 공시정보 찾음
dart_fss.api.filings.get_corp_info(corp_code)
for i in range(len(df_stock)): 
    corp_name = df_stock.iloc[i,1]
    if(('NHN' in corp_name) or ('엔에이치엔' in corp_name)):
        print(corp_name)


# 미등기임원 보수현황 찾기 
# 1분기보고서 : 11013
# 반기보고서 : 110123
# 분기보고서 : 11014
# 사업보고서 : 11011
data = dart_fss.api.info.unrst_exctv_mendng_sttus(corp_code, '2022', '11011')
# 미등기임원 보수현황을 DataFrame으로 노출
pd.DataFrame(data['list'])

# 증자 현황 찾기
dart_fss.api.info.irds_sttus(corp_code, '2022', '11011')
# 배당 현황 보기
dart_fss.api.info.alot_matter(corp_code, '2022', '11011')

# 최대 주주 현황
data = dart_fss.api.info.hyslr_sttus(corp_code, '2022', '11011')
# 이중에서 필요한 자료만 출력
pd.DataFrame(data['list'])[['nm', 'bsis_posesn_stock_qota_rt', 'trmend_posesn_stock_qota_rt']]

# 직원 현황
data =dart_fss.api.info.emp_sttus(corp_code, '2022', '11011')
pd.DataFrame(data['list'])[['sexdstn', 'rgllbr_co', 'jan_salary_am']]
df.head()
df.set_index('Symbol',inplace=True)
df.plot(kind='bar')
plt.show()