from n3_moving_average import *

dfs = []
for shrt in range(3,11):
    for lng in range(30,61):
        df = get_return_sl('005930', shrt, lng)
        dfs.append(df)
df_result = pd.concat(dfs)
print(df_result.sort_values(by = '누적곱', ascending=False))