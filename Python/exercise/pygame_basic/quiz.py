import pygame
import random
#########################################################################################################
#기본 초기화 (반드시 해야 하는 것들)
pygame.init()

#화면 크기 설정
screen_width = 480 #가로 크기
screen_hight = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("pang Game")

#FPS
clock = pygame.time.Clock()
#########################################################################################################

#1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
background = pygame.image.load("C:\\Users\\skxog\\Desktop\\PythonWorkSpace\\pygame_basic\\background.png")

character = pygame.image.load("C:\\Users\\skxog\\Desktop\\PythonWorkSpace\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_hight = character_size[1]
character_x_pos = screen_width / 2 - (character_width / 2)
character_y_pos = screen_hight - character_hight

#똥
ddong = pygame.image.load("C:\\Users\\skxog\\Desktop\\PythonWorkSpace\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_hight = ddong_size[1]
ddong_x_pos = random.randrange(0, (screen_width - ddong_width))
ddong_y_pos = 0

#이동 속도
character_speeed = 0.6

#이동거리
to_x = 0
to_y = 0

#게임 시간 설정
total_time = 100
#폰트정의
game_font = pygame.font.Font(None, 40)
#시작시간
start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(30)
    
    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #키보드 감지(캐릭터이동)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speeed
            if event.key == pygame.K_RIGHT:
                to_x += character_speeed
            # if event.key == pygame.K_DOWN:
            #     to_y += character_speeed
            # if event.key == pygame.K_UP:
            #     to_y -= character_speeed

        #캐릭터 멈춤(방향키 땟을때)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #     to_y = 0

    #캐릭터 이동
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # if character_y_pos < 0:
    #     character_y_pos = 0
    # elif character_y_pos > screen_hight - character_hight:
    #     character_y_pos = screen_hight - character_hight

    #똥 떨어지기
    ddong_y_pos += to_y * dt + 8
    if ddong_y_pos == screen_hight:
        ddong_y_pos = 0
        if ddong_y_pos == 0:
            ddong_x_pos = random.randrange(0, (screen_width - ddong_width))


    #3. 게임 캐릭터 위치 정의
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    #4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    #충돌 체크
    if character_rect.colliderect(ddong_rect):
        print("게임오버")
        running = False

    #5. 화면에 그리기
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <=0:
        print("타임아웃")
        running = False

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()