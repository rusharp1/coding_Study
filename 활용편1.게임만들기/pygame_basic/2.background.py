## 환경설정 & 프레임

import pygame
# 초기화 (반드시 필요.)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("rusharp Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\background.png")

# 이벤트 루프
runnig = True # 게임이 진행중인가?
while runnig:
    # 사용자로부터 키보드/마우스 이벤트가 들어오는 지 체크함.
    # 들어온다면 액션에 맞는 이벤트를 진행함.
    for event in pygame.event.get():
        # 여러 이벤트 중 들어온 이벤트가 QUIT이라면 runnig 은 False
        # 창이 닫히는 이벤트가 발생하였는지 확인함.
        if event.type == pygame.QUIT:
            runnig = False

    # 원하는 rgb색상으로 화면을 채움.
    # screen.fill((0,0,255))

    # 원하는 이미지(background)가 0.0 좌표를 시작으로 배경을 그려줌.
    screen.blit(background, (0,0))
    # 게임 화면을 다시 그리기
    pygame.display.update()
# pygame 종료
pygame.quit()

