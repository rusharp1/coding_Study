from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

# C3위치에 img.png 파일의 이미지 삽입.
img = Image("img.png")
ws.add_image(img, "C3")

wb.save("sample_image.xlsx")