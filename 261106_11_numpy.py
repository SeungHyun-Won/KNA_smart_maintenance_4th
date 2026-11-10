# import numpy as np

# F = 'data/11_diecasting_series_20_261105_1.csv'

# def col(c):
#     return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

# # 실습 3
# cyl = col(2)
# cyl[0] = 9999
# mean_9999 = np.mean(cyl)
# fixed = np.clip(cyl, 100, 300)
# print(f"보정 전 평균은 {round(mean_9999, 1)}, 보정 뒤에는 {round(np.mean(fixed), 1)}")

# # where
# vib = np.array([2.1, 3.5, 2.0, 6.2])
# label = np.where(vib >= 5, 2, np.where(vib >= 3, 1, 0)) ### 5이상 먼저 점검
# print(label) ### [0 1 0 2]

# # unique
# status = np.array([0, 0, 1, 0, 2, 1, 0])
# kinds, counts = np.unique(status, return_counts=True)
# print(kinds) ### 값의 종류 [0, 1, 2]
# print(counts) ### 종류별 갯수 [4, 2, 1]

# # 실습 4
# cyl = col(1)
# label = np.where(cyl >= 1000, 2, np.where(cyl >= 50, 1, 0))
# kinds, counts = np.unique(label, return_counts=True)
# print(kinds, counts)
# print(counts / len(label))

# # 실습 5
# time, cyl, press, shp = col(1), col(2), col(3), col(4) ### >>> (50,)의 1차원 배열 형태로 뽑아옴 >>> 50행1열((50, 1))의 형태가 아니라
# t = np.stack([time, cyl, press, shp])
# print(np.shape(t))
# recent = t[:, -10:]
# print(np.shape(recent))

# # 실습 6
# num = col(0)
# cyl = col(1)
# syl_p = col(2)
# max_t = np.argmax(cyl)
# max_v = cyl[max_t]
# print(f"최대값: {int(num[max_t])}번에서 {max_v}")
# max_diff = np.diff(cyl)
# max_diff_abs = np.abs(max_diff)
# max_diff_t = np.argmax(max_diff_abs)
# print(f"최대 변화 시점: {int(num[max_diff_t])}번 >> {int(num[max_diff_t + 1])}번")

# a = np.where((cyl >= 50) | (syl_p < 150), 1, 0)
# b, c = np.unique(a, return_counts=True)
# # print(a, '\n')
# # print(b, c)
# percent = c / len(a)
# print(f"사이클타임 50이상, 실린더압력 150아래 경고비율: {percent[1]}")

# top3 = np.argsort(cyl)[-3 : ]
# print(f"사이클타임 상위 3지점: {num[top3]}")

# # 실습 6 >> 강사님 코드
# cyc, ct, cyl = col(0), col(1), col(2)

# i = ct.argmax()
# print(int(cyc[i]), ct[i])

# ch = np.abs(np.diff(ct))
# j = ch.argmax()
# print(int(cyc[j]), int(cyc[j+1]))

# warn = np.where((ct >= 50) | (cyl < 150), 1, 0)
# print(round(warn.mean(), 2))

# top = np.argsort(ct)[::-1][:3]
# print(top)      # [49 47 42]  -> 인덱스
# print(cyc[top])   # [50. 48. 43.]


import numpy as np

# # isnan >> 결측값 위치 찾기
# # 결측값: 값이 빈 칸 >> 0이 아니라 값이 없음

# x = np.array([2.0, np.nan, 4.0])
# print(np.isnan(x))   #[False  True False]
# print(np.isnan(x).sum())   # 1

# 실습 1

F = "data/11_hydraulic_cooler_20_261105_2.csv"
def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

# vib = col(2)
# x = np.isnan(vib).sum()
# y = np.isnan(vib).mean()
# print("결측 개수:", x,"결측 비율:", y)
# print("결측 제외 평균:",round(float(np.nanmean(vib)), 3), "/", "일반 평균:", np.mean(vib))


# # percentile
# vib_s = np.array([2.0, 2.2, 2.5, 2.8, 3.0, 6.5])
# print(np.round(float(np.percentile(vib_s, 25)), 2))
# print(np.round(float(np.percentile(vib_s, 75)), 2))

# # 여러개 한번에
# print(np.round(np.percentile(vib_s, [25, 50, 75]), 2))

# # quantile >> 25가 0.25가 된거임 걍 같음
# print(np.round(np.quantile(vib_s, [0.25, 0.50, 0.75]), 2))

# # 사분위 기반 이상치 범위 >> IQR
# q1, q3 = np.percentile(vib_s, [25, 75])
# iqr = q3 - q1
# upper = q3 + 1.5 * iqr
# print(vib_s[vib_s > upper])

# # 평균 / 표준편차로 정규화 >> z-score
# # 부호 >> 양수: 평균보다 큼, 음수: 평균보다 작음
# z = (vib_s - np.mean(vib_s)) / np.std(vib_s)
# print(vib_s[np.abs(z) > 2])

# # 실습 2
# temp = col(1)
# temp_q1, temp_q3 = np.percentile(temp, [25, 75])
# iqr = np.abs(temp_q3 - temp_q1)
# upper = temp_q3 + iqr * 1.5
# print(f"상한 {round(upper, 1)}, 이상치: {np.round(temp[temp > upper], 1)} >> {np.sum(temp > upper)}건")

# # 실습 3
# cyc, temp = col(0), col(1)
# z = (temp - np.mean(temp)) / np.std(temp)
# z_ov2 = z[np.abs(z) > 2]
# # print(z, '\n', z_ov2)
# print(f"z값 2넘은 사이클: {cyc[np.abs(z) > 2]}, 최대 z-score: {round(np.max(z_ov2), 2)}")