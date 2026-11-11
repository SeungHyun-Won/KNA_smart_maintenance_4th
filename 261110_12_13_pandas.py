import pandas as pd
import numpy as np

# F = 'data/12_metro_compressor_22_261109_1.csv'
# FD = 'data/12_metro_digital_22_261109_3.csv'

# # 실습 1
# df = pd.read_csv(F)
# print(f"{df.head()}\n\n{df.tail()}")
# print()
# print(f"{df.head(3)}\n\n{df.tail(3)}")

# # 열 이름 목록
# # - df.columns >> 인덱스 형태로 출력
# # - df.columns.tolist() >> 목록으로 보기좋게
# print(df.columns)
# print(df.columns.tolist())

# # 행 번호표
# # - df.index
# print(df.index)   # RangeIndex(start=0, stop=200, step=1) >> 0부터 199까지 1씩 증가

# # 테이터 자료형 형태  바꾸기
# df2 = pd.read_csv(FD)
# print(df2.dtypes)
# d = pd.read_csv('data/12_metro_digital_22_261109_3.csv',dtype={'압축기': str}) # >> 0,1은 상태를 나타내므로 str처리

# # 실습 2
# print(df2.shape)
# print(df2.columns.tolist())
# print(df2.dtypes)
# print(df2.head())

# # 실습 3
# print(df.info())
# # <class 'pandas.DataFrame'>
# # RangeIndex: 200 entries, 0 to 199 >>     행
# # Data columns (total 7 columns):     >> 열
# #  #   Column  Non-Null Count  Dtype  
# # ---  ------  --------------  -----  
# #  0   측정시각    200 non-null    str    
# #  1   압축압력    200 non-null    float64
# #  2   배출압력    200 non-null    float64
# #  3   저장압력    200 non-null    float64
# #  4   오일온도    199 non-null    float64     >> nan값 한개 있음을 확인
# #  5   모터전류    200 non-null    float64
# #  6   가동상태    200 non-null    str    
# # dtypes: float64(5), str(2)
# # memory usage: 11.1 KB
# # None

# # 실습 4
# print(round(df.describe(), 2)) ## = print(df.describe().round(2))
# state = df['가동상태'].values
# cur = df['모터전류'].values
# print(f"가동: {round(float(np.mean(cur[state == '가동'])), 2)}, 정지: {round(float(np.mean(cur[state == '정지'])), 2)}")

# # 실습 5
# df = pd.read_csv(F)
# df2 = pd.read_csv(FD)
# print(df.shape, df2.shape)
# print()
# print(f"{df.dtypes} \n\n{df2.dtypes}")

# # 실습 6
# FS = "data/12_metro_small_22_261109_4.csv"
# dfs = pd.read_csv(FS)
# print(dfs.head())
# print(dfs.shape)
# print(dfs.info())

# miss = len(dfs) - dfs["오일온도"].count()

# print(dfs.describe())
# print()
# print(f"{dfs.shape[0]}행 {dfs.shape[1]}열, 결측 {miss}건, 모터전류 >> 평균 "
#       f"{dfs["모터전류"].mean():.2f} vs 중앙값 {dfs["모터전류"].median():.2f}")

# # 실습 6 다르게 짠 코드
# df = pd.read_csv(FS)
# print(df.head(3))
# print('크기:', df.shape)
# print(df.info())

# stats = df.describe()

# miss = int(df["오일온도"].isna().sum())
# print('오일온도 결측:', miss, '건')

# mean_current = round(float(stats["모터전류"]["mean"]), 2)
# median_current = round(float(stats["모터전류"]["50%"]), 2)
# print("모터전류 평균/중앙값:", mean_current, median_current)

##############################################################################################
########################################### 12 끝 ############################################
##############################################################################################

import pandas as pd
import numpy as np

F_SMALL = 'data/13_diecasting_small_24_261110_3.csv'
F_SHOT = 'data/13_diecasting_shot_24_261110_2.csv'

# # 열 골라내기
# df = pd.read_csv(F_SMALL)
# # print("이름으로 앞 3개:", df["실린더압력"].head(3).tolist())

# # # 단일 열 선택
# # # - df["실린더압력"]
# # print(df["실린더압력"])

# # 실습 1
# print(df["실린더압력"].head(3).tolist())
# t = df[["실린더압력", "형체력"]]
# print(type(t), t.shape)
# print(type(df[["형체력"]]))


# 행 선택
# - 라벨과 위치 번호의 차이
# - 라벨: 그 행에 붙은 이름표 = 인덱스 값
# - 위치 번호: 맨 위에서부터 몇 번째인지, 항상 0부터

# sorted = df.sort_values("형체력", ascending=False)

# print("정렬 후 인덱스 앞 4개:", sorted.index[:4].tolist())    # 정렬 후 인덱스 앞 4개: [22, 17, 27, 12]
# print("정렬 후 iloc[0] 샷:", int(sorted.iloc[0]['샷']))     # 정렬 후 iloc[0] 샷: 23
# print("정렬 후 loc[0] 샷:", int(sorted.loc[0, '샷']))       # 정렬 후 loc[0] 샷: 1

# # 여러 행 선택
# print(df.loc[0:4].shape)    # (5, 8)
# print(df.iloc[0:4].shape)   # (4, 8)


# # 행, 열 동시 선택
# # df.loc[행, 열] -> 열이름 사용 가능 
# # df.iloc[행, 열] -> 열이름 사용 불가 >> 숫자로 접근
# print(df.loc[0:4, ["실린더압력", "형체력"]].shape)
# print(df.iloc[0:5, [2, 6]].shape)

# # 실습 2
# df = pd.read_csv(F_SMALL)
# print(df.loc[0, "샷"], df.iloc[0]["샷"])
# s = df.sort_values("형체력", ascending=False)
# print(s.loc[0, "샷"], s.iloc[0]["샷"]) 

# # 실습 3
# print(list(df.columns))
# a = df.loc[0:4, ["실린더압력", "형체력"]]
# b = df.iloc[0:5, [2, 6]]
# print(a.shape, b.shape, a.equals(b))

# 실습 4
log = pd.read_csv(F_SHOT)
print(log.shape)
print(list(log.columns))
front = log.loc[0:9, ["설비ID", "비스킷두께", "품질등급"]]
print(front.shape)
print(front.head(3))
print(log.iloc[-5:])