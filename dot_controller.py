from blinkt import set_pixel, set_brightness, show, clear
from pyPS4Controller.controller import Controller

i = 0

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_R1_press(self):

        global i#important
        i += 1
        set_pixel(i,255,0,0)
        show()
        clear()




    def on_L1_press(self):
        global i#important
        i -= 1
        set_pixel(i,255,0,0)
        show()
        clear()




def back():
    global i #important
    while i >= 0 :

        set_pixel(i, 255, 0, 0)
        show()
        on_R1_press(self)
        clear()
        show()
        if i == 0:#important
            forward()
def forward():
    global i#important
    while i < 7:

        set_pixel(i, 255, 0, 0)
        show()
        on_R1_press()
        clear()
        show()
        if i == 7:#important
            back()


controller = MyController(interface='/dev/input/js0', connecting_using_ds4drv=False)
controller.listen()
