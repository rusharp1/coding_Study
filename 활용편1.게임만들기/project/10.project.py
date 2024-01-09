'''
오락실 pang게임 만들기.
1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
2. 스페이스를 누르면 무기를 쏘아 올림
3. 큰 공 1개가 나타나서 바운스
4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
5. 모든 공을 없애면 게임종료(성공)
6. 캐릭터가 공에 닿으면 게임 종료 (실패)
7. 시간 제한 99초 초과 시 게임 종료 (실패)
8. FPS는 30으로 고정

'''
##1 환경설정 & 프레임

######################################################################
# 무조건 해야하는 부분
######################################################################
import pygame
import os
#1 초기화 (반드시 필요.) 
pygame.init()

#1 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("rusharp Pang") # 게임 이름

######################################################################
# 사용자 게임 초개화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
######################################################################

# 지금 수행하고 있는 파일의 위치를 반환.
current_path = os.path.dirname(__file__)
print(current_path)
# 이미지 폴더 위치 반환
image_path = os.path.join(current_path,"image")
print(image_path)

# background.png파일 가져오기
backgrouond = pygame.image.load(os.path.join(image_path, "background.png"))
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
# stage_size[0] : 가로 / stage_size[1] : 세로
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
# character_size = character.get_rect().size
character_rect = character.get_rect()
character_width = character_rect.size[0]
character_height = character_rect.size[1]

character_x =(screen_width - character_width)/ 2
character_y = screen_height - character_height - stage_height

# 캐릭터 속도/이동
character_speed = 5
to_right = 0
to_left = 0

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_width = weapon.get_rect().size[0]
weapon_height = weapon.get_rect().size[1]
# 여러번 발사를 위한 리스트 변수
weapons = []
weapon_speed = 10

