import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

font_big = pygame.Font('思源黑体 Bold 1.004.otf', 38)
font_small = pygame.Font('思源黑体 Bold 1.004.otf', 36)


class SetUp:
    pygame.display.set_caption("弹球")
    icon = pygame.image.load('球-1.png')
    pygame.display.set_icon(icon)
    bg_img = pygame.image.load("背景.png")
    player_img = pygame.image.load('板-1.png')
    player_x = 400
    player_y = 550
    player_step = 0
    ball_img = pygame.image.load("球-2.png")
    ball_high = 50
    ball_weigh = 50
    ball_x = 400
    ball_y = 500
    ball_step_x = 2
    ball_step_y = -2
    score = 0
    run = True


def show_ball(x, y):  # 显示球
    screen.blit(SetUp.ball_img, (x, y))


#   使用例 show_ball(SetUp.ball_x, SetUp.ball_y)


def move_player(step, x):  # 移动玩家
    x += step
    max_x = 695
    min_x = 5
    if x > max_x:
        x = max_x
    elif x < min_x:
        x = min_x
    return x


move_player(SetUp.player_step, SetUp.player_x)


def move_ball(ball_step_x, ball_step_y, SetUp):
    # 更新位置
    SetUp.ball_x += ball_step_x
    SetUp.ball_y += ball_step_y
    # 左右反弹
    if SetUp.ball_x <= 0 or SetUp.ball_x >= 750:
        ball_step_x *= -1
    # 上反弹
    if SetUp.ball_y <= 0:
        ball_step_y *= -1
    # 下超界
    if SetUp.ball_y >= 610:
        return False  # Game over
    return True


def create_rects(player_x, player_y, ball_x, ball_y, ball_high, ball_weigh):
    player_rect = pygame.Rect(player_x, player_y, 100, 20)  # 板蒙版
    ball_rect = pygame.Rect(ball_x, ball_y, ball_high, ball_weigh)  # 球蒙版
    # Check collision with player
    if player_rect.colliderect(ball_rect):  # 打板反弹
        ball_step_y = -1
        return ball_step_y
    return True


create_rects(SetUp.player_x, SetUp.player_y, SetUp.ball_x, SetUp.ball_y, SetUp.ball_high, SetUp.ball_weigh)


def game_start():
    running = SetUp.run
    while running:
        screen.fill((0, 0, 0))
        options_start()
        pygame.display.update()


def options_start():
    running = SetUp.run
    options = ["开始游戏", "退出游戏"]
    option = 0
    for i, text in enumerate(options):
        if i == option:
            img = font_big.render("> " + text, True, (255, 255, 255))
        else:
            img = font_small.render("   " + text, True, (255, 255, 255))
        screen.blit(img, (300, 200 + i * 60))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                option = (option - 1) % len(options)
            elif event.key == pygame.K_DOWN:
                option = (option + 1) % len(options)
            elif event.key == pygame.K_RETURN:
                if option == 0:
                    return True
                elif option == 1:
                    return False
    return running


def game_over():
    global screen, font_small, font_big
    options = ["重新开始", "返回主页", "退出游戏"]
    option = 0
    running = True
    while running:
        screen.fill((0, 0, 0))
        for i, text in enumerate(options):
            if i == option:
                img = font_big.render("> " + text, True, (255, 255, 255))
            else:
                img = font_small.render("   " + text, True, (255, 255, 255))
            screen.blit(img, (300, 200 + i * 60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    option = (option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    option = (option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if option == 0:
                        return 'restart'
                    elif option == 1:
                        return 'home'
                    elif option == 2:
                        return 'quit'
                pygame.display.update()


def game_loop():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(SetUp.bg_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    SetUp.player_step = 2
                elif event.key == pygame.K_LEFT:
                    SetUp.player_step = -2
            if event.type == pygame.KEYUP:
                SetUp.player_step = 0
        screen.blit(SetUp.player_img, (SetUp.player_x, SetUp.player_y))
        SetUp.player_x = move_player(SetUp.player_step, SetUp.player_x)
        show_ball(SetUp.ball_x, SetUp.ball_y)
        running = move_ball(SetUp.ball_step_x, SetUp.ball_step_y, SetUp)
        if not running:
            result = game_over()
            if result == 'restart':
                SetUp.player_x = 400
                SetUp.player_y = 550
                SetUp.player_step = 0
                SetUp.ball_x = 400
                SetUp.ball_y = 500
                SetUp.ball_step_x = 2
                SetUp.ball_step_y = -2
                running = True
            elif result == 'home':
                return
            elif result == 'quit':
                running = False
        pygame.display.update()


while True:
    if game_start():
        game_loop()
    else:
        break


# 退出pygame
pygame.quit()
