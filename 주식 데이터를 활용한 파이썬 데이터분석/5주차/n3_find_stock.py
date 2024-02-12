from n2_day import *
import dart_fss as dart_fss
import pandas as pd

api_key = '96223be2acd5a167991115ba3c80e66a18cb44c1'
dart_fss.set_api_key(api_key=api_key)
# DART에 등록되어있는 공시대상회사의 고유번호,회사명,대표자명,종목코드, 최근변경일자 다운로드
all = dart_fss.api.filings.get_corp_code()
df = pd.DataFrame(all)
# 주식상장한 회사만 출력
df_listed = df[df['stock_code'].notnull()]
doc = {
        'name' : [],
        'return' : []
    }
for row in df_listed.sample(10)[['stock_code', 'corp_name']].itertuples():
    try:
        doc['return'].append(get_return_mf(row[1]))
        doc['name'].append(row[2])
    except:
        print("error : ", row[2])

df_result = pd.DataFrame(doc)
print(df_result.sort_values('return', ascending=False))