# # 02_02_실습1
# count = 11
# temp = 73.56
# name = 'heater'
# is_ok = True
# print(count, temp, name, is_ok)

# # 02_02_실습2
# print(type(count))
# print(type(temp))
# print(type(name))
# print(type(is_ok))

# # 02_02_실습3
# # 100 >> int(정수)
# # 100.0 >> float(실수)
# # "100" >> str(문자열)
# print(type(100))
# print(type(100.0))
# print(type("100"))

# # 02_02_실습4
# print(32+73.3)
# print("3"+"7")
# print("33"+"77")

# # 02_02_실습5
# print(3>2)
# print(5 == 5)
# print(type(3 > 2))

# # 02_02_실습6
# x = 10
# print(type(x))
# x = 10.5
# print(type(x))
# x = "10"
# print(type(x))

# # 02_02_실습7
# device_temp = 72.5
# check_count = 3
# device_name = "펌프1"
# is_normal = True

# # 02_03_실습1
# a = 17
# b = 5
# print(a + b, a - b, a * b, a / b)
# print(a // b, a % b, a ** b)

# # 02_03_실습2
# s1, s2, s3 = 85, 90, 86
# avg = (s1 + s2 + s3) / 3
# side = 7
# area = side ** 2
# volume = 3 * 4 * 5
# print("평균", avg, "· 넓이", area, "· 부피", volume)

# # 02_03_실습3
# print(10 == 10)
# print(10 != 5)
# print(3 > 5)
# print(3 < 5)
# print(5 >= 5)
# print(4 <= 2)

# # 02_03_실습4
# temp = 85
# temp_ok = temp >= 60 and temp <= 90
# pressure = 5
# pressure_ok = pressure >= 3 and pressure <= 7
# all_ok = temp_ok and pressure_ok
# print("온도 정상", temp_ok, "· 압력 정상", pressure_ok, "· 모두 정상", all_ok)

# # 02_03_실습5
# stock = 100
# print(stock)
# stock += 50
# print(stock)
# stock -= 30
# print(stock)
# stock += 5
# print(stock)

# # 02_03_실습6
# total, defect = 500, 23
# defect_rate = defect / total * 100
# run_h, all_h = 21, 24
# uptime = run_h / all_h * 100
# print("불량률", defect_rate, "% · 가동률", uptime, "%")

# # 02_03_실습7
# total_min = 500
# hours = total_min // 60
# minutes = total_min % 60
# print(hours, "시간", minutes, "분")

# # 02_04_실습1
# birth_year = int(input("태어난 해를 입력하세요: "))
# age = 2026 - birth_year
# print("나이:", age, "세")

# # 02_04_실습2
# nation = input("국가: ")
# city = input("도시: ")
# print(nation + "의 " + city + "에 거주하시는군요!")

# # 02_04_실습3
# a = int(input("수1: "))
# b = int(input("수2: "))
# print("합:", a + b)
# print("나눗셈:", a / b)

# # 02_04_실습4
# temp = int(input("온도: "))
# print("80 초과?", temp > 80)
# print("0 이상?", temp >= 0)

# # 02_04_실습5
# a = int(input("수1: "))
# b = int(input("수2: "))
# c = int(input("수3: "))
# avg = (a+b+c)/3
# print("60 이상?", avg >= 60)

# 03_01_실습1
# 삼중 따옴표: 엔터 친 그대로 줄바꿈이 됨
checklist1 = """가동 점검표
1. 온도 확인
2. 압력 확인"""
print(checklist1)

print("-" * 15)

# 이스케이프 문자: \n = 줄바꿈, \t = 탭(들여쓰기)
checklist2 = "가동 점검표\n\t1. 온도 확인\n\t2. 압력 확인"
print(checklist2)

print("-" * 15)

print("가동 점검표 / 1. 온도 확인 / 2. 압력 확인")

# 03_01_실습2
코드 = 'PUMP_A'
상태 = '정상'
날짜 = '2025-01-15'
print(코드 + '/' + 상태 + '/' + 날짜)

# 03_01_실습3
code = 'PUMP_A'
status = 'WARNING'
run_time = 600
chk_date = '2026-10-26'
print("설비: " + code)
print("상태: " + status)
print("가동 시간(min): " + str(run_time))
print("가동일: " + chk_date)