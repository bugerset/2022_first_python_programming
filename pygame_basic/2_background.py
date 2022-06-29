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

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였나?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    # screen.fill((3.1415,92,35)) # 파란색 배경으로 채우기 (R,G,B)
    # screen.blit(background, (0,0)) # 백그라운드에 저장한 사진 (0,0)에 심기

    pygame.display.update() # 백그라운드에 그리기

# 종료
pygame.quit()