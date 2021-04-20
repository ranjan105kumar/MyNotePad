from tkinter import *

def hello():
    print("hello")
    str = T.get(1.0,End)
    print(str)

root = Tk()
menubar = Menu()
filemenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = "File" ,menu = filemenu )
filemenu.add_command(label = "New" , command = hello)
filemenu.add_command(label = "Open" , command = hello)
filemenu.add_command(label = "Save" , command = hello)
filemenu.add_command(label = "Save as..." , command = hello)
filemenu.add_command(label = "Close" , command = hello)
filemenu.add_command(label = "Exit" , command = root.quit)
root.configure(menu = menubar)
S = Scrollbar(root)
T = Text(root)
S.pack(side = RIGHT,fill=Y)
T.pack()
S.config(command = T.yview)
T.config(yscrollcommand = S.set)
str = """hello buddy \n hoe are yoy \n what are you doing \n hey buddy here weather is nice so come and enjoy your life hkjdhdjslkjnd gjuysklfrdfukddnwy jgfwqiurymwqjbtfywyh dtf eyhkewleuem" \
      "8ju5tri6j8trgfki87og8okt8ut8ok98itgulov,fogl" \
      "7ijduye7kfykmyfivuifvhukmghkghklliṅfuyjgnjdcgjbg,lo;." \
      "gju kuvjkfckukvkj,k"""
T.insert(END,str)
root.mainloop()