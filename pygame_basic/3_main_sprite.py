import pygame

pygame.init() 

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Bubble Game")

# 배경 이미지 불러오기
background = pygame.image.load("/Users/youngseo/Desktop/Study/Python/강의_1/pygame_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("/Users/youngseo/Desktop/Study/Python/강의_1/pygame_basic/스크린샷 2022-06-29 오전 7.06.46.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였나?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    # screen.fill((3.1415,92,35)) # 파란색 배경으로 채우기 (R,G,B)
    screen.blit(background, (0,0)) # 백그라운드에 저장한 사진 (0,0)에 심기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기


    pygame.display.update() # 백그라운드에 그리기

# 종료
pygame.quit()