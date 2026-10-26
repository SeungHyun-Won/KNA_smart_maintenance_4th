# age = 19
# if age >= 19:
#     print("참")
# else:
#     print("거짓")
# age2 = 18
# if age2 >= 19:
#     print("참")
# else:
#     print("거짓")
    
# score = 90
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("D")
    
# temp = 60
# if temp > 80:
#     print("위험")
# elif temp > 60:
#     print("주의")
# else:
#     print("정상")
    
# id = 'admin'
# pw = 123
# if id == 'admin' and pw == 1234:
#     print ("로그인 성공")
# else:
#     print("로그인 실패")

# temp, vib, curr = 78, 3.2, 52
# if temp > 80 or vib > 4.0:
#     print("위험: 즉시 정지")
# else:
#     if curr > 60 and temp > 70:
#         print("주의: 부하 점검")
#     elif vib > 2.5:
#         print("주의: 진동 관찰")
#     else:
#         print("정상")

######################### 04파트 끝 ###########################################################################


# n = int(input("끝 숫자 N: "))

# for i in range(1, n + 1):
#     print(i, end=' ')
# print()

# print("짝수", end=' ')
# for i in range(2, n + 1, 2):
#     print(i, end=' ')
# print()

# print("역순", end=' ')
# for i in range(n, 0, -1):
#     print(i, end=' ')
# print()

N = int(input("숫자 N을 입력하세요. "))
total = 0
for i in range(N+1):
    total += i
print(total)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i, '*', j, '=', i*j)
#         j += 1
#     print('==================')
#     i += 1

# num = int(input("측정 횟수를 입력하시오. "))
# count = 0
# for i in range(1, num + 1):
#     chk_num = int(input("측정값을 입력하시오. "))
#     if chk_num > 80:
#         count += 1
#     i += 1
# print(f"({num}회 중 {count}개가 80 초과) 초과 개수: {count}") 