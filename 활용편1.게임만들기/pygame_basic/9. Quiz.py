'''
똥피하기 게임
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능.
2. 똥은 가장 위에서 떨어짐, x좌표는 랜덤으로 설정.
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정.
'''

import pygame
import random
pygame.init()

# 배경 크기 설정 
screen = pygame.display.set_mode((480, 640))

# 배경/캐릭터/적 이미지 불러오기
background = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\background.png")
character = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\character.png")
enemy = pygame.image.load("C:\\Users\\shop2\\OneDrive\\바탕 화면\\python\\활용편1.게임만들기\\pygame_basic\\enemy.png")


character_rect = character.get_rect()
character_x_max = background.get_rect().width - character_rect.width
# 캐릭터 초기 가로/세로 위치 설정 : 화면 중앙, 화면 최하단
character_x = character_x_max/2
character_y = background.get_rect().height - character_rect.height
# 적 초기 가로/세로 위치 설정 : 랜덤 위치, 화면 최상단
enemy_rect = enemy.get_rect()
enemy_x = random.randint(0,background.get_rect().width - enemy_rect.width)
enemy_y = 0

# 캐릭터/적 스피드 설정
character_speed = 1
enemy_speed = 0.5

# 이동 좌표
to_x = 0

# 게임 이름 설정
pygame.display.set_caption("똥피하기 게임") 

time = pygame.time.Clock()
start_time = pygame.time.get_ticks()

Font = pygame.font.Font(None, 40)

running = True
while running:
    # frame 30으로 설정함.
    tick = time.tick(30)
    # 닫기버튼 선택 시, 게임종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            to_x = 0
    
    character_x += to_x*tick
    enemy_y += enemy_speed*tick

    # 캐릭터가 화면 가로 범위를 넘어가지 못하게 설정
    if character_x <=0:
        character_x = 0
    elif character_x > character_x_max:
        character_x = character_x_max
    
    # 똥이 바닥에 떨어지면 위치 초기화
    if enemy_y >= background.get_rect().height:
        enemy_y = 0
        enemy_x = random.randint(0,background.get_rect().width - enemy.get_rect().width)

    character_rect.x = character_x
    character_rect.y = character_y

    enemy_rect.x = enemy_x
    enemy_rect.y = enemy_y

    if character_rect.colliderect(enemy_rect):
        print("충돌하였습니다. 게임 종료.")
        running = False

    send_time = (pygame.time.get_ticks() - start_time)//1000
    print("send_time : ", send_time)
    timer = Font.render(str(send_time),True, (0,0,0))

    # 몰랐던 사실!! blit호출 순서대로 화면 상단에 노출된다.
    screen.blit(background,(0,0))
    screen.blit(character,(character_x, character_y))
    screen.blit(enemy,(enemy_x,enemy_y))
    screen.blit(timer, (10,10))
    
    pygame.display.update()
