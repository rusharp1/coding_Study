# pip install pandas numpy
import pandas as pd
import numpy as np

data = {'name' : ['heejin', 'youjin', 'hyeneo'],
        'age' : [30, 28, 29]}
# dataprame을 만드는 기초적인 방법.
df = pd.DataFrame(data)
print(df)


### dataprame을 추가하는 방법.

# doc에 [ ] 을 사용하거나, (현재 사용 방법)
# new_df = pd.DataFrame([doc]) 를 써주면 됨.
doc = {'name' : ['yeonsu'],
    'age' : [31] }
new_df = pd.DataFrame(doc)
# 현재는 지원하지 않음
# df = df.append(doc, ignore_index=True) > 리스트 안에 딕셔너리를 담아데이터프레임 생성

# index 를 따로 넣지 않고 4번째로 넣음
# ingnore ~ 부분이 업으면 index가 0으로 나옴
df = pd.concat([df, new_df], ignore_index=True)
print(df)


### df 에 column 추가
df['city'] = ['성남', '청주', '청주', '서울']
print(df)

### df 에 특정 column 만 출력하기
print(df[['name', 'city']])


### 특정 조건만 출력하기 (나이가 30 미만)
cond = df['age'] <30
print(df[cond])


### 마지막 줄 출력
# df 를 행렬화 시켜서 출력함 ('city' 와 같이 쓸 필요 X)
print(df.iloc[-1,0])


### 연산
# age 로 정렬, 내림차순
sorted_df = df.sort_values(by='age',ascending=False)
print(sorted_df)

# df 에 is_adult 탭을 만들음.
# df['age'] 가 20보다 작으면 청소년, 아니면 성인 입력
df['is_adult'] = np.where(df['age']<20, '청소년', '성인')
print(df)

# 나이의 최소/최대/평균 등등  구하기
# min, max, mean, count ....
print(df['age'].describe())

# city 가 청주에 있는 사람들의 평균 나이
cond = df['city'] == '청주'
print(df[cond]['age'].mean())