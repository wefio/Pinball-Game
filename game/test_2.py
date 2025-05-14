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

class GameBase:
    """游戏基础类，包含初始化和资源加载"""
    # 初始化 Pygame
    pygame.init()

    # 窗口设置
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("弹球游戏")

    # 颜色定义
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # 加载字体
    FONT_PATH = "resources/Siyuan.otf"
    font = pygame.font.Font(FONT_PATH, 36)
    font_large = pygame.font.Font(FONT_PATH, 50)
    font_medium = pygame.font.Font(FONT_PATH, 40)

    # 加载游戏资源
    background_image = pygame.image.load("resources/background.png")
    paddle_image = pygame.image.load("resources/board-1.png")
    ball_image = pygame.image.load("resources/ball-2.png")
    collision_sound = pygame.mixer.Sound("resources/sound-1.mp3")
    background_music = pygame.mixer.Sound("resources/sound.mp3")


# 游戏配置信息
class GameConfig(GameBase):
    # 默认配置
    BALL_RADIUS = 25
    PADDLE_WIDTH = 100
    PADDLE_HEIGHT = 30
    PADDLE_SPEED = 5
    INITIAL_BALL_SPEED_Y = -2

    def __init__(self):
        self.ball_x = self.WINDOW_WIDTH // 2
        self.ball_y = self.WINDOW_HEIGHT - 63
        self.ball_speed_x = random.randint(-5, 5)
        self.ball_speed_y = self.INITIAL_BALL_SPEED_Y
        self.paddle_x = (self.WINDOW_WIDTH - self.PADDLE_WIDTH) // 2
        self.paddle_y = self.WINDOW_HEIGHT - self.PADDLE_HEIGHT - 10
        self.score = -1
        self.start_time = time.time()
        self.running = True

    def update_game_config(self):
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        # 边界碰撞检测
        if self.ball_x <= self.BALL_RADIUS or self.ball_x >= self.WINDOW_WIDTH - self.BALL_RADIUS:
            self.ball_speed_x = -self.ball_speed_x
        if self.ball_y <= self.BALL_RADIUS:
            self.ball_speed_y = -self.ball_speed_y
        elif self.ball_y >= self.WINDOW_HEIGHT - self.BALL_RADIUS:
            self.running = False

        # 球与挡板碰撞检测
        if (self.ball_y >= self.paddle_y - self.BALL_RADIUS and 
            self.paddle_x <= self.ball_x <= self.paddle_x + self.PADDLE_WIDTH):
            self.ball_speed_y = -abs(self.ball_speed_y)
            self.score += 1
            self.collision_sound.play()

    def get_game_time(self):
        elapsed = int(time.time() - self.start_time)
        return elapsed // 3600, (elapsed % 3600) // 60, elapsed % 60

class GameLoop(GameBase):
    """游戏循环类，处理游戏事件和渲染"""
    def handle_events(self, config):
        """处理游戏事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.running = False
        
        # 处理键盘输入
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and config.paddle_x > 0:
            config.paddle_x -= config.PADDLE_SPEED
        if keys[pygame.K_RIGHT] and config.paddle_x < self.WINDOW_WIDTH - config.PADDLE_WIDTH:
            config.paddle_x += config.PADDLE_SPEED
            
        # 处理鼠标控制
        mouse_x, _ = pygame.mouse.get_pos()
        # 确保挡板不会超出窗口边界
        half_width = config.PADDLE_WIDTH // 2
        if mouse_x - half_width > 0 and mouse_x + half_width < self.WINDOW_WIDTH:
            config.paddle_x = mouse_x - half_width
    
    def render_game(self, config):
        """渲染游戏画面"""
        # 绘制背景、球和挡板
        self.window.blit(self.background_image, (0, 0))
        self.window.blit(self.ball_image, (config.ball_x - config.BALL_RADIUS, config.ball_y - config.BALL_RADIUS))
        self.window.blit(self.paddle_image, (config.paddle_x, config.paddle_y))
        
        # 显示得分和游戏时间
        hours, minutes, seconds = config.get_game_time()
        self.window.blit(self.font.render(f"得分: {config.score}", True, self.WHITE), (10, 10))
        self.window.blit(self.font.render(f"时间: {hours:02d}:{minutes:02d}:{seconds:02d}", True, self.WHITE), (10, 50))
        
        pygame.display.update()
    
    def game_loop(self):
        """游戏主循环"""
        config = GameConfig()
        clock = pygame.time.Clock()
        
        # 播放背景音乐
        self.background_music.play(-1)
        
        # 游戏主循环
        while config.running:
            self.handle_events(config)
            config.update_game_config()
            self.render_game(config)
            clock.tick(60)
        
        # 游戏结束，显示结果并停止音乐
        hours, minutes, seconds = config.get_game_time()
        print(f"游戏结束！恭喜您浪费了人生中的 {hours} 小时 {minutes} 分钟 {seconds} 秒，您的得分是: {config.score}")
        self.background_music.stop()


class GameMenu(GameLoop, GameBase):
    """游戏菜单类，处理菜单界面和交互"""
    # 菜单配置
    MENU_X = 300
    MENU_WIDTH = 200
    MENU_ITEM_HEIGHT = 60
    MENU_START_Y = 200
    
    def render_menu(self, options, selected_index):
        """渲染菜单界面"""
        self.window.fill(self.BLACK)  # 填充背景色
        for i, text in enumerate(options):
            if i == selected_index:
                text_surface = self.font_large.render("> " + text, True, self.WHITE)
            else:
                text_surface = self.font_medium.render("   " + text, True, self.WHITE)
            self.window.blit(text_surface, (self.MENU_X, self.MENU_START_Y + i * self.MENU_ITEM_HEIGHT))
        pygame.display.update()
    
    def handle_menu_events(self, options, selected_index, running):
        """处理菜单事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return selected_index, False
            
            # 键盘控制
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    self.process_menu_selection(selected_index)
                    if selected_index == 1:  # 退出游戏
                        return selected_index, False
            
            # 鼠标控制
            x, y = pygame.mouse.get_pos()
            if self.MENU_X < x < self.MENU_X + self.MENU_WIDTH:
                # 鼠标移动高亮选项
                if event.type == pygame.MOUSEMOTION:
                    for i in range(len(options)):
                        item_y = self.MENU_START_Y + i * self.MENU_ITEM_HEIGHT
                        if item_y < y < item_y + self.MENU_ITEM_HEIGHT:
                            selected_index = i
                
                # 鼠标点击选择
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(options)):
                        item_y = self.MENU_START_Y + i * self.MENU_ITEM_HEIGHT
                        if item_y < y < item_y + self.MENU_ITEM_HEIGHT:
                            self.process_menu_selection(i)
                            if i == 1:  # 退出游戏
                                return i, False
        
        return selected_index, running
    
    def process_menu_selection(self, selected_index):
        """处理菜单选择"""
        if selected_index == 0:  # 开始游戏
            self.game_loop()
    
    def __init__(self):
        """初始化游戏菜单"""
        # 设置菜单选项
        options = ["开始游戏", "退出游戏"]
        selected_index = 0
        
        # 菜单主循环
        running = True
        while running:
            # 渲染菜单
            self.render_menu(options, selected_index)
            
            # 处理菜单事件
            selected_index, running = self.handle_menu_events(options, selected_index, running)
        
        # 退出pygame
        pygame.quit()

if __name__ == "__main__":
    GameMenu()