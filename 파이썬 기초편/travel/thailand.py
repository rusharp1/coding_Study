class ThailandPackage:
    def detail(self):
        print("태국 패키지 3박5일 방콕, 파타야 여행(야시장 투어) 50만원")


## 모듈 직접 설정.
# 패키지/모듈을 만들 때 모듈이 잘 작동되는지 확인해야 함.
# name == main이면, 즉 Thailand.py 에서 코드를 직접 실행했을 때, 
# 해당 문장은 함수호출로 실행하지 않더라도 호출되는 순간 바로 실행된다.
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행됩니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else : 
    print("Thailand 외부에서 모듈 호출")
