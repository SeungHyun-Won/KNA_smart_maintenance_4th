import numpy as np

# # 실습 3
# rpm = np.array([4603, 4603, 4603, 1241, 4603, 4603, 3149, 4603, 4987, 4603])
# lo, hi = rpm.min(), rpm.max()
# a = (rpm - lo) / (hi - lo)
# print(np.round(a, 2))

# # 실습 4
# rpm = np.array([2001, 2000, 1789, 3012, 2065, 1876, 1999, 1467])
# current = np.array([21, 24, 26, 33, 35, 32, 18, 34])
# a = rpm < 2000
# b = (rpm < 2000) | (current > 25)
# print(a)
# print(b)
# print("저회전 횟수:", a.sum(), '저회전 또는 고회전 횟수:', b.sum())
# print("저회전 비율:", a.mean(), '저회전 또는 고회전 비율:', b.mean())

# # 실습 5
# torq = np.array([1,2,3,4,19,6,15,8,11,10])
# a = torq > 10
# print(a)
# print("토크 10초과 개수:", a.sum())
# print("토크 10초과 비율:", a.mean())

# # 실습 6
# rpm = np.array([[2001, 2000], [3012, 2065], [1999, 1467]])
# torq = np.array([[1,2],[4,19],[15,8],[10, 11]])
# a = np.round(rpm.mean(axis=0), 2)
# b = np.round(rpm.std(axis=0), 2)
# c = np.round(torq.mean(axis=0), 2)
# d = np.round(torq.std(axis=0), 2)
# print(f"회전수 >> 평균: {a}, 표준편차: {b}")
# print(f"토크 >> 평균: {c}, 표준편차: {d}")

# 실습 7
# rpm = np.loadtxt('data/10_mct_tool_18_261104.csv', 
#                  delimiter=',', 
#                  skiprows=1, 
#                  usecols=4)
# # print(rpm.ndim, rpm.shape, rpm.size, rpm.dtype)
# a = np.round(rpm.mean(), 2)
# b = np.round(rpm.std(), 2)
# c, d = rpm.min(), rpm.max()
# print(f"회전수 >>> 평균값: {a}, 표준편차: {b}, 최소값: {c}, 최대값: {d}")

# # 실습 8
# torq = np.loadtxt('data/10_mct_tool_18_261104.csv', 
#                  delimiter=',', 
#                  skiprows=1, 
#                  usecols=5)
# over10 = torq[torq > 10]
# print(over10)
# print(f"토크(10 초과) >>> 개수: {len(over10)}, 평균: {round(np.mean(over10), 1)}")
# tot_mean = np.mean(torq)
# mean_10 = np.mean(over10)
# print(mean_10 - tot_mean)

# # 실습 9
# data = np.loadtxt('data/10_mct_tool_18_261104.csv',
#                   delimiter=',',
#                   skiprows=1,
#                   usecols=(4, 5))
# rpm = data[:, 0]
# torq = data[:, 1]
# print(data.shape, data.dtype)
# rpm_under_2000 = rpm[rpm < 2000]
# print(f"이상 시점: {len(rpm_under_2000)}, 이상 평균: {rpm_under_2000.mean()}, 전체평균: {round(np.mean(rpm), 1)}")

##############################################################################################
########################################### 10 끝 ############################################
##############################################################################################

import numpy as np

F = 'data/11_diecasting_series_20_261105_1.csv'
# ct = np.genfromtxt(F, delimiter=',', skip_header=1, usecols=1)
# print(ct.shape, ct.dtype)

def col(c):
    return np.genfromtxt(F, delimiter=',', skip_header=1, usecols=c)

# # 자리 찾기
# # fancy indexing
# vib = np.array([2.1, 2.3, 2.0, 5.8])
# pick = np.array([0, 3])
# print(vib[pick])

# # argsort >> 원래있던 자리번호 돌려줌.
# print(np.sort(vib))
# print(np.argsort(vib))

# 실습 1
num, cy_time = col(0), col(1)
hi = np.argmax(cy_time)
print(f"{int(num[hi])}번 샷에서 사이클타임 {cy_time[hi]}초(배열 인덱스는 {hi})")

# 실습 2
ct_diff = np.diff(cy_time)
ct_abs = np.abs(ct_diff)
j = np.argmax(ct_abs)
print(f"{int(num[j])}번과 {int(num[j + 1])}번 사이에서 {ct_abs[j]}초만큼 변함")