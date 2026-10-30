# import math
# print(math.sqrt(16))
# print(math.ceil(4.2))

# from math import sqrt, ceil
# print(sqrt(16))
# print(ceil(4.2))

# import math as mt
# print(mt.sqrt(16))
# print(mt.ceil(4.2))

##############################################################################################

# import math
# import random
# value = random.randint(1, 100)
# print(value, round(math.sqrt(value), 2))

##############################################################################################

# import os
# # 폴더 경로 확인
# print("현재 실행 위치(절대경로): ", os.getcwd())

# # 폴더 유무 확인
# print(os.path.exists("data"))

# # 폴거 목록 확인
# files = os.listdir("data")
# print(files)

##############################################################################################

# import os
# print(os.getcwd())
# file_list = os.listdir("data")
# for i in file_list:
#     print(i)
# csv_files = []
# for i in file_list:
#     if i.endswith(".csv"):
#         csv_files.append(i)
# print(csv_files)

##############################################################################################

# import os
# data_path = os.path.join("data", "08_press_13_261029_3.csv")
# judge = os.path.exists(data_path)
# print(judge)
# if judge is True:
#     print("path 확인")
# else:
#     print("path 확인불가")

##############################################################################################

# import os, datetime
# file_num = len(os.listdir("data"))
# now = datetime.datetime.now()
# print(f"파일 {file_num}개, 점검 시각 {now:%Y-%m-%d %H:%M}")

##############################################################################################

# import os
# list = os.listdir("data")
# csv_list = []
# path = []
# for i in list:
#     if i.endswith(".csv"):
#         csv_list.append(i)
#         path.append(os.path.join("path", "i"))
# print(f"[CSV]목록: {csv_list}")

##############################################################################################

# # 파일 입출력
# # open 형식: open(파일명, 모드, encoding)
# # encoding = "utf-8" >> 한글이 깨지지 않도록 하는 것

# FILE = "data/08_press_13_261029_3.csv"

# f = open(FILE, "r", encoding="utf-8")
# text = f.read()
# print(text)
# f.close()       # 파일을 열고난 후 닫기

# f = open(FILE, "r", encoding="utf-8")
# lines = f.readlines()
# print(type(lines), len(lines))
# f.close()       # 파일을 열고난 후 닫기

##############################################################################################

# # with open - 블록이 끝나면 자동으로 파일 close
# FILE = "data/08_press_13_261029_3.csv"
# with open(FILE, "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)
        
# write()
# with open("data/test.txt", "w", encoding="utf-8") as f:
#     f.write("쓰기 테스트\n")
#     f.write("실습 2. with open으로 파일에 쓰기")
    
# with open("data/test.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#     print(text)
    
##############################################################################################

# with open("data/test.txt", "a", encoding="utf-8") as f:
#     f.write("\na로 이어쓰기")
# with open("data/test.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#     print(text)

##############################################################################################

# FILE = "data/08_press_13_261029_3.csv"
# import csv
# with open(FILE, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
        
##############################################################################################    

import csv
with open("data/08_summary.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])            # 헤더
    writer.writerow(["09:00", "PRESS-01"])
    writer.writerows([["09:01", "PRESS-02"], ["09:02", "PRESS-03"]])

with open("data/08_summary.csv", "r", encoding="utf-8") as f:
    print(f.read())