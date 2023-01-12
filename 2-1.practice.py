# 자료형

print(5)                # 숫자 자료형 출력시에 따옴표 필요없음
print(3.14)             # 소수점 활용가능
print(5+3)              # 출력문에 사칙연산 활용가능
print(3*(3+5))          # 우선순위 연산자

print('나비')           # 문자열 자료형 출력시 작은따옴표 활용
print("풍선")           # 큰따옴표도 활용가능
print("가나다"*3)       # 반복출력 가능

print(5 > 10)           # boolean 자료형 (참, 거짓)
print(True)             # 직접입력 가능
print(not True)         # not 활용하여 반대(False) 출력
print(not (5 > 10))

# 변수

animal = "고양이"       # 변수 선언 시 자료형 입력안하고 바로 선언
name = "해피"
age = 2
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")                      # 변수활용
hobby = "공놀이"        # 변수를 중간에서 선언할 수도 있음
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")    # 숫자표시할 때 str로 변환
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")              # + 대신 , 활용 가능하며 이때는 str변환 불필요
print(name + "는 어른일까요? " + str(is_adult))                            # boolean 활용시에도 str로 변환

# 주석

'''
이렇게하면 
여러문장이
주석처리 됨
'''

# 그리고
# 드래그 후
# ctrl + /
# 활용해서
# 주석처리 및 해제 가능함