import pandas as pd
import numpy as np

F = 'data/14_hydraulic_26_261112_1.csv'
F_QC = 'data/14_hydraulic_qc_26_261112_2.csv'

# 그룹 통계와 상관관계
# - 그룹 통계 >> 원본 행과 그룹 기준 비교 >> 두 기준 표 >> 상관관계

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

# print(round(df['온도'].mean(), 2))
# print(round(df['온도'].std(), 2))

# print(df.groupby("냉각기상태")["온도"].mean().round(2))
# print(df.groupby("냉각기상태")["온도"].std().round(2))

# # 분산 / 표준편차
# v = df.groupby("냉각기상태")["온도"].var()
# std = df.groupby("냉각기상태")["온도"].std()
# print(v.round(2))
# print(std.round(2))
# print((std ** 2).round(2))

# agg - 여러 통계 한번에 표로 모으기
#  ㄴ 리스트: 같은 대상에 여러 통계
#  ㄴ 딕셔너리: 열별 통계
#  ㄴ named aggregation: 결과 열의 이름까지 지정

# print(df.groupby("냉각기상태")["온도"].agg(['mean', "std", "max"]).round(2)) ### 리스트: 같은 대상에 여러 통계
# print(df.groupby("냉각기상태")[["온도", "진동"]].agg(['mean', "std", "max"]).round(2))

# # 이름 붙이기
# summary = df.groupby("냉각기상태").agg(
#     평균온도=("온도", "mean"),
#     평균진동=("진동", "mean")
# )
# print(summary)
#          평균온도      평균진동
# 냉각기상태                   
# 고장     54.6675  0.688125
# 저하     45.4650  0.610125
# 정상     35.8850  0.548650

# # 열별로 다른 통계 목록 지정
# summary2 = df.groupby("냉각기상태").agg({
#     "온도": ["mean", "std"],
#     "진동": ["mean", "max"]
# })
# print(summary2.round(2))
#          온도          진동      
#         mean   std  mean   max
# 냉각기상태                         
# 고장     54.67  3.76  0.69  0.78
# 저하     45.46  1.47  0.61  0.63
# 정상     35.89  0.36  0.55  0.57

# # 실습 1
# print(qc["검사결과"].value_counts().to_dict())
# print(qc.groupby("검사결과")["온도"].agg(['mean', "std", "max"]).round(3))
# summary = qc.groupby("검사결과").agg(
#     평균온도=("온도", "mean"), 
#     평균냉각효율=("냉각효율", "mean"), 
#     측정수=("온도", "size")
# )
# print(summary.round(3))



# transform - 그룹 통계를 원래 행에 붙이기
# - 원래 행 인덱스와 모양을 유지한다

# # 같은 그룹의 평균 붙이기
# print(df.groupby("냉각기상태")["온도"].mean())
# # 냉각기상태
# # 고장    54.6675
# # 저하    45.4650
# # 정상    35.8850
# # Name: 온도, dtype: float64
# print(df.groupby("냉각기상태")["온도"].transform("mean"))
# # 0      54.6675
# # 1      54.6675
# # 2      54.6675
# # 3      54.6675
# # 4      54.6675
# #         ...   
# # 115    35.8850
# # 116    35.8850
# # 117    35.8850
# # 118    35.8850
# # 119    35.8850
# # Name: 온도, Length: 120, dtype: float64

# marked = df.copy()
# marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")
# marked["편차"] = marked["온도"] - marked["그룹평균"]
# print(marked[["냉각기상태", "온도", "그룹평균", "편차"]].head(3).round(2))
# #   냉각기상태    온도   그룹평균     편차
# # 0    고장  35.6  54.67 -19.07
# # 1    고장  47.5  54.67  -7.17
# # 2    고장  50.7  54.67  -3.97



# pivot_table - 두 기준 표를 한 번에 
# - margins=True >> 전체 집계 추가
# - 값이 없는 조합의 평균을 0으로 메우지 않도록

# temp_table = pd.pivot_table(df, index="밸브상태", columns="운전부하", values="온도",
#                             aggfunc="mean", margins=True, margins_name="전체")
# # - index : 결과표의 행을 나누는 기준
# # - columns : 결과표의 열을 나누는 기준
# # - values : 각 칸에서 계산할 측정값
# # - aggfunc="mean" : 그 측정값을 평균으로 요약
# # - margins=True : 전체 집계 행, 열 추가
# # - margins_name : 추가 집계 이름 표시

