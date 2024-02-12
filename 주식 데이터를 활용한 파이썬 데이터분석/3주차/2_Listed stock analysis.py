import dart_fss as dart_fss
import pandas as pd
import matplotlib.pyplot as plt

# 해당 회사의 정기보고서(사업, 분기, 반기보고서) 내에 개인별 보수지급 금액(5억이상 상위5인) 가져오기
def get_salary(corp_name, bsns_year, reprt_code):
    # 회사명이 `카카오` 이면서 `상장된 회사` 를 찾음.
    cond = (df_listed['corp_name']==corp_name)&(df_listed['stock_code'].notnull())
    corp_code = df_listed[cond].iloc[0,0]
    data = dart_fss.api.info.indvdl_by_pay(corp_code, bsns_year, reprt_code, api_key=None)
    df = pd.DataFrame(data['list'])
    df = df[['corp_name','nm','ofcps','mendng_totamt']]
    df.columns = ['기업명', '이름', '역할', '보수']
    # 보수 내 컴마 제거
    df['보수'] = df['보수'].str.replace(',','')
    # 보수를 숫자로 변경함.
    df['보수'] = pd.to_numeric(df['보수'])
    # 보수의 타입 출력
    df.dtypes
    # 오름차순으로 변경
    return df

# 최대 주주의 주식 변동 모아보기
def get_shareholders(corp_name, bsns_year, reprt_code):
    cond = (df_listed['corp_name']==corp_name)&(df_listed['stock_code'].notnull())
    corp_code = df_listed[cond].iloc[0,0]
    data = dart_fss.api.info.hyslr_sttus(corp_code, bsns_year, reprt_code, api_key=None)
    df = pd.DataFrame(data['list'])
    df = df[['corp_name', 'nm', 'relate', 'bsis_posesn_stock_qota_rt', 'trmend_posesn_stock_qota_rt', 'nm']]
    df.columns = ['기업명', '이름', '관계', '기초지분율', '기말지분율', '비고']
    # 관계가 null이 아닌 행만 뽑아옴
    df = df[df['관계'].notnull()]
    # 기초지분율, 기말지분율을 숫자 타입으로 변경
    df['기초지분율'] = pd.to_numeric(df['기초지분율'])
    df['기말지분율'] = pd.to_numeric(df['기말지분율'])
    # 기초지분율을 정렬 후 top3 선택
    return df.sort_values(by='기초지분율', ascending=False).head(3)

# 돈을 가장 많이 번 회사 확인하기
def get_profit(corp_name, bsns_year, reprt_code):
    corp_code = df_listed[df_listed['corp_name'] == corp_name].iloc[0,0]
    data = dart_fss.api.finance.fnltt_singl_acnt(corp_code, '2021', '11011')
    df = pd.DataFrame(data['list'])
    cond = (df['fs_div']== 'CFS')&(df['account_nm']=='이익잉여금')
    df = df[cond]
    df['name']=corp_name
    df = df[['name','thstrm_amount','frmtrm_amount']]
    df.columns = ['기업명','당기','전기' ]
    df['당기'] = pd.to_numeric(df['당기'].str.replace(',',''))
    df['전기'] = pd.to_numeric(df['전기'].str.replace(',',''))
    df['증감'] = df['당기']-df['전기']
    # 절대값
    df['증감율'] = abs(df['증감']/df['전기'])
    return df

api_key = '96223be2acd5a167991115ba3c80e66a18cb44c1'
dart_fss.set_api_key(api_key=api_key)
# 전체 회사 정보를 가져옴
all = dart_fss.api.filings.get_corp_code()
# 위 정보를 pandas 를 통해 dataframe화 함.
df_all = pd.DataFrame(all)

df_listed = df_all[df_all['stock_code'].notnull()]
# 사업연도(4자리) ※ 2015년 이후 부터 정보제공
bsns_year = '2021'
# 1분기보고서 : 11013반기보고서 : 110123분기보고서 : 11014사업보고서 : 11011
reprt_code = '11011'

### 연봉왕 뽑아보기
names = ['삼성전자','LG에너지솔루션','SK하이닉스','NAVER','삼성바이오로직스','삼성전자우',
         '카카오','삼성SDI','현대차','LG화학','기아','POSCO홀딩스', 'KB금융','카카오뱅크',
         '셀트리온','신한지주','삼성물산','현대모비스','SK이노베이션','LG전자','카카오페이',
         'SK','한국전력','크래프톤','하나금융지주','LG생활건강','HMM','삼성생명','하이브',
         '두산중공업','SK텔레콤','삼성전기','SK바이오사이언스','LG','S-Oil','고려아연',
         'KT&G','우리금융지주','대한항공','삼성에스디에스','현대중공업','엔씨소프트','삼성화재',
         '아모레퍼시픽','KT','포스코케미칼','넷마블','SK아이이테크놀로지','LG이노텍','기업은행']

# https://pandas.pydata.org/docs/user_guide/merging.html#concat
dfs = []
for name in names:
    try:
        df = get_salary(name, bsns_year, reprt_code)
        dfs.append(df)
    except:
        print(f'error-{name}')

result = pd.concat(dfs)
result.sort_values(by='보수', ascending=False)
print(result.sort_values(by='보수', ascending=False))
print("------------------------------------------------------------------------------------------------------------")

### 최대 주주의 주식 변동 모아보기

# corp_code를 불러오기(sample 10가지만)
corp_names = list(df_listed.sample(10)['corp_name'])
dfs = []
for corp_name in corp_names:
    try:
        df = get_shareholders(corp_name,  bsns_year, reprt_code)
        dfs.append(df)
    except:
        print(f'error - {corp_name}')
df_result = pd.concat(dfs)
df_result['증감']= df_result['기초지분율'] - df_result['기말지분율']
df_result.sort_values(by='증감', ascending=False)
print(df_result.sort_values(by='증감', ascending=False))
print("------------------------------------------------------------------------------------------------------------")
### 돈 많이 번 회사’를 찾기
dfs = []
for corp_name in corp_names:
    try:
        df = get_profit(corp_name,  bsns_year, reprt_code)
        dfs.append(df)
    except:
        print(f'error - {corp_name}')
df_result = pd.concat(dfs)
df_result.sort_values(by='증감율', ascending=False)
print(df_result.sort_values(by='증감율', ascending=False))


