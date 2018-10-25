#!/usr/bin/python



# Задаем параметры окна игры
from tkinter import *

HEIGHT = 500

WIDTH = 600

window = Tk()

window.title('Космический защитник')

c=Canvas(window, width=WIDTH, height=HEIGHT, bg='dimgray')

my_image = PhotoImage(file='/home/dukuz/python3/tenor.gif')

c.create_image(0,0,anchor=NW, image=my_image)

c.pack()




# Рисуем космический корабль и устанавливаем ео в начальную позицию

ship = c.create_polygon(30,0,0,40,60,40,fill='ivory', outline='cyan')

BOTTOM_Y = (HEIGHT-50)

MID_X = WIDTH/2

c.move(ship,MID_X,BOTTOM_Y)



# Задаем движение космического корабля

MOVE_Q = 10

def ship_move(press):

    if press.keysym == 'Left':

        c.move(ship, -MOVE_Q,0)

    elif press.keysym == 'Right':

        c.move(ship, MOVE_Q,0)

    elif press.keysym == 'Up':

        make_shoot()

c.bind_all('<Key>', ship_move)



# Рисуем вражиские космические корабли

from random import randint

enemy_id = list()

enemy_spd = list()

def create_enemy():

    y = 0

    x = randint(40, WIDTH-40)

    spd = randint(2, 5)

    id1 = c.create_oval(x-20, y-20, x+20, y+20, fill='tomato', outline='linen')

    enemy_id.append(id1)

    enemy_spd.append(spd)



# Задаем движение вражеского флота

def move_enemy():

    for k in range(len(enemy_id)):

        c.move(enemy_id[k], 0, enemy_spd[k])



# Задаем параметры снарядов и условия выстрела

shoot_id = list()

shoot_speed = 15


def make_shoot():

    if len(shoot_id) <3:

        pos = c.coords(ship)

        x = pos [0]

        y = pos [1]

        id1 = c.create_oval(x-6, y-6, x+6, y+6, fill = 'yellow', outline = 'magenta')

        shoot_id.append(id1)



# Перемещение снаряда

def move_shoot():

    for i in range(len(shoot_id)):

        c.move(shoot_id[i], 0,-shoot_speed)



# Определение положения снаряда на ировом поле

def coords_shoot(id_num):

    pos = c.coords(id_num)

    x = (pos[0] + pos[2]) / 2

    y = (pos[1] + pos[3]) / 2

    return x,y



# Удаление снаряда

def del_shoot(i):

    c.delete(shoot_id[i])

    del shoot_id[i]



# Стирание снаряда при вылете за экран

def clean_shoot():

    for i in range (len(shoot_id)-1, -1, -1):

        x,y = coords_shoot(shoot_id[i])

        if y < 0 :

                del_shoot(i)



# Определение положение корабля противника на игровом поле

def coords_enemy(id_num):

    pos = c.coords(id_num)

    x = (pos[0] + pos [2]) / 2

    y = (pos[1] + pos [3]) / 2

    return x,y


# Удаление корабля противника

def del_enemy(i):

        c.delete(enemy_id[i])

        del enemy_id[i]


# Стирание корабля противника при вылете за экран

def clean_enemy():

    for i in range(len(enemy_id)-1, -1, -1):

        x,y = coords_enemy(enemy_id[i])

        if y > HEIGHT:

                del_enemy(i)



# Задаем функцию расчета расстояния между двумя обьектами

from math import  sqrt

def distance(id1, id2):

    x1, y1 = coords_enemy(id1)

    x2, y2 = coords_enemy(id2)

    return sqrt((x2-x1) **2 + (y2-y1) **2)



# Стирание корабля противника при попадании снаряда

def bum():

        for i in range (len(enemy_id) -1, -1, -1):

            for n in range (len(shoot_id) -1, -1, -1):

                if distance(enemy_id[i], shoot_id[n]) < 26:

                    del_enemy(i)

                    del_shoot(n)



from time import sleep, time


while True:

    if randint(1, 40) == 1:

        create_enemy()

    move_enemy()

    move_shoot()

    clean_shoot()

    clean_enemy()

    bum()

    window.update()

    sleep(0.05)







