import dart_fss as dart_fss
import pandas as pd
import matplotlib.pyplot as plt

def get_earning(corp_name):
    # 정기보고서(사업, 분기, 반기보고서) 내에 배당에 관한 사항을 제공합니다.
    # 당기 순이익을 출력합니다.
    corp_code = df_unlisted[df_unlisted['corp_name'] == corp_name].iloc[0,0]
    data = dart_fss.api.info.alot_matter(corp_code, '2021', '11011')
    df = pd.DataFrame(data['list'])
    df = df[df['se']=='(연결)당기순이익(백만원)']
    df = df[['corp_name', 'thstrm','frmtrm', 'lwfr']]
    df.columns = ['기업명', 2021, 2020, 2019]
    for i in range(2019, 2022):
        df[i] = pd.to_numeric(df[i].str.replace(',',''))
    return df

api_key = '96223be2acd5a167991115ba3c80e66a18cb44c1'
dart_fss.set_api_key(api_key=api_key)
# 전체 회사 정보를 가져옴
all = dart_fss.api.filings.get_corp_code()
# 위 정보를 pandas 를 통해 dataframe화 함.
df_all = pd.DataFrame(all)

df_unlisted = df_all[df_all['stock_code'].isnull()]
# 사업연도(4자리) ※ 2015년 이후 부터 정보제공
bsns_year = '2021'
# 1분기보고서 : 11013반기보고서 : 110123분기보고서 : 11014사업보고서 : 11011
reprt_code = '11011'

### 비상장 종목 분석하기

dfs = []
names = list(df_unlisted.sample(1000)['corp_name'])
for name in names:
    try:
        df = get_earning(name)
        dfs.append(df)
    except:
        print(f"error-{name}")
df_result = pd.concat(dfs)
print(df_result)