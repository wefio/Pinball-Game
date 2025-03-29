"""Python编程当作业，碰碰球小游戏开发
编程要求：
1.使用Python语言进行编程；
2.游戏基础功能：运行后弹出一小窗口，有游戏开始键，按确认后游戏开始；
在窗口中出现1个具有初速度的小球；在靠小窗口下边沿的一侧，有一条粗线表示一个托板，
可由键盘或鼠标控制左右滑动；小球在小窗口中，以自由直线运动，碰到小窗口的左上右边缘时会反弹，
反弹按物理规则反弹，小球碰到小窗口的下侧边缘后会直接掉落(小球掉落不是由于小球受到向下方的重力作用，
只是纯粹的小球有一个初始速度)；通过控制托板，防止小球从下侧边缘掉落；在游戏界面内设置有定时显示，
表示玩游戏则坚持的时间，当小球掉落后游戏结束，给出相应的评分。
3.游戏附加功能：小球在与左上右侧边缘碰撞时，有音效发出，与托板碰撞时有音效和动画；
随着时间的增加，小球的速度逐渐增加，游戏难度加大；有兴趣的话，
还可以在窗口场景中布置一些辅助机关，比如碰触后可以加速的弹簧，或者是减速的海绵。"""
import random
import time
import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口大小
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("弹球游戏")

# 加载字体
font_path = "resources/Siyuan.otf"
font = pygame.font.Font(font_path, 36)
font_big = pygame.font.Font(font_path, 50)
font_small = pygame.font.Font(font_path, 40)

# 加载背景、板、球和音效
bg_img = pygame.image.load("resources/background.png")
player_img = pygame.image.load("resources/board-1.png")
ball_img = pygame.image.load("resources/ball-2.png")
sound = pygame.mixer.Sound("resources/sound.mp3")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# 游戏配置信息
class GameConfig:
    def __init__(self):
        self.ball_x = window_width // 2
        self.ball_y = window_height - 63
        self.ball_radius = 25
        self.ball_speed_x = random.randint(-5, 5)
        self.ball_speed_y = -2
        self.board_width = 100
        self.board_height = 30
        self.board_x = window_width // 2 - self.board_width // 2
        self.board_y = window_height - self.board_height - 10
        self.board_speed = 5
        self.score = 0
        self.start_time = time.time()
        self.run = True

    def update_game_config(self):
        # 更新球的位置
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        # 球与窗口边界碰撞检测
        if self.ball_x <= self.ball_radius or self.ball_x >= window_width - self.ball_radius:
            # 如果球的横坐标超出窗口左右边界，反向改变速度，让球反弹
            self.ball_speed_x = -self.ball_speed_x

        if self.ball_y <= self.ball_radius or self.ball_y >= window_height - self.ball_radius:
            # 如果球的纵坐标超出窗口上下边界，反向改变速度，让球反弹
            self.ball_speed_y = -self.ball_speed_y

        # 如果球碰到窗口边界，游戏结束
        if self.ball_y >= window_height - self.ball_radius:
            # 如果球的纵坐标超出窗口下边界，游戏结束
            self.run = False

        # 球与板碰撞检测
        if self.ball_y >= self.board_y - self.ball_radius and self.board_x <= self.ball_x <= self.board_x + self.board_width:
            self.ball_speed_y = -abs(self.ball_speed_y)  # 碰撞后速度取绝对值
            self.score += 1
        sound.play()

    def get_game_time(self):
        elapsed_time = int(time.time() - self.start_time)
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60
        return hours, minutes, seconds


# 游戏循环
def game_loop():
    game_config = GameConfig()
    clock = pygame.time.Clock()

    while game_config.run:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                game_config.run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and game_config.board_x > 0:
            game_config.board_x -= game_config.board_speed
        if keys[pygame.K_RIGHT] and game_config.board_x < window_width - game_config.board_width:
            game_config.board_x += game_config.board_speed

        game_config.update_game_config()

        window.blit(bg_img, (0, 0))
        window.blit(ball_img,(game_config.ball_x - game_config.ball_radius, game_config.ball_y - game_config.ball_radius))
        window.blit(player_img, (game_config.board_x, game_config.board_y))

        # 显示得分和游戏时间
        score_text = font.render("得分: " + str(game_config.score - 1), True, WHITE)
        hours, minutes, seconds = game_config.get_game_time()
        time_text = font.render("时间: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds), True, WHITE)
        window.blit(score_text, (10, 10))
        window.blit(time_text, (10, 50))

        pygame.display.update()

        clock.tick(60)

    print("游戏结束！恭喜您浪费了人生中的", hours, "小时", minutes, "分钟", seconds, "秒，" "您的得分是:",
          game_config.score)

    pygame.quit()


# 设置选项
options = ["开始游戏", "退出游戏"]
option = 0

# 设置分裂效果的初始位置
split_y = 0

# 游戏主循环
running = True
while running:
    window.fill(BLACK)  # 填充背景色
    for i, text in enumerate(options):
        if i == option:
            img = font_big.render("> " + text, True, (255, 255, 255))
        else:
            img = font_small.render("   " + text, True, (255, 255, 255))
        window.blit(img, (300, 200 + i * 60))

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
                    game_loop()
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
                        game_loop()
                elif option == 1:
                    running = False
    pygame.display.update()
# 退出pygame
pygame.quit()
