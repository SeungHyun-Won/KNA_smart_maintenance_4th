# x = '2025-01-15'
# x = x.split('-')
# print(x)
# print('-'.join(x))

# print('2025', '01', '15',sep='-')
# print('2025', '01', '15',sep=', ')

# y = '2025/01/15'
# y = y.split('/')
# print(y)
# y = '-'.join(y)
# print(y)

# z = '1, NORMAL, 25.3'
# z = z.split(', ')
# print(z)
# print(z[1].strip().lower())

# pump_name = 'PUMP_A'
# temp = 87
# print(f'설비 {pump_name}, 온도 {temp}도')

# score_1 = 88
# score_2 = 78
# score_3 = 92
# print(f'평균 {(score_1 + score_2 + score_3) / 3}')

# x = 87.456
# print(f'{x:.2f}')
# print(f'{x:.1f}')

# text = ' 5,sensor_2,WARNING,0.78912 '
# text = text.strip()
# text = text.split(',')
# print(text)
# value = float(text[3])
# print(type(value))
# print(f'[센서 {text[1].lower().replace(' ', '_')}] 상태 {text[2].strip().lower()}, 측정값 {value:.2f}')

######################### 03파트 끝 ###########################################################################

# temps = [25, 26, 24, 28, 27]
# results = []
# print(temps)
# print(results)
# print(len(temps))
# print(len(results))

# temps = [25, 26, 24, 28, 27, 23]
# print(temps[0])
# print(temps[2])
# print(temps[-1])

# prods = [123, 122, 111, 100, 105, 99]
# x = prods[0]
# y = prods[5]
# print(x + y)
# print((x + y) / 2)

# temps = [25, 26, 24, 28, 27, 23, 21, 21, 19, 17]
# print(temps[:3])
# print(temps[-3:])
# print(len(temps[:3]))

# temps = [25, 26, 24, 28, 27, 23, 21, 21, 19, 17, 17, 18]
# first = temps[:6]
# second = temps[-6:]
# print(first)
# print(second)
# print(len(first), len(second))

# temps = [25, 26, 24, 28, 240, 27]
# print(240 in temps)
# print(temps.index(240))
# temps[4] = 24
# print(temps)
# print(240 in temps)

# temps2 = []
# temps2.append(28)
# print(temps2)
# temps2.insert(2, 21)
# print(temps2)
# temps2.extend(temps)
# print(temps2)

temps = [25, 26, 24, 28, 999, 26]
temps.remove(999)
print(temps)
temps_pop = temps.pop(1)
print("꺼낸 값",temps_pop)
del temps[0]
print(temps)

temps = [26, 24, 28, 24, 27, 30, 22]
temps.sort()
print(temps)
temps.reverse()
print(temps)
print(temps.count(24), temps.index(24))