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

## 4 키보드 이벤트
#4 이동할 좌표
to_x = 0
to_y = 0

#5 이동속도
character_speed = 0.3


##5 FPS
# 프레임 수가 높을수록 부드럽다.
clock = pygame.time.Clock()


#1 이벤트 루프
#1 화면이 켜지자마자 꺼지지 않도록 함.
runnig = True # 게임이 진행중인가?
while runnig:
    #5 게임화면의 초당 프레임수를 설정함.
    dt = clock.tick(80)
    print("fps : {}".format(clock.get_fps()))

    #1 사용자로부터 키보드/마우스 이벤트가 들어오는 지 체크함.
    #1 들어온다면 액션에 맞는 이벤트를 진행함. 
    for event in pygame.event.get():
        #1 여러 이벤트 중 들어온 이벤트가 QUIT이라면 runnig 은 False
        #1 창이 닫히는 이벤트가 발생하였는지 확인함.
        if event.type == pygame.QUIT:
            runnig = False
        
        #4 키보드가 눌렸는지 확인.
        if event.type == pygame.KEYDOWN:
            #4 캐릭터를 왼쪽으로
            if event.key == pygame.K_LEFT:
                to_x -=character_speed
            #4 캐릭터를 오른쪽으로
            elif event.key == pygame.K_RIGHT:
                to_x +=character_speed
            #4 캐릭터를 위쪽으로
            elif event.key == pygame.K_UP:
                to_y -=character_speed
            #4 캐릭터를 아래쪽으로
            elif event.key == pygame.K_DOWN:
                to_y +=character_speed
        #4 키보드에서 손을 떼면
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    #4 이 부분이 for문 안에 들어가있으면 키 입력마다 작동하고
    #4 이 부분이 for문 밖에 들어가있으면 연속 키누름에도 작동됨

    #5 캐릭터가 1초에 100만큼 이동해야할 떄,
    #5 10fps : 1초동안 10번 동작 > 1번에 10만큼 이동해야함
    #5 20fps : 1초동안 20번 동작 > 1번에 5만큼 이동해야함.
    #5 즉, 이동하는 곳에 dt
    character_x_pos +=to_x*dt
    character_y_pos +=to_y*dt

    #4 가로 경계값 처리
    if character_x_pos < 0 : 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #4 세로 경계값 처리
    if character_y_pos < 0 : 
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

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

