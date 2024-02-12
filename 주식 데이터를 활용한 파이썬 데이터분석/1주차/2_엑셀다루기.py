import openpyxl


wb= openpyxl.load_workbook("sample.xlsx")
ws = wb.active
print(ws['A1'].value)

# 번호, 국어, 영어, 컴퓨터, 수학 모두 불러오기
rows = ws.rows
for row in rows:
    for column in row:
        print(column.value, end="\t")
    print()

# 번호 영역을 제외하고 모두 불러오기
rows = list(ws.rows)[1:]
for row in rows:
    for column in row:
        print(column.value, end="\t")
    print()
