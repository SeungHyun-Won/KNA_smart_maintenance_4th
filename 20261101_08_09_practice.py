# import csv
# FILE = "data/08_press_13_261029_3.csv"
# high = []
# with open(FILE, "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if float(row["전류"]) > 90:
#             high.append(row)

# with open("data/high_current.csv", "w", encoding="utf-8", newline="") as f: #newline >> 빈줄 없애기
#     writer = csv.writer(f)
#     for row in high:
#         writer.writerow(high)
# print(len(high), "행 저장")
    
##############################################################################################

# import csv
# # 새로운 리스트 변수 선언
# list = []

# with open("data/08_press_13_261029_3.csv", "r", encoding="utf-8") as f:
#     # 헤더 값 건너뛰기
#     reader = csv.reader(f)
#     header = next(reader)
#     print(header)

#     # 전류 값 기준 90 초과 값만 새로운 리스트 담기
#     for row in reader:
#         current = float(row[4])
#         if current > 90:
#             list.append(row)

# # 조건에 맞는 데이터를 새 CSV로 저장
# with open("data/08_current_over90.csv", "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerows(list)

# print("저장된 행 수:", len(list))

##############################################################################################
########################################### 08 끝 ############################################
##############################################################################################

# try:
#     temp = float(input("온도: "))
#     print("변환성공 >> 온도: ", temp)
# except ValueError:
#     temp = float(input("온도(숫자로 입력): "))
# print("프로그램이 계속됩니다.") 

##############################################################################################

# text = input("측정값: ")
# try:
#     n = int(text)
#     print(100 / n)
# except ValueError:
#     print("정수를 입력하세요.")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")

##############################################################################################

# f = open("data/09_ict_inspection_15_261102_1.csv", "r", encoding="utf-8")
# try:
#     lines = f.readlines()
#     x = 1 / 0
# finally:
#     f.close()
#     print("파일 닫힘:", f.closed)

##############################################################################################

# try:
#     with open("data/09_ict_inspection_dirty_15_261102_2.csv", "r", encoding="utf-8") as f:
#         rows = f.readlines()[1:]    # 슬라이싱 >> 헤더 빼려고
# except FileNotFoundError:
#     rows = []

# total = 0.0
# skipped = 0
# for line in rows:
#     try:
#         total += float(line.split(",")[2])  # 측정값만 더함
#     except (ValueError, IndexError):
#         skipped += 1
#         continue
    
# print("합계: ", round(total, 1), "/ 건너뜀: ", skipped)
# print(rows)

##############################################################################################

# total = 0.0
# skipped = 0
# try:
#     with open("data/09_ict_inspection_dirty_15_261102_2.csv", "r", encoding="utf-8") as f:
#         rows = f.readlines()[1:]
#     for line in rows:
#         try:
#             total += float(line.split(",")[2])
#         except (ValueError, IndexError):
#             skipped += 1
#             continue
# except FileNotFoundError:
#     print("파일 없음")

# print("합계: ", round(total, 1), "/ 건너뜀: ", skipped)

##############################################################################################

names = ["data/09_ict_inspection_15_261102_1.csv", "data/08_press.csv",
         "data/09_ict_inspection_dirty_15_261102_2.csv"]
done = 0
for name in names:
    try:
        with open(name, "r", encoding="utf-8") as f:
            rows = f.readlines()[1:]
            done += 1
            row_num = len(rows)
            print(name, "의 행 수: ", row_num)
    except FileNotFoundError:
        continue
print("처리한 파일: ", done)
        
        
        

