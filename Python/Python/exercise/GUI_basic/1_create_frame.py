from tkinter import *

root = Tk()
root.title("myGUI")
root.geometry("640x480") #가로 * 세로
# root.geometry("640x480+400+150") #가로 * 세로 + X좌표 + Y좌표

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가

root.mainloop()