# resources.py
import threading

import pygame

# 使用一个 字典来保存图片资源
images = {}

def load_image_threaded(file_path):
    # 创建并启动一个新线程来加载图像
    thread = threading.Thread(target=_load_image, args=(file_path,))
    thread.start()

    # 等待线程完成
    thread.join()

    # 返回加载的图像或者如果加载失败则返回None
    return images.get(file_path, None)

def _load_image(file_path):
    try:
        # 使用try-except来捕获可能发生的错误
        image = pygame.image.load(file_path)
        # 将加载的图片存入字典中
        images[file_path] = image
    except pygame.error as err:
        print(f"无法加载图像：{err}")
        raise

# 你可以使用这个函数来加载图片，例如：
# load_image_threaded('球-1.png')
# load_image_threaded('背景.png')
# ...以此类推
