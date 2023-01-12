# 문자열 포맷

# 방법 1
print("나는 %d살입니다." % 20)                      # %d는 정수
print("나는 %s을 좋아해요" % "파이썬")               # %s는 문자열
print("Apple 은 %c로 시작해요." % "A")              # %c는 문자
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))    # 두가지 이상 출력 () 활용

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))  # 중괄호 안에 숫자를 활용하면, 괄호 안의 순서대로 출력

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))     # 변수 활용

# 방법 4 (파이썬 버전 3.6이상 부터)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")            # f 활용


# 탈출문자

print("백문이 불여일견\n백견이 불여일타")               # 줄바꿈문자(\n) 활용

print("저는 \"나도코딩\" 입니다.")                     # 큰따옴표 출력(\")

print("현재경로는 C:\\Users\\PythonWorkspace 입니다")  # 백슬래시 출력(\\)

print("Red Apple\rPine")                            # 커서를 맨앞으로 이동(\r)

print("Redd\bApple")                                # 백스페이스 기능(\b)

print("Red\tApple")                                 # 탭 기능(\t)