import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

# 设置窗口标题
pygame.display.set_caption("弹球")

# 加载图标
icon = pygame.image.load('球-1.png')
pygame.display.set_icon(icon)

# 加载背景
bgImg = pygame.image.load("背景.png")

# 板
playerImg = pygame.image.load('板-1.png')
playerX = 400
playerY = 550
playerStep = 0

# 球
ballImg = pygame.image.load("球-2.png")
ballX = 400
ballY = 500
ballStepX = 2
ballStepY = -2

def show_ball(x, y):
    screen.blit(ballImg, (x, y))

def move_player():
    global playerX
    playerX += playerStep  # 移动
    if playerX > 695:
        playerX = 695
    if playerX < 5:
        playerX = 5
# 运动与碰撞检测
def move_ball():
    global ballX, ballY, ballStepX, ballStepY
    ballX += ballStepX
    ballY += ballStepY
    if ballX <= 0 or ballX >= 750:
        ballStepX = -ballStepX
    if ballY <= 0:
        ballStepY = -ballStepY
    if ballY >= 610:
        return False  # 游戏结束
    # 创建一个表示托板的矩形
    player_rect = pygame.Rect(playerX, playerY, 100, 1)
    # 创建一个表示小球的矩形
    ball_rect = pygame.Rect(ballX, ballY, ballImg.get_width(), ballImg.get_height())
    # 检查小球和托板是否碰撞
    if player_rect.colliderect(ball_rect):
        ballStepY = -ballStepY
    return True

# 游戏主循环
running = True
while running:
    screen.blit(bgImg, (0, 0))  # 画背景
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerStep = 2
            elif event.key == pygame.K_LEFT:
                playerStep = -2
        if event.type == pygame.KEYUP:
            playerStep = 0
    screen.blit(playerImg, (playerX, playerY))
    move_player()
    show_ball(ballX, ballY)  # 在这里调用show_ball函数
    running = move_ball()
    pygame.display.update()  # 刷新图像

# 退出pygame
pygame.quit()
