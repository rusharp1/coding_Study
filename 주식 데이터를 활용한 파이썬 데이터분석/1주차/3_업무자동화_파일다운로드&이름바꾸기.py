from s1_python_foundation_scraping import get_news
import os

# keywords 내 모든 key 에 따라 진행
keywords = ['삼성전자','LG에너지솔루션','SK하이닉스','NAVER','삼성바이오로직스',
            '삼성전자우','카카오','삼성SDI','현대차','LG화학','기아','POSCO홀딩스',
            'KB금융','카카오뱅크','셀트리온','신한지주','삼성물산','현대모비스','SK이노베이션',
            'LG전자','카카오페이','SK','한국전력','크래프톤','하나금융지주','LG생활건강',
            'HMM','삼성생명','하이브','두산중공업','SK텔레콤','삼성전기','SK바이오사이언스',
            'LG','S-Oil','고려아연','KT&G','우리금융지주','대한항공','삼성에스디에스',
            '현대중공업','엔씨소프트','삼성화재','아모레퍼시픽','KT','포스코케미칼',
            '넷마블','SK아이이테크놀로지','LG이노텍','기업은행']

for k in keywords:
    get_news(k)

# 현재 폴더 하위에 위치해있기 때문에 괄호안을 빈칸으로 둠.
# 필요 시, path 지정 후 괄호안에 path 변수 사용
# path = 'C:/Users/owner/Desktop/coding'
files = os.listdir()


for name in files:
    if '2024-01-22' in name:
        # 새로운 이름 지정
        new_name = name.split('xlsx')[0] + '(뉴스).' + name.split('.')[1]
        # name 에 포함되는 파일을 new_name으로 이름변경
        os.rename(name,new_name)
        print(name+"변경 완료")
        # os.remove(name)
        # print(name+"삭제 완료")
    