from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active
# 8번째 행이 추가됨 (빈 상태)
ws.insert_rows(8)
# 8번째 행에 5줄이 추가됨 (빈 상태)
ws.insert_rows(8, 5)

ws.delete_rows(8,6)
# B 열이 추가됨
ws.insert_cols(2)
ws.insert_cols(2, 3)

ws.delete_cols(2,4)
wb.save("sample.xlsx")