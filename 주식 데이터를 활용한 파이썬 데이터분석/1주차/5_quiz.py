import openpyxl
import os
from s4_img_download import *
wb = openpyxl.load_workbook("관리종목.xlsx")
# ws = wb['종목'] 을 통해서 원하는 시트 위치로 이동함.
ws = wb.active

rows =list(ws.rows)[1:]
# row[0] : 종목명 / row[1] : 종목코드
for row in rows:
    img_download(row[0].value, row[1].value)


# 위에서 다운로드받은 파일 전체 삭제.
# files = os.listdir()

# for name in files:
#     if 'png' in name:
#         # 새로운 이름 지정
#         # name 에 포함되는 파일을 new_name으로 이름변경
#         os.remove(name)
#         print(name+"삭제 완료")
    