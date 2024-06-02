import pygame
import time
import os

# 初始化 Pygame
pygame.init()

# 设置窗口大小
screen_width = 1024
screen_height = 218
screen = pygame.display.set_mode((screen_width, screen_height))

# 加载图片
image = pygame.image.load("image.jpg")  # 替换为你的图片路径

# 主循环
running = True
start_time = time.time()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 在屏幕上绘制图片
    screen.blit(image, (0, 0))

    pygame.display.flip()

    if time.time() - start_time > 1:  # 显示 1 秒后
        os.system("runtime\python.exe main.py")  # 替换为实际的下一个文件路径
        running = False
        

# 退出程序
pygame.quit()