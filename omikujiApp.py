import tkinter as tk
import random # SSIS - 118

def dispLabel():
    kuji = ["大吉", "中吉", "小吉", "凶", "半吉", "未吉", "大大吉"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="PUSH", command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()
