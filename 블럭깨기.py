import pygame
import sys

# 게임 화면 크기
WIDTH = 800
HEIGHT = 600

# 색깔
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 패들의 크기
PADDLE_WIDTH = 400
PADDLE_HEIGHT = 20

# 공의 크기와 속도
BALL_RADIUS = 10
BALL_SPEED_X = 7
BALL_SPEED_Y = 7

# 블록의 설정
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 30
BLOCK_ROWS = 5
BLOCK_COLS = 8

# 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭 깨기")

clock = pygame.time.Clock()

# 패들 초기 설정
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 초기 설정
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS, BALL_RADIUS)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# 블록 초기 설정
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(col * (BLOCK_WIDTH + 2), row * (BLOCK_HEIGHT + 2), BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.circle(screen, WHITE, (ball.x + BALL_RADIUS // 2, ball.y + BALL_RADIUS // 2), BALL_RADIUS)
    for block in blocks:
        pygame.draw.rect(screen, RED, block)

def move_ball():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 벽과의 충돌 검사
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과의 충돌 검사
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y

    # 블록과의 충돌 검사
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

def move_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += 5

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_ball()
        move_paddle()

        draw_objects()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
