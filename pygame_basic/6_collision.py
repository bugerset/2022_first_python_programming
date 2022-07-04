import pygame

pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Bubble Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("/Users/youngseo/Desktop/sacrifice/Python-programming/Python-programming-1/pygame_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("/Users/youngseo/Desktop/sacrifice/Python-programming/Python-programming-1/pygame_basic/스크린샷 2022-06-29 오전 7.06.46.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/youngseo/Desktop/sacrifice/Python-programming/Python-programming-1/pygame_basic/적.png")
enemy_size = character.get_rect().size # 이미지의 크기를 구해옴
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반에 위치
enemy_y_pos = (screen_height/2) - (enemy_height/2) # 화면 세로 크기 중간에 위치

# 이벤트 루프
running = True
while running: 
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였나?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값
    if 0 > character_x_pos:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값
    if 0 > character_y_pos:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했습니다")
        running = False

    # screen.fill((3.141character_speed,92,3character_speed)) # 파란색 배경으로 채우기 (R,G,B)
    screen.blit(background, (0,0)) # 백그라운드에 저장한 사진 (0,0)에 심기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update() # 백그라운드에 그리기

# 종료
pygame.quit()