##1 환경설정 & 프레임

######################################################################
# 무조건 해야하는 부분
######################################################################
import pygame
#1 초기화 (반드시 필요.) 
pygame.init()

#1 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#1 화면 타이틀 설정
pygame.display.set_caption("rusharp Game") # 게임 이름

######################################################################
# 사용자 게임 초개화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
######################################################################

##2 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\background.png")

##3 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\character.png")
#3 캐릭터 사이즈를 가져옴 (가로/세로 크기)
character_size = character.get_rect().size
print("character_size : ",character_size)
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

##6 충돌 처리
#6 적 (enemy) 캐릭터
enemy = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\enemy.png")
#6 캐릭터 사이즈를 가져옴 (가로/세로 크기)
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
#6 캐릭터가 움직일수 있는 가로/세로 범위
enemy_x_pos = (screen_width-enemy_width)/2
enemy_y_pos = (screen_height-enemy_height)/2

##7 텍스트
#7 폰트 정의 : 폰트 객체 생성, (폰트, 크기)
game_font = pygame.font.Font(None, 40)
total_time = 10
#7 시작 시간 정보를 받아옴.
start_ticks = pygame.time.get_ticks()

#1 이벤트 루프
#1 화면이 켜지자마자 꺼지지 않도록 함.
running = True # 게임이 진행중인가?
while running:
    #5 게임화면의 초당 프레임수를 설정함.
    dt = clock.tick(60)

    #1 사용자로부터 키보드/마우스 이벤트가 들어오는 지 체크함.
    #1 들어온다면 액션에 맞는 이벤트를 진행함. 
    for event in pygame.event.get():
        #1 여러 이벤트 중 들어온 이벤트가 QUIT이라면 runnig 은 False
        #1 창이 닫히는 이벤트가 발생하였는지 확인함.
        if event.type == pygame.QUIT:
            running = False
        
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

    #6 충돌 처리
    #6 실제로 캐릭터 자체의 rect 이미지는 처음 호출한 위치에 고정되어 있다.
    character_rect = character.get_rect()
    print("character.get_rect() :", character_rect)
    print("character_rect.left : ",character_rect.left)
    print("character_rect.top : ",character_rect.top)

    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    # 직접적으로 enemy_rect 에 반영된 것이 아니기 때문에 직접 업데이트해야함.
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #6 충돌 체크
    #6 colliderect : Rect와 자신에게 겹침이 있는지 없는지(충돌)를 반환
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    #2 원하는 rgb색상으로 화면을 채움.
    #2 screen.fill((0,0,255))
    #2 원하는 이미지(background)가 0.0 좌표를 시작으로 배경을 그려줌.
    screen.blit(background, (0,0))
    
    #3 캐릭터를 그려줌.
    screen.blit(character, (character_x_pos, character_y_pos))
    
    #6 적을 그려줌.
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    #7 타이머 집어넣기
    #7 경과시간을 1000으로 나누어서 초단위로 표시
    elspsed_time = (pygame.time.get_ticks() - start_ticks)//1000
    #7 timer 에 GUI에서 열 수 있는 텍스트를 삽입함(character 처럼)
    timer = game_font.render(str(total_time - elspsed_time),True, (0,0,0))

    #7 만약 시간이 0 이하이면 게임 종료
    if total_time - elspsed_time <=0:
        timer = game_font.render("Time out",True, (0,0,0))
        running = False

    screen.blit(timer, (10,10))

    # #7 만약 시간이 0 이하이면 게임 종료
    # if total_time - elspsed_time <=0:
    #     print("타임아웃")
    #     running = False

    #2 게임 화면을 다시 그리기
    #2 아래 내용이 없는 경우, 화면이 한번 보여지고 바로 초기화(검정)됨.
    pygame.display.update()

#7 종료 직전 잠시 대기할 수 있는 코드
pygame.time.delay(2000)

#1 pygame 종료
pygame.quit()

