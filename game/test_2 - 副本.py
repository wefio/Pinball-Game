import pygame
import os


class GameScreen:
    def __init__(self):
        # 初始化 Pygame
        pygame.init()

        # 设置窗口大小
        self.window = 800, 600
        self.WINDOW = pygame.display.set_mode(self.window)
        pygame.display.set_caption("弹球")

        # 获取资源文件夹路径
        self.resource_dir = os.path.join(os.path.dirname(__file__), 'resources')

        # 加载板、球、音效和字体
        self.player_img = pygame.image.load(os.path.join(self.resource_dir, "board-1.png"))
        self.ball_img = pygame.image.load(os.path.join(self.resource_dir, "ball-2.png"))
        self.sound = pygame.mixer.Sound(os.path.join(self.resource_dir, "sound.mp3"))
        # 加载碰撞音效
        self.sound_1 = pygame.mixer.Sound(os.path.join(self.resource_dir, "sound-1.mp3"))
        self.font_path = os.path.join(self.resource_dir, "Siyuan.otf")

        # 设置字体
        self.font = pygame.font.Font(self.font_path, 36)

        # 设置板的初始位置和移动速度
        self.player_x = self.window[0] // 2
        self.player_speed = 10

        # 设置球的初始位置和速度
        self.ball_x = self.window[0] // 2
        self.ball_y = 50
        self.ball_speed = [3, 3]

        # 记录上一次按键的状态
        self.key_down = False

        # 是否退出游戏的标志
        self.quit_game = False

        # 设置选项和初始选项
        self.options = ["开始游戏", "退出游戏"]
        self.option = 0
        self.running = True

    # 绘制游戏界面
    def draw_game_screen(self):
        self.WINDOW.fill((0, 0, 0))  # 填充背景色

        # 绘制板
        self.WINDOW.blit(self.player_img, (self.player_x, self.window[1] - 50))

        # 绘制球
        self.WINDOW.blit(self.ball_img, (self.ball_x, self.ball_y))

        pygame.display.update()  # 更新屏幕显示

    # 处理键盘事件
    def handle_keyboard_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player_x -= self.player_speed
                elif event.key == pygame.K_RIGHT:
                    self.player_x += self.player_speed

    # 开始游戏
    # 开始游戏
    def start_screen(self):
        while self.running:
            self.handle_keyboard_events()  # 处理键盘事件
            self.draw_game_screen()  # 绘制游戏界面
            pygame.display.update()  # 更新屏幕显示

        pygame.quit()

    # 添加移动球的方法
    # 修改 move_ball 方法
    # 在 move_ball 方法中添加板与球碰撞检测的逻辑
    def move_ball(self):
        # 更新球的位置
        self.ball_x += self.ball_speed[0]
        self.ball_y += self.ball_speed[1]

        # 创建球和窗口边界的矩形区域
        ball_rect = self.ball_img.get_rect(topleft=(self.ball_x, self.ball_y))
        window_rect = pygame.Rect((0, 0), self.window)

        # 检查球是否与窗口边界发生碰撞
        if not window_rect.contains(ball_rect):
            # 如果球与窗口的左右边界发生碰撞，反转水平速度，改变移动方向
            if ball_rect.left < 0 or ball_rect.right > self.window[0]:
                self.ball_speed[0] = -self.ball_speed[0]
            # 如果球与窗口的上边界发生碰撞，反转垂直速度，改变移动方向
            if ball_rect.top < 0:
                self.ball_speed[1] = -self.ball_speed[1]

        # 创建板的矩形区域
        player_rect = self.player_img.get_rect(topleft=(self.player_x, self.window[1] - 50))

        # 检查球是否与板发生碰撞
        if ball_rect.colliderect(player_rect):
            # 反转垂直速度，改变移动方向
            self.ball_speed[1] = -self.ball_speed[1]
            # 播放碰撞音效
            self.sound_1.play()

    # 游戏开始界面
    '''def start_screen(self):
        while self.running:
            self.handle_keyboard_events()  # 处理键盘事件
            pygame.display.update()  # 更新屏幕显示

        pygame.quit()'''


# 创建游戏界面对象并开始游戏界面
game_screen = GameScreen()
game_screen.start_screen()
