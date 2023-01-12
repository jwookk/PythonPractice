sentence = '나는 소년입니다.'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""                                 # 여러줄 입력
print(sentence3)


#슬라이싱

number = "991020-1234567"

print("성별 : " + number[7])        # 대괄호 활용해서 위치에 있는 값 가져옴
print("연 : " + number[0:2])        # 0부터 2전까지 있는 값 가져옴
print("월 : " + number[2:4])        # 2부터 4전까지
print("일 : " + number[4:6])        # 4부터 6전까지
print("생년월일 : " + number[:6])    # 처음부터 6전까지
print("뒤 7자리 : " + number[7:])    # 7부터 끝까지
print("뒤 7자리(뒤에부터) : " + number[-7:])
# 맨 뒤에서 7번째부터 끝까지


#문자열 처리함수

python = "Python is Amazing"

print(python.lower())                   # 모든 문자 소문자로 출력
print(python.upper())                   # 모든 문자 대문자로 출력
print(python[0].isupper())              # 문자가 대문자인지 True/False 출력
print(len(python))                      # 문자열 길이 출력
print(python.replace("Python", "Java")) # 문자열 변경

index = python.index("n")               # n이라는 몇번째 위치해있는지 출력 (첫번째)
print(index)
index = python.index("n", index + 1)    # 첫번째 "n" 다음부터 찾음 (두번째 n 찾음)
print(index)

print(python.find("Java"))              # 찾는 문자열이 없으면 -1 반환
#print(python.index("Java"))             # 찾는 문자열이 없으면 오류(이후 실행안됨)

print(python.count("n"))                # 찾는 문자가 몇개 있는지 출력