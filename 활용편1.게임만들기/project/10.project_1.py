
##1 환경설정 & 프레임

######################################################################
# 무조건 해야하는 부분
######################################################################
import pygame
import os

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("rusharp Pang") # 게임 이름

# 객체 생성
current_path = os.path.dirname(__file__)
current_path = os.path.join(current_path, "image")

print()
# background
background = pygame.image.load(os.path.join(current_path, "background.png"))
wd, bd = -1,-1

# stage 
stage = pygame.image.load(os.path.join(current_path, "stage.png"))
stage_rect = stage.get_rect()
stage_height = stage_rect.height

# 캐릭터
character = pygame.image.load(os.path.join(current_path, "character.png"))
character_rect = character.get_rect()
character_width = character_rect.width
character_height = character_rect.height
character_x = (screen_width - character_width) / 2
character_y = screen_height - character_height-stage_height
to_left = 0
to_right = 0
chracter_speed = 3

# 공
ball_image = [pygame.image.load(os.path.join(current_path, "balloon1.png")),
         pygame.image.load(os.path.join(current_path, "balloon2.png")),
         pygame.image.load(os.path.join(current_path, "balloon3.png")),
         pygame.image.load(os.path.join(current_path, "balloon4.png"))]

ball_speed = [-18, -15, -12, -9]
balls = []
balls.append({"x": 50,
              "y": 50,
              "img_idx" : 0,
              "to_x": 3,
              "to_y": -6,
              "init_speed_idx" : 0})
# balls_rect = balls.get_rect()
# balls_width = balls_rect.width
# balls_height = balls_rect.height
# balls_x = balls_rect.x
# balls_y = balls_rect.y

# 무기
weapon_img = pygame.image.load(os.path.join(current_path, "weapon.png"))
weapons = []
weapon_rect = weapon_img.get_rect()
weapon_width = weapon_rect.width
weapon_height = weapon_rect.height
weapon_speed = 6
# weapons_x = weapons_rect.x
# weapons_y = weapons_rect.y

game_font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()
init_time = pygame.time.get_ticks()
total_time = 15

# 모든 공을 없애면 게임종료(성공) : MISSON COMPLETE
# 캐릭터가 공에 닿으면 게임 종료 : GAME OVER
# 시간이 초과되면 게임 종료 : TIME OVER

message = "GAME OVER"


running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # 캐릭터 좌우 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left -=chracter_speed
            elif event.key == pygame.K_RIGHT:
                to_right +=chracter_speed
            # 스페이스를 누르면 weapons에 출력 추가
            elif event.key == pygame.K_SPACE:
                weapons.append([character_x+character_width/2 -weapon_width/2,
                                character_y])
        # 키보드에서 손을 떼면 좌우이동 멈춤.        
        if event.type == pygame.KEYUP:
            to_left = 0
            to_right = 0
    # 캐릭터 좌우이동 확인.
    character_x = character_x + to_left+to_right
    # 공 튕기기
    for ball in balls:
        # 공 가로 크기 위치 가져오기
        ball_img_idx = ball["img_idx"]
        ball_width = ball_image[ball_img_idx].get_rect().size[0]
        ball_height = ball_image[ball_img_idx].get_rect().size[1]
        # 공이 좌우 위치를 넘어가면 더하는 값에 -1을 곱함.
        if ball["x"]<=0 or ball["x"]>=screen_width - ball_width:
            ball["to_x"] *= -1
        # 공의 높이가 stage_heght보다 작아지면 속도 초기화
        if ball["y"]> screen_height-stage_height-ball_height:
            ball["to_y"] = ball_speed[ball_img_idx]

        ball["to_y"] +=0.5
        ball["x"] += ball["to_x"]
        ball["y"] += ball["to_y"]

    # 공과 캐릭터가 충돌할 경우
    # 캐릭터rect 지정
    character_rect.x = character_x
    character_rect.y = character_y 
    for ball_idx, ball_val in enumerate(balls):
        # 공 이미지 인덱스 가져오기
        ball_img_idx = ball_val["img_idx"]
        # 공 이미지의 rect값 가져오기.
        ball_img_rect = ball_image[ball_img_idx].get_rect()
        ball_img_rect.x =  ball_val["x"]
        ball_img_rect.y =  ball_val["y"]
        # 공 가로크기 / 세로크기 가져오기
        ball_width = ball_img_rect.width
        ball_height = ball_img_rect.height
        
        if ball_img_rect.colliderect(character_rect):
            running = False
            break
        for weapon_idx , weapon_val in enumerate(weapons):
            # 위에서 1회 호출됨
            # 공과 충돌여부를 확인하ㅣ기 위해 무기 rect 가져옴.
            # weapon_rect = weapon_img.get_rect()
            weapon_rect.x = weapon_val[0]
            weapon_rect.y = weapon_val[1]
            if weapon_rect.colliderect(ball_img_rect):
                # 삭제할 공 인덱스 / 무기 인덱스 저장하기.
                bd = ball_idx
                wd = weapon_idx
                # 공 index가 3보다 작으면 즉, 가장작은 공이 아니면.
                if ball_img_idx < 3:
                    new_ball_width = ball_image[ball_img_idx+1].get_rect().width
                    new_ball_height = ball_image[ball_img_idx+1].get_rect().height
                    # 공을 삭제하고 새로생긴 공 추가하기
                    # 공의 x값 / y값 계산
                    new_ball_x = ball_val["x"]+ball_width/2-new_ball_width/2
                    new_ball_y = ball_val["y"]+ball_height/2-new_ball_height/2
                    balls.append({"x": new_ball_x,
                                "y": new_ball_y,
                                "img_idx" : ball_img_idx+1,
                                "to_x": 3,
                                "to_y": -6,
                                "init_speed_idx" : 0})
                    balls.append({"x": new_ball_x,
                                "y": new_ball_y,
                                "img_idx" : ball_img_idx+1,
                                "to_x": -3,
                                "to_y": -6,
                                "init_speed_idx" : 0})
                break
        else : continue
        break
    if wd > -1:
        del weapons[wd]
        wd = -1
    if bd > -1:
        del balls[bd]
        bd = -1

    if len(balls) <=0:
        message = "MISSON COMPLETE"
        running = False
    
    timer = total_time - (pygame.time.get_ticks() - init_time) // 1000
    if timer <=0:
        message = "TIME OVER"
        running = False
    
    # 게임이 10초 미만으로 남으면 빨간색으로 출력.
    if timer>10:
        timer = game_font.render("Time : {}".format(timer), True, (0,0,0))
    else:
        timer = game_font.render("Time : {}".format(timer), True, (255,0,0))
    # weapons = [[w[0], w[1]-weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]-weapon_speed] for w in weapons if w[1]>0]

    screen.blit(background,(0,0))
    for w in weapons:
        screen.blit(weapon_img, (w[0], w[1]))

    for idx, ball in enumerate(balls):
        screen.blit(ball_image[ball["img_idx"]], (ball["x"], ball["y"]))
    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_x, character_y))
    screen.blit(timer, (10, 10))

    pygame.display.update()

msg = game_font.render(message, True, (255,255,0))
msg_rect = msg.get_rect(center = (screen_width/2, screen_height/2))
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()
