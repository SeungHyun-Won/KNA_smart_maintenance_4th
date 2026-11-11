import pandas as pd

F_SHOT = 'data/13_diecasting_shot_24_261110_2.csv'

# fs = pd.read_csv(F_SHOT)

# # 배열에서 하던 것
# arr = fs["비스킷두께"].values
# print("배열에서 조건 참 개수:", int((arr >= 16).sum())) ### True는 1로 계산되어 sum된다. >> 74

# # 표에서 하는 것
# print("배열에서 조건 참 개수:", int((fs["비스킷두께"] >= 16).sum())) ### 74

# # 조건 -> Boolean Series
# print((fs["비스킷두께"] >= 16).head(3).tolist()) ### [False, False, False]


# # 실습 1
# print(fs.shape)
# cond = fs["비스킷두께"] >= 16
# print(fs[cond], len(cond))
# cond2 = fs["비스킷두께"] < 16
# print(cond.sum(), cond2.sum(), len(fs) - (cond.sum() + cond2.sum()))


# # 복합 조건
# both = fs[(fs["비스킷두께"] >= 16) & (fs["사이클타임"] >= 25)]
# either = fs[(fs["비스킷두께"] >= 16) | (fs["사이클타임"] >= 25)]
# print(len(both), len(either))

# # 부정 조건: ~
# print(len(fs[~(fs["품질등급"] == "불량")]))

# # isin : 값이 포함되어 있는지
# print(len(fs[fs["품질등급"].isin(['주의', '불량'])])) # | 사용과 같은 결과

# # between: 사이를 의미(양쪽 경계 모두 포함)
# print(len(fs[fs["비스킷두께"].between(10, 16)]))

# # 문자열 조건
# # - str.contains : 해당 문자열을 포함하는 값
# print(len(fs[fs["설비ID"].str.contains("A")]))  # A라인 전체

# # - str.split, str.replace, str.strip ...
# print(fs["설비ID"].head(1).tolist())    # ['DIE-A-01']
# print(fs["설비ID"].str.split("-").head(1).tolist())     # [['DIE', 'A', '01']]


# # 실습 2
# cond = (fs["비스킷두께"] >= 16) & (fs["사이클타임"] >= 25)
# cond2 = (fs["비스킷두께"] >= 16) | (fs["사이클타임"] >= 25)
# print(len(fs[cond]), len(fs[cond2]))
# print(len(fs[~(fs["품질등급"] == "불량")]))
# print("-" * 20)

# # 실습 3
# print(len(fs[fs["품질등급"].isin(['주의', '불량'])]))
# print(len(fs[fs["비스킷두께"].between(10, 16)]))
# print(len(fs[fs["설비ID"].str.split("-").str[1] == "A"]))
# print(len(fs[fs["설비ID"].str.contains("A") & fs["설비ID"].str.contains("01")]))

# # 정령, 복사본
# # 정렬 - sort_values >> 기본 작은값순서인 오름차순
# asc = fs.sort_values("비스킷두께")  ### >> 표임
# print(asc["비스킷두께"].head(3).tolist())

# # 다중 키 정렬, 내림 차순
# dec = fs.sort_values("사이클타임", ascending=False)
# print(dec["사이클타임"].head(3).tolist())

# # 다중 키 정렬
# two = fs.sort_values(["품질등급", "비스킷두께"], ascending=[True, False]) ## 품질등급 나누고나서 나눈 범위안의 값들의 비스켓두께
#                                                                     ## 기준으로 내림차순정리한다. >> 뭐먼저 적는지에따라 바뀜.
# print(two["샷"].head(3).tolist())

# #copy
# x = fs[fs["품질등급"] == '불량'].copy()
# print(x.shape)
# x["위험등급"] = "높음"
# print(x.shape)


# # 실습 4
# print(fs.sort_values("비스킷두께", ascending=False).head(5))
# m = fs.sort_values(["품질등급", "사이클타임"], ascending=[True, False])
# print(m.head(5))
# print(m["샷"].head(5).tolist())
# print(fs["샷"].head(5).tolist())
# print("-" * 20)

# # 실습 5
# cond = (~(fs["품질등급"] == "양품")) & (fs["비스킷두께"] >= 16)
# a = fs[cond].sort_values("비스킷두께", ascending=False)
# print(a[["샷", "비스킷두께", "품질등급"]].head(5), "\n", len(a), sep = '')
# miss = (fs["품질등급"] != "양품") & fs["비스킷두께"].isna()
# print(miss.sum())


F_MASTER = 'data/13_diecasting_master_24_261110_1.CSV'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

# print(log.shape)
# print(master.shape)

# three = log.head(3)[["샷", "설비ID", "비스킷두께"]]
# print(three.to_string(index = False))

# print(three.merge(master, on="설비ID").to_string(index = False))

# merge 기본 사용법
# - on : 두 표를 잇는 키 열
# - 행은 예측불가, 열 수는 예측 가능

# - how : 어느쪽을 다 남길 것인가
#   - (기본) how='inner'
#   - how='left' : 왼쪽은 다 남기고 짝 없으면 빈 칸
#   - how='outer' : 양쪽 다 남김

# m_inner = log.merge(master, on="설비ID")
# m_left = log.merge(master, on="설비ID", how='left')
# m_outer = log.merge(master, on="설비ID", how='outer')

# print(m_inner.shape, m_left.shape, m_outer.shape)   #(185, 12) (200, 12) (201, 12)

# # 실습 1
# print(log.shape)
# print(master.shape)
# print(log.columns.tolist())
# print(master.columns.tolist())
# merged = log.merge(master, on="설비ID")
# print(merged.shape)
# print(merged.columns.tolist())


# # 합치기 전후 점검 코드
 
# print(len(log))     #200
# print(len(master), master["설비ID"].nunique())  #5 5

# m_left = log.merge(master, on="설비ID", how="left")
# print(len(m_left))  #200
# print(int(m_left["라인"].isna().sum()))     #15

# unmatched = m_left[m_left["라인"].isna()]
# print(unmatched["설비ID"].head().tolist(), len(unmatched))  #['DIE-C-01', 'DIE-C-01', 'DIE-C-01', 'DIE-C-01',       'DIE-C-01'] 15

# 실습 2
print(len(log.merge(master, on="설비ID")))
ml = log.merge(master, on="설비ID", how="left")
mo = log.merge(master, on="설비ID", how="outer")
print(len(ml), len(mo))
lost = ml[ml["라인"].isna()]
print(lost["설비ID"].unique().tolist(), len(lost))
print(mo[mo["샷"].isna()]["설비ID"].tolist())