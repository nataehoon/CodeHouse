from tkinter import *

from matplotlib.pyplot import fill

root = Tk()
root.title("Windows 메모장")
root.geometry("640x480")

def save_mynote():
    txtf = open("./exercise/GUI_basic/mynote.xtx", "w")
    txtf.write(txt.get("1.0", END))
    txtf.close()

def load_mynote():
    txtf = open("./exercise/GUI_basic/mynote.xtx", "r")
    txt.delete("1.0", END)
    txt.insert(END, txtf.read())
    txtf.close()

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, width=640, height=480, yscrollcommand=scrollbar.set)
txt.pack()

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=load_mynote)
menu_file.add_command(label="저장", command=save_mynote)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()