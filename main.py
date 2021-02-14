from random import randint
import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =   (255, 0, 0)
# Описание настроек игральной кости
class Bone1:
    w = h = 150 # Размеры
    color = BLACK # Цвет
    x = 100 # Координаты
    y = 100
    border = 5 # Толщина границы

class Bone2:
    w = h = 150 # Размеры
    color = BLACK # Цвет
    x = 100+200 # Координаты
    y = 100
    border = 5 # Толщина границы

pg.init() # Запустить внутрнние команды pygame
screen = pg.display.set_mode((640, 480))
painter = pg.draw # Художник (который умеет рисовать простые фигуры)

bone_1 = randint(1, 6)
bone_2 = randint(1, 6)
print(bone_1, bone_2)


# 1
def one(bone):
    painter.circle(screen, bone.color, \
                   (bone.x+bone.w/2, bone.y+bone.h/2), 15, 3)
# 2
def two(bone):
    painter.circle(screen, bone.color, \
                   (bone.x+bone.w/4, bone.y+bone.h/4), 15, 3)
    painter.circle(screen, bone.color, \
                   (bone.x+3*bone.w/4, bone.y+3*bone.h/4), 15, 3)
# 3
def three(bone):
    one(bone)
    two(bone)
    
# 4
def four(bone):
    two(bone)
    painter.circle(screen, bone.color, \
                   (bone.x+bone.w/4, bone.y+3*bone.h/4), 15, 3)
    painter.circle(screen, bone.color, \
                   (bone.x+3*bone.w/4, bone.y+bone.h/4), 15, 3)
# 5    
def five(bone):
    one(bone)
    four(bone)

# 6
def six(bone):
    four(bone)
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
    
    painter.rect(screen, Bone1.color, \
                 (Bone1.x, Bone1.y, Bone1.w, Bone1.h), Bone1.border, 10)
    painter.rect(screen, Bone2.color, \
                 (Bone2.x, Bone2.y, Bone2.w, Bone2.h), Bone2.border, 10)
    
    if bone_1 == 1: one(Bone1)
    elif bone_1 == 2: two(Bone1)
    elif bone_1 == 3: three(Bone1)
    elif bone_1 == 4: four(Bone1)
    elif bone_1 == 5: five(Bone1)
    elif bone_1 == 6: six(Bone1)
    
    if bone_2 == 1: one(Bone2)
    elif bone_2 == 2: two(Bone2)
    elif bone_2 == 3: three(Bone2)
    elif bone_2 == 4: four(Bone2)
    elif bone_2 == 5: five(Bone2)
    elif bone_2 == 6: six(Bone2)
    
    pg.display.update() # Обновляем экран
    
pg.quit() # Остановть все внутрнние команды pygame