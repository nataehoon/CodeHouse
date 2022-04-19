import time
import tkinter.ttk as ttk
from multiprocessing.sharedctypes import Value
from tkinter import *

root = Tk()
root.title("myGUI")
root.geometry("640x480") #가로 * 세로

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") #indeterminate : 정해지지않은 상태(로딩상태)
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) #10 ms마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() #작동 중지

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(101): # 1 ~ 100
        time.sleep(0.01) # 0.01 초 대기

        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()