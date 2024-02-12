# 01. 파이썬 기초 (리스트, 딕셔너리)

a_list = ['사과', '배', '감', '수박']
a_list.append('딸기')
a_list[4] # 딸기

a_dict = {'name' : 'heejin', 
         'age' : 30}
a_dict['age']
a_dict['height'] = 167

a_list = [a_dict, {'name' : 'youjin', 
         'age' : 28}]

print(a_list[1]['age'])
# 28

# 02. 업무 자동화 - 스크래핑 실습

from openpyxl import Workbook
from bs4 import BeautifulSoup
from datetime import datetime
import requests

def get_news(keyword):
    wb = Workbook()
    ws = wb.active

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    data = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}', headers=headers)
    data.raise_for_status()

    soup = BeautifulSoup(data.text, 'html.parser')
        #main_pack > section.sc_new.sp_nnews._fe_news_collection._prs_nws > div.api_subject_bx > div.group_news > ul

    list =soup.select('ul.list_news._infinite_list > li')
    # a = list[0].select_one('a.news_tit')
    # print(a['href'])

    for a in list:
        a = a.select_one('a.news_tit')
        row = [a.text, a['href']]
        ws.append(row)
        print(a.text, a['href'])
    print("====================================================================")

    today = datetime.today().strftime("%Y-%m-%d")
    wb.save(f"{today}_{keyword}.xlsx")
    wb.close()
# s1 을 직접 실행했을 때만 실행됨.
if __name__ == "__main__":
    while True:
        keyword = input("검색어 : ")
        if len(keyword)<=0:
            break
        get_news(keyword)