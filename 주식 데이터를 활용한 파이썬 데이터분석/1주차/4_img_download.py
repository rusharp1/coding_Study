import urllib.request
def img_download(file_name, code):
    # 이미지 주소 넣어서 다운로드 받기.
    print(file_name, code)
    url = f'https://ssl.pstatic.net/imgfinance/chart/item/area/day/{code}.png?sidcode=1705920189386'
    urllib.request.urlretrieve(url, f'{file_name}.png')