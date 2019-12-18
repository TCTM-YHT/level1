# coding:utf-8
# 导入pygame库，并进行初始化
import pygame, sys
from pygame.locals import*
pygame.init()

# 创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255, 255, 255))

# 设置窗口标题
pygame.display.set_caption("飞机大战")

# 加载图片
enemy = pygame.image.load("images/enemy.png")
enemy2 = pygame.image.load("images/enemy2.png")
enemy3 = pygame.image.load("images/enemy3.png")
bg = pygame.image.load("images/bg.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()  
            
while True:
    # 画出游戏背景和三架敌飞机
    canvas.blit(bg, (0, 0))
    canvas.blit(enemy, (92, 100))
    # 画出飞机方阵
    canvas.blit(enemy, (152, 100))
    canvas.blit(enemy, (212, 100))
    canvas.blit(enemy, (272, 100))
    canvas.blit(enemy, (332, 100))
    canvas.blit(enemy2, (147, 160))
    canvas.blit(enemy2, (217, 160))
    canvas.blit(enemy2, (287, 160))
    canvas.blit(enemy3, (192, 230))

    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
    
