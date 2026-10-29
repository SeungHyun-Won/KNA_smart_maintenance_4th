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

def min_max(sensor_values):
    return min(sensor_values), max(sensor_values), (sum(sensor_values) / len(sensor_values))

sensor_values = [77, 88, 99, 66, 55, 44]
min, max, avg = min_max(sensor_values)
print("최소: ", min, "최대: ", max, "평균: ", avg)