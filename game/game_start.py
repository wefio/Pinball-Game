import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

# 设置窗口标题
pygame.display.set_caption("游戏菜单")

# 设置字体和大小
font_big = font = pygame.font.Font('思源黑体 Bold 1.004.otf', 38)
font_small = pygame.font.Font('思源黑体 Bold 1.004.otf', 36)

# 设置选项
options = ["开始游戏", "退出游戏"]
option = 0

# 设置分裂效果的初始位置
split_y = 0


# 游戏主循环
running = True
while running:
    screen.fill((0, 0, 0))  # 填充背景色

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
                    print("开始游戏")
                    # 在这里添加执行x的代码
                    # 开始分裂效果
                    split_y = 0
                elif option == 1:
                    running = False
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            if 300 < x < 500:
                if 200 < y < 260:
                    option = 0
                elif 260 < y < 320:
                    option = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 300 < x < 500:
                if 200 < y < 260:
                    if option == 0:
                        print("开始游戏")
                            # 在这里添加执行x的代码
                            # 开始分裂效果
                        split_y = 0
                            # 绘制分裂效果
                        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, split_y))
                        pygame.draw.rect(screen, (0, 0, 0), (0, 600 - split_y, 800, split_y))
                        split_y += 5  # 改变这个值可以调整分裂速度
                elif option == 1:
                    running = False



    pygame.display.update()  # 刷新图像

# 退出pygame
pygame.quit()
