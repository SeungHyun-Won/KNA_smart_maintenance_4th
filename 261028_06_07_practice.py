# sensor = ['S01', 'S04', 'S03', 'S02', 'S01', 'S04']
# s = set(sensor)
# print(sorted(s), "종류 수: ", len(s))

##############################################################################################

# line_A = {'S01', 'S04', 'S03', 'S02', 'S01', 'S04'}
# line_B = {'S02', 'S03', 'S06', 'S05', 'S06'}
# print(f"전체: {line_A.union(line_B)}\n"
#       f"교집합: {line_A.intersection(line_B)}\n"
#       f"A만: {sorted(line_A.difference(line_B))}\n"
#       f"B만: {sorted(line_B.difference(line_A))}")
# print()

##############################################################################################

# day1 = {'S01', 'S04', 'S03', 'S02', 'S01', 'S04'}
# day2 = {'S02', 'S03', 'S06', 'S05', 'S06'}
# print(f"신규 이상: {sorted(day2.difference(day1))}\n"
#       f"지속 이상: {sorted(day1.intersection(day2))}")
# print()

##############################################################################################

# sensors = {"sensor_A": 78, "sensor_B": 67, "sensor_C": 76}
# print(sensors["sensor_A"])
# print(sensors.get("sensor_D"))
# sensors["sensor_D"] = 54 #### 단일 추가
# sensors.update({"sensor_A": 87, "sensor_E": 77}) #### 여러개 추가 및 수정
# print(sensors)
# print(sensors.get("sensor_D"))
# print("sensor_E" in sensors)

##############################################################################################

# sensors = {"sensor_A": 78, "sensor_B": 67, "sensor_C": 76}
# sensors_2 = {"sensor_A": 73, "sensor_D": 76}
# sensors.update({"sensor_A": 73, "sensor_D": 76}) ### == sensors.update(sensors_2)
# del sensors ["sensor_C"]
# print(sensors, " / 센서 수: ", len(sensors))
# print()

##############################################################################################

# sensors = {"sensor_A": 78, "sensor_B": 67, "sensor_C": 76, "sensor_D": 88}
# avg = sum(sensors.values()) / len(sensors)
# print(round(avg, 2))
# max_value, max_name = None, None
# for name, value in sensors.items():
#     if max_value is None or value > max_value:  ### None >> is로 상태 지정 / max_value == 0
#         max_name = name
#         max_value = value
# print(f"최댓값 센서: {max_name}, {max_value}")
# print()

##############################################################################################

# names = ['sensor_A', 'sensor_B', 'sensor_C', 'sensor_D']
# values = [77, 56, 64, 80]
# sensors = dict(zip(names, values))
# # print(sensors)
# for name, value in sensors.items():
#     print(f"센서명: {name}, 측정값: {value}")

# print()

##############################################################################################

# values = {"온도": 95, "진동": 0.5, "압력": 88}
# limits = {"온도": 90, "진동": 1.0, "압력": 90}
# warning = []
# for name, value in values.items():
#     if value > limits[name]:
#         warning.append(name)
# print("경고 센서:", warning)   # ['온도']



# ##############################################################################################

# plant = {
#   "1번모터": {"온도": 78, "상태": "정상"},
#   "2번펌프": {"압력": 95, "상태": "경고"}
# }

# print(plant["2번펌프"]["압력"])

# for name, info in plant.items():
#   if info["상태"] == "경고":
#     print(name, "점검 필요")

# ##############################################################################################

# sensors = ["sensor_A, 78", "sensor_B, 67", "sensor_C, 76", "sensor_D, 88", "sensor_E, 90"]
# result = {}
# for sensor in sensors:
#     name, value = sensor.split(",")
#     result[name] = float(value)
# print(result)
# print()

# ##############################################################################################

# sensors = {"온도": 95, "압력": 96}
# limits = {"온도": 90, "압력": 90}

# # values() 이용한 평균
# avg = sum(sensors.values()) / len(sensors)
# print("평균:", round(avg, 1))

# # items() 순회 -> 임계값 비교 -> 초과한 값은 셋에 담기(키 값 담기)
# danger = set()
# for name, v in sensors.items():
#   if v > limits[name]:
#     danger.add(name)

# # 셋 정렬하여 출력
# print("위험 센서:", sorted(danger))

##############################################################################################
########################################### 06 끝 ############################################
##############################################################################################

# 함수의 기본 구조
# 형식: def 함수이름():
#          실행할 코드(들여쓰기)

def greet():
    print("점검을 시작합니다.")

# 정의만으론 실행 안됨. >> 호출해야함.
# 호출: 함수 이름 적고 괄호를 붙인다.

greet()
greet()
greet()
greet()
