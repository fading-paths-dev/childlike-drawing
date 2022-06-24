
import random
import turtle as tur
from drawings import *

def get_mouse_click_coor(x, y):
    tur.onscreenclick(wait)
    random.choice(images)(random.choice(colours),random.choice(colours), x, y)
    tur.onscreenclick(get_mouse_click_coor)

def wait (x,y):
    print ("wait until this drawing has finished")

tur.onscreenclick(get_mouse_click_coor)
tur.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
