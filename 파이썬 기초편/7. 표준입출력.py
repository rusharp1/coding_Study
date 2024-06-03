## 표준입출력
# sep = , 에 뭐가들어갈지 정할 수 있음.
# end = print문 끝에 원하는 텍스트를 넣을 수 있음.
print("Python","Java", "C#",sep = " vs ", end = "?")
print("무엇이 더 재밌을까요?")

import sys
# 표준출력으로 문장이 출력된다.
print("Python","Java", "C#",file = sys.stdout)
# 표준에러로 문장이 출력된다. 사용 에러가 난 부분을 쉽게 찾을 수 있음.
print("Python","Java", "C#",file = sys.stderr)

scores = {"수학":50, "영어":100, "코딩":80}
# for문에 dictionary사용 시, 아이템을 2개씩 받아야 한다.
for subject, score in scores.items():
    # ljust(n) = n개의 공간 확보 후 좌측정렬
    # rjust(n) = n개의 공간 확보 후 우측정렬
    print(subject.ljust(5), str(score).rjust(4), sep= ":")


for num in range(1,21,3):
    # zfill(n) = n개의 공간 중 빈칸을 `0`으로 채움
    print("대기번호 :",str(num).zfill(3))

# # input값은 무조건 string 타입으로 들어감
# answer = input("아무 값이나 입력하세요 : ")
# print("입력 값은 {}입니다.".format(answer))

## 다양한 출력포맷
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일땐 +, 음수일땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬 후 빈칸을 _로 채움
print("{0:_<10}".format(500))

# 3자리마다 콤마 찍어주기
print("{0:,}".format(100000000000))
# 3자리마다 콤마, +-부호
print("{0:+,}".format(100000000000))
# 3자리마다 콤마, +-부호, 자릿수 확보(30), 빈자리는 _
print("{0:_<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 n째 자리까지 표시 (n+1자리에서 반올림)
print("{0:.2f}".format(5/3))

## 파일입출력
# 파일을 쓰기용으로 열음
score_file = open("score.txt","w", encoding="utf8")
print("수학 : 0",file=score_file)
print("영어 : 50",file=score_file)
print("코딩 : 100",file=score_file)
# 파일을 열었을 때 반드시 닫아줘야 함.
score_file.close()


# append, 즉 덮어쓰기용으로 파일을 열음
score_file = open("score.txt","a", encoding="utf8")
# 변수명.write로 텍스트 입력 시, 줄바꿈되지 않음.
score_file.write("과학 : 80\n")
score_file.write("코딩 : 100")
# 파일을 열었을 때 반드시 닫아줘야 함.
score_file.close()

# read, 즉 읽기용으로 파일을 열음.
score_file = open("score.txt","r", encoding="utf8")
# 현재 커서가 있는 한줄을 읽고 출력함.
# 다만 readline, print 모두 줄바꿈이 있어서 줄바꿈이 2회됨.
print("score_file.readline()")
print(score_file.readline())
# 파일의 모든 내용을 읽고 출력함.
print("score_file.read()")
print(score_file.read())
score_file.close()

# 파일이 몇줄인지 모를 때 처리방법
# 무한반복 사용.
score_file = open("score.txt","r", encoding="utf8")
index = 0
while(True):
    line = score_file.readline()
    if not line:
        break
    index +=1
    print("{} : {}".format(index, line), end = "")
score_file.close()

print()
# list 사용
score_file = open("score.txt","r", encoding="utf8")
index = 0
# lines에 한줄씩 리스트로 불러옴.
lines = score_file.readlines()
for line in lines:
    index +=1
    print("{} : {}".format(index, line), end = "")
score_file.close()
print()


## pickle
# 사용하고 있는 데이터를 파일형태로 저장 후 재사용할 수 있음.
import pickle
# write biinary, pickle타입은 무조건 binary 타입을 정의해야함.
profile_file = open("profile.pickle","wb")
profile = {"이름":"조희진", "나이":30, "취미":["영어", "게임", "코딩"]}
print(profile)
# profile에 있는 정보를 file에 저장.
pickle.dump(profile,profile_file)
profile_file.close()

# read biinary, pickle타입은 무조건 binary 타입을 정의해야함.
profile_file = open("profile.pickle","rb")
# profile_file에 있는 정보를 profile 에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()


## with
# profile.pickle을 열어 profile_file이라는 변수에 저장.
# 이 파일 내용을 pickle.load를 퉁해 불러오기함.
# close를 할 필요가 없음.
with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))

with open("score.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 공부하고 있어요.")

with open("score.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


## 퀴즈
'''
매주 1회 보고서 작성해야 하며 형식이 지정되어있음 (참고)
1~5주차까지 보고서 파일을 만드는 프로그램 작성.
'''
for i in range(1,6):
    with open("{} 주차.txt".format(i), "w",encoding="utf8") as report:
        report.write("- {}주차 주간보고 -\n".format(i))
        report.write("부서 : \n이름 : \n업무 요약 : ")
