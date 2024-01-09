from openpyxl import Workbook

#새 워크북 생성
wb = Workbook()
#활성화된 시트를 가져옴
ws = wb.active 
#시트의 이름을 변경함.
ws.title = "루샵"
wb.save("sample.xlsx")
wb.close()