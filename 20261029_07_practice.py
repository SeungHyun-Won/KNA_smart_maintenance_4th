# def show_info():
#     print("전원을 차단합니다.")
#     print("보호구를 착용합니다.")
#     print("결과를 기록합니다.")

# print("압축기 A 점검")
# show_info()
# print("펌프 1 점검")
# show_info()

##############################################################################################

# def hello():
#     print("안녕하세요")
    
# hello()
# hello()

##############################################################################################

# def print_line():
#     print('=' * 50)
    
# def show_info():
#     print("전원을 차단합니다.")
#     print("보호구를 착용합니다.")

# print_line()
# print("압축기 A 점검")
# show_info()
# print_line()
# print("펌프 1 점검")
# show_info()
# print_line()

##############################################################################################

# def print_temp(name, temp):
#     print(name + ' ' + str(temp) + ' 도')

# print_temp("모터", 78)
# print_temp(name = "펌프", temp = 78)

##############################################################################################

# def print_temp(name, temp):
#     print(name + ' ' + str(temp) + ' 도')

# print_temp(name = "펌프", temp = 78)
# print_temp(temp = 78, name = "펌프")
# print_temp("펌프", temp = 78)

##############################################################################################

# def cal_func(a, b):
#     return round(((a + b)/2), 2)

# avg = cal_func(14, 16)
# print("평균: ", avg)
# print("합계: ", avg * 2)

##############################################################################################

# def min_max(sensor_values):
#     return min(sensor_values), max(sensor_values), (sum(sensor_values) / len(sensor_values))

# sensor_values = [77, 88, 99, 66, 55, 44]
# min, max, avg = min_max(sensor_values)
# print("최소: ", min, "최대: ", max, "평균: ", avg)

##############################################################################################

# def cal_limit(value, limit = 50):
#     if value > limit:
#         print(f"{value} >> 경고")
#     else:
#         print(f"{value} >> 정상")

# cal_limit(78)
# cal_limit(44)
# cal_limit(78, limit = 80)

##############################################################################################

# def get_avg(values):
#     x = 55
#     return sum(values, x) / (len(values) + 1)

# temp = [66, 78, 98, 22, 55, 101, 56, 88]
# avg = get_avg(temp)
# print(round(avg, 2))
# print(x)


##############################################################################################

def get_avg(values):
    return sum(values) / len(values)

def judge(avg, limit = 80):
    if avg < limit:
        print("평균: ", avg, " >> ", "정상")
    else:
        print("평균: ", avg, " >> ", "비정상")

temp = [66, 78, 98, 22, 55, 101, 56, 88]
avg = get_avg(temp)
judge(avg)
judge(avg, limit = 70)

##############################################################################################

def cal_avg(sensor_values):
    return sum(sensor_values) / len(sensor_values)

def judge_status(avg, limit = 70):
    if avg < limit:
        return "정상"
    else:
        return "점검 필요"
    
sensor_values = [77, 67, 99, 44, 53, 66, 81, 43]
avg = cal_avg(sensor_values)
status = judge_status(avg)
print(avg, status)