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
# 导入pygame库
import pygame

# 导入资源文件中的函数
from image import load_image_threaded

# from xy import player_step

# 初始化pygame
pygame.init()

# 设置窗口大小
screen = pygame.display.set_mode((800, 600))

# 设置窗口标题
pygame.display.set_caption("弹球")


class LoadImage:
    # 加载图标
    icon = load_image_threaded('球-1.png')
    # 加载背景
    bgImg = load_image_threaded("背景.png")
    # 板
    playerImg = load_image_threaded('板-1.png')


playerX = 400
playerY = 550
playerStep = 0
# 球
bollImg = load_image_threaded("球-2.png")
bollStep = 4


def show_boll():
    screen.blit(bollImg, (playerX + 25, playerY - 50))


def move_player():
    global playerX
    playerX += playerStep  # 移动
    if playerX > 695:
        playerX = 695
    if playerX < 5:
        playerX = 5


def move_keyboard():
    global playerStep
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            playerStep = 2
        elif event.key == pygame.K_LEFT:
            playerStep = -2
    if event.type == pygame.KEYUP:
        # 延迟
        time_delay = 2
        for i in range(4):
            time_delay = time_delay - 0.5
        playerStep = time_delay


# 游戏主循环
running = True
while running:
    screen.blit(LoadImage.bgImg, (0, 0))  # 画背景
    show_boll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move_keyboard()
    screen.blit(LoadImage.playerImg, (playerX, playerY))
    move_player()
    pygame.display.update()  # 刷新图像

# 退出pygame
pygame.quit()
