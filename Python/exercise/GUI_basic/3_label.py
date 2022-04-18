from tkinter import *

from pygame import image

root = Tk()
root.title("myGUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="GUI_basic/image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 # Garbage Collection : 불필요한 메모리 공간 해제 / 때문에 글로벌 설정
    photo2 = PhotoImage(file="GUI_basic/image2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()