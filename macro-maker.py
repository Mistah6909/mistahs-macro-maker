from tkinter import *

tk = Tk()
brake = '\n'
labelGrid = 0
macro = []
tk.geometry("500x200")
frame1 = Frame(tk)
frame2 = Frame(tk)
frame3 = Frame(tk)
frame4 = Frame(tk)
frame1.pack(side=RIGHT)
frame2.pack(side=TOP)
frame3.pack(side=TOP)
frame4.pack(side=BOTTOM)
A = Button(frame2, text="A")
A.grid(row=0, column=1)
B = Button(frame2, text="B")
B.grid(row=0, column=2)
C = Button(frame2, text="C")
C.grid(row=0, column=3)
D = Button(frame2, text="D")
D.grid(row=0, column=4)
E = Button(frame2, text="E")
E.grid(row=0, column=5)
F = Button(frame2, text="F")
F.grid(row=0, column=6)
G = Button(frame2, text="G")
G.grid(row=0, column=7)
H = Button(frame2, text="H")
H.grid(row=0, column=8)
I = Button(frame2, text="I")
I.grid(row=0, column=9)
J = Button(frame2, text="J")
J.grid(row=0, column=10)
K = Button(frame2, text="K")
K.grid(row=0, column=11)
L = Button(frame2, text="L")
L.grid(row=0, column=12)
M = Button(frame2, text="M")
M.grid(row=0, column=13)
N = Button(frame2, text="N")
N.grid(row=0, column=14)
O = Button(frame2, text="O")
O.grid(row=1, column=2)
P = Button(frame2, text="P")
P.grid(row=1, column=3)
Q = Button(frame2, text="Q")
Q.grid(row=1, column=4)
R = Button(frame2, text="R")
R.grid(row=1, column=5)
S = Button(frame2, text="S")
display = Label(frame4,text=macro)
S.grid(row=1, column=6)
T = Button(frame2, text="T")
T.grid(row=1, column=7)
U = Button(frame2, text="U")
U.grid(row=1, column=8)
V = Button(frame2, text="V")
V.grid(row=1, column=9)
W = Button(frame2, text="W")
W.grid(row=1, column=10)
X = Button(frame2, text="X")
X.grid(row=1, column=11)
Y = Button(frame2, text="Y")
Y.grid(row=1, column=12)
Z = Button(frame2, text="Z")
Z.grid(row=1, column=13)
delay = Button(frame2, text="Delay")
delay.grid(row=3, column = 8)
spacebar = Button(frame2, text="spacebar")
spacebar.grid(row=3,column = 7,padx= 10, pady = 10)
label = Label(text = macro)
def Acon():
    global label
    macro.append("Key press: A")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Bcon():
    global label
    macro.append("Key press: B")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Ccon():
    global label
    macro.append("Key press: C")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Dcon():
    global label
    macro.append("Key press: D")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Econ():
  global label
  macro.append("Key press: E")
  macro.append(brake)
  label.forget()
  label = Label(text=macro)
  label.pack()
def Fcon():
    global label  
    macro.append("Key press: F")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Gcon():
    global label
    macro.append("Key press: G")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Hcon():
    global label
    macro.append("Key press: H")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Icon():
    global label
    macro.append("Key press: I")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Jcon():
    global label
    macro.append("Key press: J")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Kcon():
    global label
    macro.append("Key press: K")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Lcon():
    global label
    macro.append("Key press: L")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Mcon():
    global label
    macro.append("Key press: M")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Ncon():
    global label
    macro.append("Key press: N")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Ocon():
    global label
    macro.append("Key press: O")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Pcon():
    global label
    macro.append("Key press: P")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Qcon():
    global label
    macro.append("Key press: Q")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Rcon():
    global label
    macro.append("Key press: R")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Scon():
    global label
    macro.append("Key press: S")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Tcon():
    global label
    macro.append("Key press: T")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Ucon():
    global label
    macro.append("Key press: U")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()

def Vcon():
    global label
    macro.append("Key press: V")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Wcon():
    global label
    macro.append("Key press: W")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Xcon():
    global label
    macro.append("Key press: X")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Ycon():
    global label
    YText.pack()
    macro.append("Key press: Y")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def Zcon():
    global label
    macro.append("Key press: Z")
    macro.append(brake)
    label.forget()
    label = Label(text=macro)
    label.pack()
def DelayCon():
  global label
  macro.append("Delay 1 second")
  macro.append(brake)
  label.forget()
  label = Label(text=macro)
  label.pack()
def SpacebarCon():
  global label
  macro.append("Key press: Spacebar")
  macro.append(brake)
  label.forget()
  label = Label(text=macro)
  label.pack()
A.config(command=Acon)
B.config(command=Bcon)
C.config(command=Ccon)
D.config(command=Dcon)
E.config(command=Econ)
F.config(command=Fcon)
G.config(command=Gcon)
H.config(command=Hcon)
I.config(command=Icon)
J.config(command=Jcon)
K.config(command=Kcon)
L.config(command=Lcon)
M.config(command=Mcon)
N.config(command=Ncon)
O.config(command=Ocon)
P.config(command=Pcon)
Q.config(command=Qcon)
R.config(command=Rcon)
S.config(command=Scon)
T.config(command=Tcon)
U.config(command=Ucon)
V.config(command=Vcon)
W.config(command=Wcon)
X.config(command=Xcon)
Y.config(command=Ycon)
Z.config(command=Zcon)
delay.config(command=DelayCon)
spacebar.config(command = SpacebarCon)
