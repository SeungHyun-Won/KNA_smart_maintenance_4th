# temps = [35, 32, 31, 22, 21, 20, 25, 19]
# for t in temps:
#     if t >= 30:
#         print(f"고온: {t} ", end = '')
# print()


#############################################################################################
 
# act_time = [8, 6, 10, 9, 11, 4, 2, 3, 14, 15]
# for t in act_time:
#     if t >= 5 and t <= 10:
#         print(t, end = " ")
# print()

#############################################################################################

# temps = [36, 32, 31, 22, 21, 20, 25, 19]
# sum = 0
# count = 0
# for t in temps:
#     if t > 30:
#         sum += t
#         count += 1
# print("고온 평균: ", sum / count)
# print()

#############################################################################################

# temps = [35, 32, 31, 33, 22, 21, 20, 25, 19]
# high_temps = []
# for t in temps:
#     if t > 30:
#         high_temps.append(t)
# print(temps, '/', high_temps, ', 개수: ', len(high_temps))
# print()

#############################################################################################

# temps_c = [35, 32, 31, 33, 22, 21, 20, 25, 19]
# temps_f = []
# for t in temps_c:
#     t = t*1.8 + 32
#     temps_f.append(round(t, 2))
# print(f"섭씨 온도: {temps_c}")
# print(f"화씨 온도: {temps_f}")
# print()

##############################################################################################

# temps = [35, 32, 31, 33, 22, 21, 20, 25, 19]
# high_temps = []
# total = 0
# high_total = 0
# count = 0
# high_count = 0
# for t in temps:
#     if t > 30:
#         high_temps.append(t)
#         total += t
#         high_total += t
#         count += 1
#         high_count += 1
#     else:
#         total += t
#         count += 1
# print(f"전체 평균: {round((total / count), 2)} / 고온 개수: {high_count} / 고온 평균: {high_total / high_count}")

##############################################################################################
########################################### 05 끝 ############################################
##############################################################################################

# #################### tuple과 list 차이점 ########################## 
#               구분	        list = []	  tuple = ()
#          여러 자료형 섞기	        가능	       가능
#          값 수정, 추가, 삭제	    가능	      불가능
#          딕셔너리 키로 사용	    불가능	        가능

# sensor = ('모터온도', 78)
# print(sensor[0])
# print(sensor[1])
# name, value = sensor   # >> name = sensor[0], value = sensor[1]
# print(name, value)
# print()

##############################################################################################

# sensor = [('sensor_A', 77), ('sensor_B', 64), ('sensor_C', 88), ('sensor_D', 76)]
# names = []
# values = []
# for n, v in sensor:   #### >> for t in sensor    n, v = t  
#     names.append(n)
#     values.append(v)
#     print(f"{n}의 출력: {v}")
#     if v > 90:
#         print(f"{n} 경고")
# print()
# print(names)
# print(values)

##############################################################################################

sensor = [('sensor_A', 77, (5, 2)), ('sensor_B', 64, (3, 4)),
          ('sensor_C', 88, (8, 6)), ('sensor_D', 76, (10, 8))]
names = []
values = []
location_x = []
location_y = []
for n, v, loc in sensor:
    names.append(n)
    values.append(v)
    location_x.append(loc[0])
    location_y.append(loc[1])
    if loc[0] <= 5:
        print(f"센서 이름: {n} / 센서 위치 = {loc} / 센서 측정값: {v}")
    else:
        print(f"센서 이름: {n} / 센서 위치 = {loc}")
print()

##############################################################################################
################################### 위에 코드랑 같은 내용 #######################################
##############################################################################################

sensors = [('sensor_A', 77, (5, 2)), ('sensor_B', 64, (3, 4)),
           ('sensor_C', 88, (8, 6)), ('sensor_D', 76, (10, 8))]
X_LIMIT = 5
selected = []

for name, value, (x, y) in sensors:   ### >>>>>> name  = sensor[0][0], value = sensor[0][1],
    print(f"{name}: 위치 ({x}, {y}) / 측정값 {value}")   ### x = sensor[0][2][0], y = sensor[0][2][1]
    if x <= X_LIMIT:
        selected.append(name)

print(f"x ≤ {X_LIMIT} 센서만: {', '.join(selected)}")