# import numpy as np
# F = 'data/11_hydraulic_cooler_20_261105_2.csv'
# def col(c):
#     return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

# # 실습 4
# cyc, temp = col(0), col(1)
# m, s = np.nanmean(temp), np.nanstd(temp)
# upper = m + 3 * s
# print(temp[temp > upper])
# print(f"상한 {round(upper, 2)}에 걸리는 사이클: {cyc[temp > upper]}")

# # 실습 5
# temp, ceff = col(1), col(3)
# a = round(np.corrcoef(temp, ceff)[0, 1], 2)   ### >> (temp, temp), (temp, ceff), (ceff, temp), (ceff, ceff) 이렇게 
#                                               ###    2x2행렬형태로 corrcoef값이 나옴. >> [0, 1]이 그 값중 필요한 비교군 선택한거임.
# print(f"{a} >> 온도가 오르면 거의 정확히 냉각효율 감소")

# # 실습 6
# temp, vib, ceff, cpw = col(1), col(2), col(3), col(4)
# a = np.stack([temp, vib, ceff, cpw])
# print(a.shape)
# print(np.round(np.nanmean(a, axis = 1), 1))
# print(np.round(np.nanstd(a, axis = 1), 1))

# # 실습 7
# cyc, temp = col(0), col(1)
# cs = np.cumsum(temp - np.nanmean(temp))
# a = cyc[np.argmin(cs)]
# print(f"{int(a)}번 사이클 뒤({int(a)} ~ {int(a+1)}번 사이)가 경계 후보 / {int(a+2)}번은 경보 초과 시작")

# # 실습 8
# cyc, temp, ceff, stat = col(0), col(1), col(3), col(5)
# t = np.abs(np.round((temp - np.nanmean(temp)) / np.nanstd(temp), 2))
# ce = np.abs(np.round((ceff - np.nanmean(ceff)) / np.nanstd(ceff), 2))
# score = t + ce
# top = np.nanargmax(score)
# top_3 = np.argsort(score)[: : -1][0 : 3]
# print(f"최고 점수: {cyc[top]}번({top}), 상위 세 지점 {cyc[top_3].astype(int)}")


##############################################################################################
########################################### 11 끝 ############################################
##############################################################################################

import numpy as np
import pandas as pd

# Pandas
# - 표 형태의 데이터를 잘 다루기 위해
# - Series: 하나의 열들
# - DataFrame: Series가 모여서 합쳐진 표 형태의 데이터 구조(df)

# 앞 단원 방식 -> 숫자 열만 골라야 함.
# Pandas 방식 -> 글자 열까지 그대로, 열은 이름으로

F = 'data/12_metro_compressor_22_261109_1.csv'

df = pd.read_csv(F)
# print("데이터 크기:", df.shape) # 데이터 크기: (200, 7)
# # print(df.head())
# print("열 이름:", df.columns.to_list())
# # 열 이름: ['측정시각', '압축압력', '배출압력', '저장압력', '오일온도', '모터전류', '가동상태']
# print(df.dtypes)

# state = df["가동상태"].values
# print("가동상태 종류:", np.unique(state, return_counts=True))
# #가동상태 종류: (array(['가동', '정지'], dtype=object), array([ 96, 104]))

# cur = df["모터전류"].values
# print("모터 전류 평균 %.2f / 가운데 값 %.2f" % (np.mean(cur), np.median(cur)))
# # 모터 전류 평균 2.06 / 가운데 값 0.04

# s = df["오일온도"]
# print(s.head(3))
# # 0    51.3
# # 1    56.8
# # 2    55.7
# # Name: 오일온도, dtype: float64

# # Pandas - 열 이름
# # 여러 열 불러오기
# new = pd.read_csv(F, usecols=["오일온도", "모터전류"])
# print(new.shape)
# # 행 수 제한하는 설정
# print(pd.read_csv(F, nrows=10).shape)
# # read_csv 옵션
# # - usecols, nrows, encoding, sep(구분자)

# # 실습 2
# df = pd.read_csv(F)
# a = pd.read_csv(F, usecols=["측정시각", "오일온도", "모터전류"])
# print(a.shape)
# print(pd.read_csv(F, nrows=20).shape)

# 실습 3
df_sep = pd.read_csv(F, sep = ";", encoding="utf-8")
print(df)
print(df_sep)
print("열 이름:", df_sep.columns.to_list())

# 실습 4
F_semi = "data/12_metro_compressor_semicolon_22_261109_2.csv"
df = pd.read_csv(F_semi, sep=";", encoding="utf-8", usecols=["측정시각", "오일온도", "모터전류"], nrows=50)
print(df.shape)                                         # ⑤
print(df.head(3))