# # 인덱싱 - 위치번호로 글자를 하나 꺼낸다.
# # 형식: 문자열[번호] (첫 글자 = 0번)\
    
#  word = 'PYTHON'
#  print(word[0], word[2], word[5]) #결과: P  T  N

# # # 음수 인덱스: 뒤에서부터 -1, -2, ...
#  print(word[-1], word[-2])  #결과: N  O

# print(word[6])  #IndexError: string index out of range

# word_2 = 'SIGNAL'
# print(word_2[0], word_2[2], word_2[5])  #결과: S  G  L
# print(word_2[-1], word_2[-2])  #결과: L  A
# print(word_2[6])  #IndexError: string index out of range

# print(word_2[0:3])
# print(word_2[2:5])
# word3 = 'temp_sensor'
# print(word3[:4])
# print(word3[5:])

# word4 = 'sensor_01'
# print(word4[-2:])

# word_2 = 'SIGNAL'
# print(word_2[::2])
# print(word_2[::-1])

#========03_03=========

# 문자열 연산과 검색
# 문자열 연결(+), 반속(*)

# len() >> 글자 수 표시 / 형식: len(문자열)
print(len('PYTHON'))
print(len('AI 분석'))
print(len(''))

# in / not in >> 포함 / 불포함 여부 판단 (결과: bool)
# 형식: '찾을 것' in 문자열
print('고장' in '설비 고장 발생')
print('정상' not in '고장 발생')

# count
# 형식: 문자열.count('x') >> 개수
print('banana'.count('a'))

# find
# 형식: 문자열.find('x') >> 처음 나오는 위치를 반환해줌
print('banana'.find('a')) # 1
print('banana'.find('t')) # -1 (못 찾았을 경우)

# index
# 주의) 위치를 반환하지만 없으면 오류발생
email = 'hong@company.com'
at = email.index('@')
print(at)
print(email[:at]) #Hong

# startwith / endswith
# 형식: 문자열.startswitch('x') >> bool
print('EQP-001'.startswith('EQP'))

# replace
print(' 정 상 가 동 '.replace(' ', ''))