# 공 만들기 (크기가 4종류)
ball_image = [pygame.image.load(os.path.join(image_path, "balloon1.png")),
              pygame.image.load(os.path.join(image_path, "balloon2.png")),
              pygame.image.load(os.path.join(image_path, "balloon3.png")),
              pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

# 공 리스트
# 최초 발생하는 큰 공 추가, dictionary 타입
balls = []
balls.append({"pos_x" : 50, #공의 x좌표
              "pos_y" : 50, #공의 y좌표
              "img_idx" : 0, #공의 이미지 인덱스 (ball_image[n])
              "to_x" : 3, #공의 x축 이동방향 (-3 : 좌 / 3 : 우)
              "to_y" : -6, # 공의 y축 이동방향
              "init_spe_y": ball_speed_y[0]}) # y축의 최초 속도

# 게임종료 조건 처리 (시간)
# Font정의
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks() # 시작시간정의

# 게임 종료 메시지
# Time out : 시간 종료.
# Mission Complete : 공을 모두 제거
# Game Over : 공에 맞음
game_result = "Game Over"

# 사라질 무기와 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1


running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left -=character_speed
            elif event.key == pygame.K_RIGHT:
                to_right +=character_speed
            # 무기 발사
            if event.key == pygame.K_SPACE:
                weapon_x = character_x +(character_width-weapon_width)/2
                weapon_y = character_y
                weapons.append([weapon_x, weapon_y])
        elif event.type == pygame.KEYUP:
            to_left = 0
            to_right = 0

    character_x =character_x + to_right + to_left
    if character_x < 0:
        character_x = 0
    elif character_x > screen_width-character_width:
        character_x = screen_width-character_width

    # 무기 위치 조절 (y를 점점 위로 올림)
    weapons = [ [w[0], w[1] -weapon_speed] for w in weapons]

    # 천장에 닿은 무기 없애기
    # weapons = []
    # for w in weapons:
    #     if w[1] > 0:
    #         weapons.append = [w[0], w[1]]
    # 즉, weaponse 의 높이가 0보다 클때만 weapons 값을 추가함.
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 위치 정의
    # enumerate : ball list 의 것들을 가져와서 index 번호, 값을 가져옴
    for ball_val in balls:
        # ball 가로/세로 위치/ 공의 이미지 인덱스 지정
        # 초기값의 경우, 50, 50, 0 이다.
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_image[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        # 볼 가로가 화면밖으로 나가는 경우, 공 방향 변경
        if ball_pos_x < 0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] *= -1
        # 공 세로가 바닥에 닿는 경우, 속도 초기화
        if ball_pos_y > screen_height-ball_height-stage_height:
            ball_val["to_y"] = ball_val["init_spe_y"]
        # 그외에는 속도를 증가함.
        else:
            ball_val["to_y"]+=0.5
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 공과 캐릭터가 충돌하는 케이스
    character_rect.x = character_x
    character_rect.y = character_y

    for ball_idx, ball_val in enumerate(balls):
        # 공 쪼개기 시작값을 위한 위치 받아오기
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        # 공 rect 정보 업데이트 
        ball_rect = ball_image[ball_val["img_idx"]].get_rect()
        ball_rect.x = ball_val["pos_x"]
        ball_rect.y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        
        if ball_rect.colliderect(character_rect):
            print("공과 사용자가 충돌하였습니다.")
            running = False
            break
    
        # 공과 무기가 충돌하는 케이스
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_val[0]
            weapon_rect.top = weapon_val[1]
            if weapon_rect.colliderect(ball_rect):
                # 충돌하면 무기와 공을 제거해야함.
                # 없애기 위한 공과 무기 index 받아옴.
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx
                # 공 2개로 만들어서 하나는 왼쪽/하나는 오른쪽으로 만듬
                # 가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나누어주기.
                if ball_img_idx < 3:
                    # 현재 공 크기의 정보를 가지고옴.
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                    # 나눠진 공 정보
                    small_ball_rect = ball_image[ball_img_idx+1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]
                    # 왼쪽으로 튕겨나가는 공
                    balls.append({"pos_x" : ball_pos_x + (ball_width - small_ball_width)/2, #공의 x좌표
                            "pos_y" : ball_pos_y + (ball_height - small_ball_height)/2, #공의 y좌표
                            "img_idx" : ball_img_idx+1, #공의 이미지 인덱스 (ball_image[n])
                            "to_x" : -3, #공의 x축 이동방향 (-3 : 좌 / 3 : 우)
                            "to_y" : -6, # 공의 y축 이동방향
                            "init_spe_y": ball_speed_y[ball_img_idx+1]}) # y축의 최초 속도})
                    balls.append({"pos_x" : ball_pos_x + (ball_width - small_ball_width)/2, #공의 x좌표
                            "pos_y" : ball_pos_y + (ball_height - small_ball_height)/2, #공의 y좌표
                            "img_idx" : ball_img_idx+1, #공의 이미지 인덱스 (ball_image[n])
                            "to_x" : 3, #공의 x축 이동방향 (-3 : 좌 / 3 : 우)
                            "to_y" : -6, # 공의 y축 이동방향
                            "init_spe_y": ball_speed_y[ball_img_idx+1]}) # y축의 최초 속도})
                # 해당부분은 `for weapon_idx~` 부분만 탈출함
                '''2중 탈출을 하고싶을 때
                for문1 : 
                    for문2 :
                        if 조건 : 액션
                            break
                    else: # 조건이 맞지 않으면 continue를 진행하여 for1을 작동함.
                        continue
                    break
                이렇게하면 break를 만나면 for문1도 break
                '''
                break
        else : continue # for문이 진행중이면 계속 진행 
        break

    # 충돌한 공  or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
        
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 공이 더이상 없을 때(balls 크기가 0일 때)
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000
    timer = game_font.render("Time : {}".
                             format(int(total_time - elapsed_time)), True, (0,0,0))

    if total_time-elapsed_time <= 0:
        game_result = "Time Over"
        running = False
    

    # 화면 출력
    screen.blit(backgrouond,(0,0))
    for weapon_x, weapon_y in weapons:
        screen.blit(weapon, (weapon_x, weapon_y))

    for idx, val in enumerate(balls):
        ball_x = val["pos_x"]
        ball_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_image[ball_img_idx], (ball_x, ball_y))

    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_x, character_y))
    screen.blit(timer,(10,10))


    pygame.display.update()

#1 pygame 종료

msg = game_font.render(game_result,True, (255,255,0))
# 화면 기준 가로/세로 중앙 위치 반환
msg_rect = msg.get_rect(center = (screen_width/2, screen_height/2))
# 메시지 출력 후 2초 딜레이 > 종료
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.time.delay(2000)
pygame.quit()

