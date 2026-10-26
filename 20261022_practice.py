# print(len('01012345678'))
# print('고장' in '설비 고장 발생')
# print('정상' in '설비 고장 발생')
# print('sensor-01-temp'.count('-'))
# print('temp_2024'.find('_'))
# print('temp_2024'.find('7'))
##====================================
# file_name = 'sensor_log.csv'
# print(file_name.startswith("sensor"))
# print(file_name.endswith('.csv'))

# label = 'WARNING'
# print(label == 'WARNING', label == 'warning')

#====================================
# x = 'ready'
# print(x.upper())
# y = 'WARNING'
# print(y.lower())
# name = 'kim chul soo'
# print(name.title())
# a = 'Fault'
# b = 'FAULT'
# print(a == b)
# a = a.lower()
# b = b.lower()
# print(a == b)

# #====================================
# print('ABC'.isupper(), 'ABC'.islower())
# print('abc'.isupper(), 'abc'.islower())
# print('Abc'.isupper(), 'Abc'.islower())

# x = 'Sensor_LOG.CSV'
# x_lower = x.lower()
# print(x_lower.startswith('sensor'), x_lower.endswith('.csv'))

# y = "   가동중   "
# y_strip = y.strip()
# print("[" + y_strip + "]")

# z = "  대기  "
# print("[" + z.lstrip() + "]", "[" + z.rstrip() + "]")

# print("***경고***".strip("*"))

# x = ' WARNING '
# print(x.strip().lower())

# y = '   경보   '
# print('[' + y.strip() + ']')
# print('[' + y + ']')
# y = y.strip()
# print('[' + y + ']')

#====================================
x = '설비 정상 가동'
print(x.replace('정상','점검'))

y = 'PUMP A 03'
print(y.split())

z = 'a,b,c,d'
print(z.split(','))

print(z.split(',', 1))