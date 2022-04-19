from multiprocessing.sharedctypes import Value
from tkinter import *

root = Tk()
root.title("myGUI")
root.geometry("640x480") #가로 * 세로


label1 = Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
button_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
button_burger1.select()
button_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var)
button_burger3 = Radiobutton(root, text="치킨햄버거", value=3, variable=burger_var)

button_burger1.pack()
button_burger2.pack()
button_burger3.pack()

label2 = Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar()
btn_drink = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)
btn_drink.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) #햄버거 중 선택된 라디오 항목의 값(value)
    print(drink_var.get()) #음료 중 선택된 값을 출력

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()