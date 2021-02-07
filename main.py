from random import randint
import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =   (255, 0, 0)
# Описание настроек игральной кости
class Bone:
    w = h = 150 # Размеры
    color = BLACK # Цвет
    x = 100 # Координаты
    y = 100
    border = 5 # Толщина границы

pg.init() # Запустить внутрнние команды pygame
screen = pg.display.set_mode((640, 480))
painter = pg.draw # Художник (который умеет рисовать простые фигуры)

bone_1 = randint(1, 6)
bone_2 = randint(1, 6)
print(bone_1, bone_2)

running = True
while running:
    screen.fill(WHITE) # Закрашиваем весь экран цветом WHITE
    
    listEvents = pg.event.get() # Список всех событий окна
    for event in listEvents:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN: # Собитие нажатия на к-л клавишу
            if event.key == pg.K_ESCAPE: # Нажатие на клавишу ESCAPE
                running = False
    
    painter.rect(screen, Bone.color, \
                 (Bone.x, Bone.y, Bone.w, Bone.h), Bone.border, 10)
    painter.rect(screen, Bone.color, \
                 (Bone.x+200, Bone.y, Bone.w, Bone.h), Bone.border, 10)
    
    # 1
    painter.circle(screen, Bone.color, \
                   (Bone.x+Bone.w/2, Bone.y+Bone.h/2), 15, 3)
    # 2-3
    painter.circle(screen, Bone.color, \
                   (Bone.x+Bone.w/4, Bone.y+Bone.h/4), 15, 3)
    painter.circle(screen, Bone.color, \
                   (Bone.x+3*Bone.w/4, Bone.y+3*Bone.h/4), 15, 3)
    # 4-5
    painter.circle(screen, Bone.color, \
                   (Bone.x+Bone.w/4, Bone.y+3*Bone.h/4), 15, 3)
    painter.circle(screen, Bone.color, \
                   (Bone.x+3*Bone.w/4, Bone.y+Bone.h/4), 15, 3)
    # 6
    painter.circle(screen, Bone.color, \
                   (Bone.x+Bone.w/2, Bone.y+Bone.h/4), 15, 3)
    painter.circle(screen, Bone.color, \
                   (Bone.x+Bone.w/2, Bone.y+3*Bone.h/4), 15, 3)
    
    
    pg.display.update() # Обновляем экран
    
pg.quit() # Остановть все внутрнние команды pygame