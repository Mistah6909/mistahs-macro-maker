from tkinter import *
tk = Tk()
labelGrid = 0
macro = []
tk.geometry("500x200")
frame1 = Frame(tk)
frame2 = Frame(tk)
frame3 = Frame(tk)
frame4 = Frame(tk)
frame1.pack(side = RIGHT)
frame2.pack(side =TOP)
frame3.pack(side = TOP)
frame4.pack(side = BOTTOM)
A = Button(frame2,text = "A").grid(row=0,column=1)
B = Button(frame2,text ="B").grid(row=0,column=2)
C = Button(frame2,text ="C").grid(row=0,column=3)
D = Button(frame2,text ="D").grid(row=0,column=4)
E = Button(frame2,text ="E").grid(row=0,column=5)
F = Button(frame2,text ="F").grid(row=0,column=6)
G = Button(frame2,text ="G").grid(row=0,column=7)
H = Button(frame2,text ="H").grid(row=0,column=8)
I = Button(frame2,text ="I").grid(row=0,column=9)
J = Button(frame2,text ="J").grid(row=0,column=10)
K = Button(frame2,text ="K").grid(row=0,column=11)
L = Button(frame2,text ="L").grid(row=0,column=12)
M = Button(frame2,text ="M").grid(row=0,column=13)
N = Button(frame2,text ="N").grid(row=0,column=14)
O = Button(frame2,text ="O").grid(row=1,column=2)
P = Button(frame2,text ="P").grid(row=1,column=3)
Q = Button(frame2,text ="Q").grid(row=1,column=4)
R = Button(frame2,text ="R").grid(row=1,column=5)
S = Button(frame2,text ="S").grid(row=1,column=6)
T = Button(frame2,text ="T").grid(row=1,column=7)
U = Button(frame2,text ="U").grid(row=1,column=8)
V = Button(frame2,text ="V").grid(row=1,column=9)
W = Button(frame2,text ="W").grid(row=1,column=10)
X = Button(frame2,text ="X").grid(row=1,column=11)
Y = Button(frame2,text ="Y").grid(row=1,column=12)
Z = Button(frame2,text ="Z").grid(row=1,column=13)
delay = Button(frame3,text="Delay")
spacebar = Button(frame3,text="spacebar")
AText = Label(frame3,text = "Key Press: A")
BText = Label(frame3,text = "Key Press:B")
CText = Label(frame3,text = "Key Press:C")
EText = Label(frame3,text = "Key Press:D")
FText = Label(frame3,text = "Key Press:E")
GText = Label(frame3,text = "Key Press:F")
HText = Label(frame3,text = "Key Press:G")
IText = Label(frame3,text = "Key Press:H")
JText = Label(frame3,text = "Key Press:I")
KText = Label(frame3,text = "Key Press:J")
LText = Label(frame3,text = "Key Press:K")
MText = Label(frame3,text = "Key Press:L")
NText = Label(frame3,text = "Key Press:M")
OText = Label(frame3,text = "Key Press:N")
PText = Label(frame3,text = "Key Press:O")
QText = Label(frame3,text = "Key Press:P")
RText = Label(frame3,text = "Key Press:Q")
SText = Label(frame3,text = "Key Press:R")
TText = Label(frame3,text = "Key Press:S")
UText = Label(frame3,text = "Key Press:T")
VText = Label(frame3,text = "Key Press:U")
WText = Label(frame3,text = "Key Press:V")
XText = Label(frame3,text = "Key Press:W")
YText = Label(frame3,text = "Key Press:X")
ZText = Label(frame3,text = "Key Press:Z")
DelayText = Label(frame3, text = "Delay")

A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
F.pack()
G.pack()
H.pack()
I.pack()
J.pack()
K.pack()
L.pack()
M.pack()
N.pack()
O.pack()
P.pack()
Q.pack()
R.pack()
S.pack()
T.pack()
U.pack()
V.pack()
W.pack()
X.pack()
Y.pack()
Z.pack()
spacebar.pack()
delay.pack()


def Acon():
  AText.pack()
  macro.append("a")

def Bcon():
  BText.pack()
  macro.append("b")

def Ccon():
  CText.pack()
  macro.append("c")

def Dcon():
  DText.pack()
  macro.append("d")
  
def Econ():
  EText.pack()
  macro.append("e")
  
def Fcon():
  FText.pack()
  macro.append("f")
  
def Gcon():
  GText.pack()
  macro.append("g")
  
def Hcon():
  HText.pack()
  macro.append("h")
  
def Icon():
  IText.pack()
  macro.append("i")
  
def Jcon():
  JText.pack()
  macro.append("j")
  
def Kcon():
  KText.pack()
  macro.append("k")
  
def Lcon():
  LText.pack()
  macro.append("l")
  
def Mcon():
  MText.pack()
  macro.append("m")
  
def Ncon():
  NText.pack()
  macro.append("n")
  
def Ocon():
  OText.pack()
  macro.append("o")
  
def Pcon():
  PText.pack()
  macro.append("p")
  
def Qcon():
  QText.pack()
  macro.append("q")
  
def Rcon():
  RText.pack()
  macro.append("r")
  
def Scon():
  SText.pack()
  macro.append("s")
  
def Tcon():
  TText.pack()
  macro.append("t")
  
def Ucon():
  UText.pack()
  macro.append("u")
  
def Vcon():
  VText.pack()
  macro.append("v")
  
def Wcon():
  WText.pack()
  macro.append("w")
  
def Xcon():
  XText.pack()
  macro.append("x")
  
def Ycon():
  YText.pack()
  macro.append("y")

def Zcon():
  ZText.pack()
  macro.append("z")

