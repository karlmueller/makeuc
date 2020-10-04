from tkinter import *
from location import *

root = Tk()
root.geometry('300x150')

def Randomization(event):
    print('Random')
    
def Manual(event):
    print('Manual')

def Default(event):
    print('You are in Default mode')
    xmax, ymax = 5, 5
    city = Map(xmax, ymax)
    city.Generate_map(random = False)
    solve_best_path(city, xmax, ymax)

frame = Frame(root)
frame.pack()

bframe = Frame(root)
bframe.pack(side = BOTTOM)

widget_1 = Button(frame, text = 'Randomization')
widget_1.bind('<Button-1>', Randomization)
widget_1.pack(side = LEFT)


widget_2 = Button(frame, text = 'Manual')
widget_2.bind('<Button-1>', Manual)
widget_2.pack(side = LEFT)


widget_3 = Button(frame, text = 'Default')
widget_3.bind('<Button-1>', Default)
widget_3.pack(side = LEFT)

widget_4 = Button(bframe, text = 'Exit the Program', command = quit)
widget_4.bind('<Button-1>')
widget_4.pack(side = BOTTOM)

root.mainloop()


