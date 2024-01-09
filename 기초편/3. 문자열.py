## 문자열
sentence = "나는 소년입니다."
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
# 문자열에 여러줄 입력
sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)



## 슬라이싱
jumin = "991231-1234567"
print("성별 : "+jumin[7])
# jumin 텍스트의 0~2 직전까지의 값을 가져옴.
print("연: " + jumin[0:2])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

# 문자 슬라이싱에서 `:`으로 시작하면 처음부터
print("생년월일 : "+jumin[:6])
# 문자 슬라이싱에서 `:`으로 끝나면 마지막까지
print("뒤 7자리 : "+jumin[7:])
# 문자 슬라이싱에서 음수로 시작하면 맨 뒤에서 7 번째부터 끝까지
print("뒤 7자리 : "+jumin[-7:])

##문자열 처리함수
python = "Python is Amazing"
# python 을 소문자로
print(python.lower())
# python 을 대문자로
print(python.upper())
# python의 첫번째 문자가 대문자인지 확인
print(python[0].isupper())

# python의 길이 구하기
print(len(python))
# python의 Python을 Java로 교체
print(python.replace("Python","Java"))

# python 안의 "n"의 위치 출력 (첫번째)
index = python.index("n")
print(index)

# index+1 이후부터의 "n"의 위치 출력
index = python.index("n", index+1)
print(index)

# python.index("n")과 동일
print(python.find("n"))

# python에 없는 텍스트 찾는 경우,
# find는 없으면 -1 출력 / index 는 에러 발생
print(python.find("Java"))
# print(python.index("Java"))

# python 내부의 "n"의 개수 출력
print(python.count("n"))


## 문자열 포멧

# 방법1
print("나는 %d살입니다." %20)
print("나는 %s를 좋아해요" %"파이썬")
print("Apple 은 %c로 시작해요" %"A")

# %s를 사용하면 값과 관계없이 출력할수 있음.
print("나는 %s살입니다." %20.323)

print("나는 %s색과 %s색을 좋아해요" %("분홍", "하늘"))

# 방법2
print("나는 {}살입니다.".format(20))
# format의 index값을 지정하여 뒤의 출력순서변경 가능.
print("나는 {1}색과 {0}색을 좋아해요" .format("분홍", "하늘"))


# 방법3
print("나는 {age}살이며, {color}색을 좋아해요."\
      .format(age = 20, color = "분홍"))
print("나는 {age}살이며, {color}색을 좋아해요."\
      .format(color = "하늘", age = 29))

# 방법4
age = 20
color = "분홍"
# 큰따옴표 앞에 f로 시작.
print(f"나는 {age}살이며, {color}색을 좋아해요.")


## 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
# \", \' : 문장 내에서 따옴표를 사용가능
print("저는 \"조희진\"입니다.")

# \+문자 : 탈출문자가 된다.
# \사용을 위해서는 \\를 사용해야 함.
print("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python")

# \r : 커서를 맨 앞으로 이동.
print("Red apple \rPine") # PineRed apple

# \b : backspae, 한 글자 삭제
print("Redd\bApple")

# \t : tap
print("Red\tApple")


## 퀴즈
'''
사이트별 비밀번호를 만들어주는 프로그램 작성.
http://naver.com
1. http://, 처음 만나는 . 이후 부분 제외 => naver
2. 남은 글자 중 처음 세자리 + 글자개수 + 글자 내 'e'개수 + "!" 로 구성
ex ) nav51!
'''

# 내 답변
site = "http://naver.com"
site = site[site.find("//")+2:site.find(".")]
site = site+str(len(site))+str(site.count("e"))+"!"
print(site)

# 선생님 답변
site = "http://naver.com"
site = site.replace("http://", "")
site = site[:site.index(".")]
site = site+str(len(site))+str(site.count("e"))+"!"
print(site)
