import pandas as pd

F_SHOT = 'data/13_diecasting_shot_24_261110_2.csv'
F_MASTER = 'data/13_diecasting_master_24_261110_1.CSV'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

# # merge는 옆으로 칸을 이어 붙이고, concat은 아래로 줄을 쌓는다
# # concat은 키 열이 필요 없고, 칸 이름만 맞으면 된다

# # pd.concat

# # ex) 설비 로그를 1차, 2차로 나눠 받은 경우
# part1 = log.iloc[:100].reset_index(drop=True)
# part2 = log.iloc[100:].reset_index(drop=True)
# print(part1.shape, part2.shape)      # (100, 8) (100, 8)

# stacked = pd.concat([part1, part2])
# print(stacked.shape)  # (200, 8)
# print(stacked.index[-3:].tolist())  # [97, 98, 99]
# print(len(stacked.loc[[0]]))  # 2

# # - 번호를 다시 매기기 -> ignore_index
# renumbered = pd.concat([part1, part2], ignore_index=True)
# print(int(renumbered.index[-1]))

# - 칸이(열이) 다른 표를 붙이면 -> 빈 칸
# - 붙이기 전에 두 표의 columns 비교
#   -> set(표1.columns) - set(표2.columns)

# # 실습 3
# log = pd.read_csv(F_SHOT)
# front = log.iloc[:100].reset_index(drop=True)
# back = log.iloc[100:].reset_index(drop=True)
# both = pd.concat([front, back])
# print(both.shape, len(both.loc[[0]]))
# both2 = pd.concat([front, back], ignore_index=True)
# print(both2.index[-1])
# # 실습 4
# log = pd.read_csv(F_SHOT)
# master = pd.read_csv(F_MASTER)
# m = log.merge(master, on="설비ID", how="left")
# has_line = m[m["라인"].notna()]
# print(len(has_line))
# not_ok = has_line[has_line["품질등급"] != "양품"]
# print(len(not_ok))
# top = not_ok.sort_values("비스킷두께", ascending=False)
# print(top[["샷", "설비ID", "라인", "비스킷두께", "품질등급"]].head(5))

##############################################################################################
########################################### 13 끝 ############################################
##############################################################################################

import pandas as pd

F = 'data/14_hydraulic_26_261112_1.csv'
df = pd.read_csv(F)

# # 실습 1
# print(df.shape)
# value_counts = df["밸브상태"].value_counts()
# load_counts = df["운전부하"].value_counts()
# print(value_counts)
# print(df["밸브상태"].value_counts(normalize=True).round(3))
# print(load_counts)
# print(df["운전부하"].value_counts(normalize=True).round(3))

# for counts in [value_counts, load_counts]:
#     print("가장 많은 값:", counts[counts == counts.max()])
#     print("가장 적은 값:", counts[counts == counts.min()])
# # vc = df["밸브상태"].value_counts() 
# # print("최대:", vc[vc == vc.max()].index.tolist())
# # print("최소:", vc[vc == vc.min()].index.tolist())

# # 실습 2
# F_QC = 'data/14_hydraulic_qc_26_261112_2.csv'
# qc = pd.read_csv(F_QC)
# print(qc.shape)
# value_counts = qc["검사결과"].value_counts()
# print(value_counts)
# p = qc["검사결과"].value_counts(normalize=True)
# print(p.round(3))
# print(f"불합격은 전체의 약 {p.loc['불합격'] * 100:.1f}%")

# # 실습 3
# vib = qc["진동"]
# print(vib.max(), vib.min())
# vib_c = pd.cut(vib, bins=[0, 0.6, 0.7, 10], labels=["약함", "보통", "강함"], right=True)
# a = vib_c.value_counts()
# print(a)
# print("검산:", a.sum(), "구간 미지정:", a.isna().sum())
# print("최대구간:", a[a == a.max()])
# print("최소구간:", a[a == a.min()])
# # print("구간 미지정:", vib_c.isna().sum())
# # print("최대:", a.idxmax(), " 최소:", a.idxmin())

# v2 = pd.cut(df["진동"], bins=[0, 0.62, 0.7, 10], labels=["약함", "보통", "강함"])
# print(v2.value_counts(sort=False).tolist())


# # groupby
# means = df.groupby("냉각기상태")["온도"].mean()
# print(means.round(2))

# print(df.groupby("냉각기상태")["온도"].max())

# # 여러 키 그룹 코드
# keys = ["냉각기상태", "운전부하"]
# print(df.groupby(keys)["온도"].max())
# # 냉각기상태  운전부하
# # 고장     고부하     57.8
# #        저부하     57.1
# # 저하     고부하     44.1
# #        저부하     51.2
# # 정상     고부하     36.4

# # crosstab - 두 기준의 결과를 가로세로 표로
# print(pd.crosstab(df["냉각기상태"], df["운전부하"]))
# # 운전부하   고부하  저부하
# # 냉각기상태
# # 고장      17   23
# # 저하       3   37
# # 정상      40    0

# 실습 4
group = df.groupby("냉각기상태")["온도"]
print(group.size())  ### .size()와 비교해봐
print(group.mean().round(2))
print(group.max().round(2))
means = group.mean()
print(f"차이: {(means.max() - means.min()).round(2)}")
print("-"*30)

# 실습 5
total = df["밸브상태"].value_counts()
fail = df[df["result"] == "고장"]
fail_tot = fail["밸브상태"].value_counts() ### = fail.groupby("밸브상태").size()
# fail_tot = fail.groupby("밸브상태").size()

# 고장 라벨이 0건인 상태도 빠지지 않도록 이름표를 맞춘다
fail_tot = fail_tot.reindex(total.index, fill_value = 0)

rate = (fail_tot / total).sort_values(ascending=False)
print(total, fail_tot, rate.round(3))