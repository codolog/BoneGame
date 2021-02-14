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


# 1
def one(x, y, bone):
    painter.circle(screen, bone.color, \
                   (bone.x+bone.w/2, bone.y+bone.h/2), 15, 3)
# 2
def two(x, y, bone):
    painter.circle(screen, bone.color, \
                   (bone.x+bone.w/4, bone.y+bone.h/4), 15, 3)
    painter.circle(screen, bone.color, \
                   (bone.x+3*bone.w/4, bone.y+3*bone.h/4), 15, 3)
# 3
def three(x, y, bone):
    one(x, y, bone)
    two(x, y, bone)
    
# 4
def four(x, y, bone):
    painter.circle(screen, bone.color, \
                   (bone.x+bone.w/4, bone.y+3*bone.h/4), 15, 3)
    painter.circle(screen, bone.color, \
                   (bone.x+3*bone.w/4, bone.y+bone.h/4), 15, 3)
# 5    
def five(x, y, bone):
    one(x, y, bone)
    four(x, y, bone)

# 6
def six(x, y, bone):
    four(x, y, bone)
    painter.circle(screen, bone.color, \
                   (bone.x+bone.w/2, bone.y+bone.h/4), 15, 3)
    painter.circle(screen, bone.color, \
                   (bone.x+bone.w/2, bone.y+3*bone.h/4), 15, 3)

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
    
   
    
    
    pg.display.update() # Обновляем экран
    
pg.quit() # Остановть все внутрнние команды pygame