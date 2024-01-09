##1 환경설정 & 프레임

import pygame
#1 초기화 (반드시 필요.)
pygame.init()

#1 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#1 화면 타이틀 설정
pygame.display.set_caption("rusharp Game") # 게임 이름

##2 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\background.png")

##3 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\character.png")
#3 캐릭터 사이즈를 가져옴 (가로/세로 크기)
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
#3 캐릭터가 움직일수 있는 가로/세로 범위
character_x_pos = (screen_width-character_width)/2
character_y_pos = screen_height-character_height

#1 이벤트 루프
#1 화면이 켜지자마자 꺼지지 않도록 함.
runnig = True # 게임이 진행중인가?
while runnig:
    #1 사용자로부터 키보드/마우스 이벤트가 들어오는 지 체크함.
    #1 들어온다면 액션에 맞는 이벤트를 진행함. 
    for event in pygame.event.get():
        #1 여러 이벤트 중 들어온 이벤트가 QUIT이라면 runnig 은 False
        #1 창이 닫히는 이벤트가 발생하였는지 확인함.
        if event.type == pygame.QUIT:
            runnig = False

    #2 원하는 rgb색상으로 화면을 채움.
    #2 screen.fill((0,0,255))
    #2 원하는 이미지(background)가 0.0 좌표를 시작으로 배경을 그려줌.
    screen.blit(background, (0,0))
    
    #3 캐릭터를 그려줌.
    screen.blit(character, (character_x_pos, character_y_pos))

    #2 게임 화면을 다시 그리기
    #2 아래 내용이 없는 경우, 화면이 한번 보여지고 바로 초기화(검정)됨.
    pygame.display.update()



#1 pygame 종료
pygame.quit()