# print(temp_table.round(2))
# # 운전부하    고부하    저부하     전체
# # 밸브상태                     
# # 경미    42.20  47.52  44.86
# # 심각    45.25  47.09  46.02
# # 정상    39.34  49.40  45.11
# # 지연    43.75  49.79  45.86
# # 전체    41.85  48.82  45.34

# # 실습 2
# copy = df.copy()
# copy["그룹평균온도"] = copy.groupby("냉각기상태")["온도"].transform("mean")
# copy["편차"] = copy["온도"] - copy["그룹평균온도"]
# print(copy[["냉각기상태", "온도", "그룹평균온도", "편차"]].head(3).round(3))
# print()

# copy["거리"] = copy["편차"].abs()
# furthest = copy.sort_values("거리", ascending=False).head(1)
# print(furthest[["냉각기상태", "온도", "그룹평균온도", "편차"]].round(2))
# #   냉각기상태    온도  그룹평균온도     편차
# # 0    고장  35.6   54.67 -19.07

# print(copy.groupby("냉각기상태")["편차"].sum().round(10))

# # far = copy["편차"].abs().idxmax()
# # print(far, copy.loc[far, "냉각기상태"], round(copy.loc[far, "편차"], 2))
# print()

# temp_table = pd.pivot_table(df, index="밸브상태", columns="운전부하", values="온도", 
#                             aggfunc="mean", margins=True, margins_name="전체")
# print(temp_table.round(3))


# # corr - 두 지표의 상관계수 구하기
# print(round(df["온도"].corr(df["진동"]), 3))
# print(round(df["온도"].corr(df["냉각효율"]), 3))
# print(round(df["온도"].corr(df["압력"]), 3))

# # 실습 3
# print("온도와 진동의 상관계수:", round(df["온도"].corr(df["진동"]), 3))
# print("온도와 압력의 상관계수:", round(df["온도"].corr(df["압력"]), 3))
# print("온도와 냉각효율의 상관계수:", round(df["온도"].corr(df["냉각효율"]), 3))
# print()
# t = ["온도", "진동", "압력", "냉각효율"]
# t_table = df[t].corr()
# print(round(t_table, 3))
# t_abs = t_table.abs()

# s = t_abs[t_abs < 1].stack()
# # t_abs < 1 >> 같은 4 x 4 행렬에  True, False값이 들어간 행렬
# # t_abs[t_abs < 1 >> t_abs < 1 행렬에 True엔 원래 값이, False엔 NaN이 들어간 4 x 4 행렬
# # stack() >> 0번 열 아래로 1번 열 내리고 2번 열 내리고 ... >> 1열로 행렬을 편다.
# print(round(s.max(), 3), s.idxmax())
# print(round(s.min(), 3), s.idxmin())
# # .max() >>> 가장 큰 값
# # .idxmax() >>> 가장 큰 값의 이름(인덱스) >>> a, b = s.idxmax() >>> a = "온도", b = "냉각효율"

# 실습 4
sensor_cols = qc.select_dtypes(include="number").columns.tolist()
table = qc[sensor_cols].corr()
copy = table.copy()
n = len(sensor_cols)
for i in range(n):
    for j in range(n):
        if j <= i:
            copy.iloc[i, j] = np.nan

print(copy.round(3))
p = copy.stack().dropna()
s = p.abs()
print(len(p), (s >= 0.4).sum(), (s >= 0.95).sum())
print()
top = s[s >= 0.95].sort_values(ascending=False).head(5).index
print(p[top].round(3))




# 15단원
import pandas as pd

F_PROC = "data/15_사출성형_공정_28_261113_1.csv"
F_LOG = "data/15_사출성형_로그_28_261113_2.csv"

df = pd.read_csv(F_PROC)

# # 결측 처리
# # - 종류: NaN, None, NA, NAT
# # ㄴ 표현은 달라도 isna()로 결측 여부 확인 가능

# s = pd.Series([10, None, 20])
# print(s.mean()) ## 15.0 >>> NaN값이 있다고 해서 계산이 멈춘다 X >>> (10 + 20) / 2
# # print(s + 1) 11.0, NaN, 21.0

# 실습 1
df_log = pd.read_csv(F_LOG)
print(df_log.shape)
print(df_log.isna().sum())
print(int(df_log["사출압력"].eq(0).sum()))
print(int(df_log["스크루속도"].eq(-999).sum()))
print(int(df_log["배럴온도"].eq(999).sum()))

# print(df_log.isna().sum().sum()) 
# print((df_log["사출압력"] == 0).sum(), (df_log["스크루속도"] == -999).sum(), (df_log["배럴온도"] == 999).sum())