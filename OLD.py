# -*- coding:utf-8 -*-
import ast
import bdb
import builtins
import ctypes
import keyword
import subprocess
import threading
import pyautogui
directory_name = ".\\"
b_num=r"\b\d+\.?\d*\b"
b_self=r"\b(self|cls)\b"
b_x=r"@\w+"
import time
import PIL,pygetwindow
lines=[]
lines2=[]
ii = 10
try:
    import pyi_splash
    pyi_splash.close()
except:
    pass
import webbrowser
from idlelib import colorizer, percolator
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
from ttkbootstrap.dialogs import Messagebox
from tkinter.colorchooser import askcolor
import _tkinter,customtkinter
import os,pip
import tkinter as tk
import ttkbootstrap as tkk
import sys
from tkinter.filedialog import *
global textMess
default = 1
dark = 0
light = 0
superhero = 0
ad = []
askrq = []
ask = []
i = 1
debug=None
isdebug=False
breakp=set()
curr_frame=None
db_stack=[]
class EditorDB(bdb.Bdb):
    def __init__(self):
        super().__init__()
        self.quitting=False
    def user_line(self, frame):
        global curr_frame,isdebug
        curr_frame=frame
        isdebug=True
        lineno=frame.f_lineno
        highlight_current_line(lineno)
        update_vari(frame)
        update_stack_viewer(frame)
        self.set_step()
        self.set_continue()
    def user_return(self, frame, return_value):
        pass
    def user_exception(self, frame, exc_info):
        exc_type, exc_value, exc_traceback = exc_info
        print(f"Error: {exc_type.__name__}:{exc_value}")
def sto_db():
    global debug,isdebug
    if debug:
        debug.set_quit()
        debug=None
    isdebug=False
    textPad.tag_remove("curr","1.0","end")
    print("[EDB]:Stopped")
global flag
if not os.path.exists("Output.txt"):
    with open("Output.txt", "w") as f:
        f.write("")
sty = tkk.Style(theme="darkly")
root=sty.master
root.config(cursor="mouse")
root.attributes("-topmost", True)
root.update()
root.attributes("-topmost", False)
root.attributes("-alpha", 0.9)
pd = tkk.PanedWindow(root, orient=tk.HORIZONTAL)
n = ttk.Notebook(pd)
global textPad
tab = tk.Frame(n, )
frame = tk.Frame(tab)
my_title = "Python3 Editor"
root.title(my_title)
frame2 = ttk.Notebook(pd)
lbs=tk.Listbox(frame2)
fr=tk.Frame(frame2)
textMess = tk.Text(fr, bg="#1e1f22", undo=1, font=("Lucida Console", 8), state=tk.DISABLED, )
textMess.config(bg="#1e1f22")
frame2.add(fr,text="Output")
tkframe=tk.Frame(frame2,height=12)
terminal=tk.Text(tkframe,height=12)
terminal.pack(fill="both",expand=True,side="left")
lrf=customtkinter.CTkScrollbar(tkframe,orientation=tk.VERTICAL,command=terminal.yview)
lrf.pack(fill="y",side="right")
terminal.config(yscrollcommand=lrf.set)
frame2.add(tkframe,text="Terminal")
terminal.insert("1.0","TERMINAL - Please press [Enter] to start...\n")
terminal["state"]="d"
inp__=tk.Entry(terminal)
class myevent:
    def __init__(self,k):
        self.keycode=k
def rc(e):
    global inp__
    if e.keycode==13:
        if "Please press [Enter]"in terminal.get("1.0","end"):
            terminal["state"]="n"
            terminal.delete("1.0","end")
            terminal["state"]="d"
        try:
            t=inp__.get()
            terminal.see("end")
            tf=subprocess.run(t,shell=1,capture_output=1)
            tx=tf.returncode
            tf=tf.stdout
            terminal["state"] = "n"
            terminal.insert("end",t+"\n")
            terminal.insert("end",tf)
            terminal["state"] = "d"
        except:pass
        finally:
            try:
                inp__.destroy()
            except:pass
            finally:
                terminal["state"] = "n"
                terminal.insert("end",f"\n{os.getcwd()}>")
                inp__=tk.Entry(terminal)
                inp__.bind("<KeyPress>", rc)
                terminal.window_create("end",window=inp__)
                terminal["state"]="d"
                inp__.focus_set()
                inp__.wait_window(inp__)
                return
terminal.bind("<KeyPress>",rc)
fee = tk.LabelFrame(root, text='Files', width=120)
frx=tk.Frame(fee)
tframek=tk.Entry(fee,fg="gray")
tframek.pack(fill="x",expand=False)
tframek.focus_set()
lstbox = tk.Listbox(frx, width=50)
frx.pack(fill="both",expand=True)
def rrrk(ev):
    global lstbox
    d=directory_name
    t=os.listdir(d)
    lstbox.delete(0,"end")
    for i in t:
        if tframek.get() in i:
            lstbox.insert("end",i)
def TFK(e):
    if tframek["fg"]=="gray":
        tframek.delete(0,"end")
        if light:
            tframek["fg"]="black"
        else:
            tframek["fg"]="white"
def TK(E):
    tframek["fg"]="gray"
    tframek.config(fg="gray")
    tframek.delete(0,"end")
    tframek.insert(0,"Filter...")
tframek.bind("<FocusIn>",TFK)
tframek.bind("<FocusOut>",TK)
tframek.bind("<KeyRelease>",rrrk)
lst_pyz=customtkinter.CTkScrollbar(frx, orientation=tk.VERTICAL)
line = tk.Canvas(tab, highlightthickness=0)
cdx = tkk.Combobox(frame, width=60)
cdx.config(state="readonly")
hwndx=ctypes.windll.user32.GetParent(root.winfo_id())
DWA=20
DWA2=19
textPad = tk.Text(tab, undo=1, font=("楷体", 14), spacing1=2, wrap="none")
textPad.focus_set()
global filename
filename = ""
def funcIII(event):
    global textPad, filename, flag
    if filename == "":
        filename = asksaveasfilename(initialfile=filename, defaultextension=".py",
                                     filetypes=[("Python Files", "*.py *.pyw *.pyi"), ("All Files", "*.*")],
                                     title="Save As...")
        if filename != "":
            fh = open(filename, "w", encoding="utf-8", errors="ignore")
            msg = textPad.get("1.0", tk.END)
            fh.write(msg)
            fh.close()
            root.title(f"{os.path.abspath(filename)} - {my_title}")
            flag = 1
            fg.append(os.path.basename(filename))
    else:
        with open(filename, "w", encoding="utf-8") as f:
            msg = textPad.get(1.0, tk.END)
            f.write(msg)
cdxval = []
def fxf(e=None):
    upd(None)
    curr=textPad.index(tk.INSERT).split(".")[0]
    now=int(curr)
    jsq=1
    idx3264=1
    for i in lines:
        if abs(e.y-i)<15:
            jsq=idx3264
        idx3264+=1

    now=lines2[jsq-1]
    if now in breakp:
        breakp.remove(now)
        textPad.tag_remove("breakpoint", f"{now}.0", f"{now}.end+1c")
        print("INFO:Breakpoint removed")
    else:
        breakp.add(now)
        textPad.tag_add("breakpoint",  f"{now}.0", f"{now}.end+1c")
        print("INFO:Breakpoint added")
    textPad.tag_config("breakpoint", background="#40252b",foreground="yellow")
    upd(None)
line.bind("<Button>",fxf)
def upd(event):
    global textPad, filename, flag,lines,lines2
    line.delete("all")

    textPad.tag_remove("act", "1.0", "end")#    highlightthickness=2,    #
    textPad.tag_add("act", "insert linestart", "insert lineend+1c")
    i = textPad.index("@0,0")
    dl = textPad.dlineinfo(i)
    h, y = i.split(".")
    line.create_text(1, dl[1], anchor="nw", font=("楷体", 11), text="{0:>2}".format(1), fill="#c6c07b")
    ind = 0
    id_obj=1
    line_wid=line.winfo_width()
    for breakpoim in breakp:
        dl=textPad.dlineinfo(str(breakpoim)+".0")
        if dl:
            y=dl[1]
            line.create_text(line_wid-35,y+5,anchor="nw", font=("楷体", 11), text="{}".format("✅"),fill="red")
    lines=[]
    lines2=[]
    while 1:
        dl = textPad.dlineinfo(i)
        h, y = i.split(".")
        debug222 = textPad.get(i)
        id_obj+=1
        if dl == None:
            break
        if y == "0":
            yl = dl[1]
            lines.append(yl)
            lines2.append(h)
            ln = h
            if ln == 1: continue
            leng = len(str(ln))
            line.config(width=leng * 11 + 44)
            lnp = textPad.index("insert").split(".")[0]
            if lnp == str(ln):
                if light:
                    colour="#000011"
                else:
                    colour="#eeeefe"
                line.create_text(1, yl, anchor="nw", font=("Consolas", ii), text="{0:>2}".format(ln), fill=colour)
            else:
                line.create_text(1, yl, anchor="nw", font=("Consolas", ii), text="{0:>2}".format(ln), fill="gray")
        i = textPad.index(str(int(h) + 1) + "." + "0")
        j = 1
def __undo__():
    try:
        textPad.edit_undo()
    except:
        pass
def __redo__():
    try:
        textPad.edit_redo()
    except:
        pass
pd.add(n,)
pd.add(frame2)
class Tip:
    def __init__(self, widg, txt):
        self.widg = widg
        self.text = txt
        self.toolt = None
        self.widg.bind("<Enter>", self.show)
        self.widg.bind("<Leave>", self.hide)
    def show(self, e):
        if self.toolt == None:
            x, y, _, _ = self.widg.bbox("insert")
            x += self.widg.winfo_rootx() + 25
            y += self.widg.winfo_rooty() + 25
            self.toolt = tk.Toplevel(self.widg)
            self.toolt.attributes("-topmost", True)
            self.toolt.wm_overrideredirect(True)
            self.toolt.wm_geometry("+%d+%d" % (x, y))
            self.toolt.configure(background="#1e1f22", relief="solid", borderwidth=2)
            tkk.Label(self.toolt, text=self.text, ).pack()
    def hide(self, e):
        if self.toolt != None: self.toolt.destroy();self.toolt = None
n.add(tab, text="Work Area")
k_prefix=""
class VariableVisitor(ast.NodeVisitor):
    def __init__(self):
        self.variables=set()
    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Load,ast.Store)):
            self.variables.add(node.id)
        self.generic_visit(node)
    def visit_FunctionDef(self, node):
        self.variables.add(node.name)
        self.generic_visit(node)
kp_win=None
def on_k_rel(keyw):
    global kp_win
    global k_prefix,textPad
    def show(mt):
        global kp_win,k_prefix,textPad
        try:
            kp_win.destroy()
        except:pass
        kp_win=tk.Toplevel(root)
        kp_win.attributes("-topmost",True)
        kp_win.overrideredirect(True)
        x,y,_,_=textPad.bbox("insert")
        x+=textPad.winfo_rootx()+25
        y+=textPad.winfo_rooty()+25
        kp_win.geometry(f"+{x}+{y}")
        lstbgv=tk.Listbox(kp_win,height=min(5,len(mt)))
        tl=customtkinter.CTkScrollbar(kp_win,orientation=tkk.VERTICAL,command=lstbgv.yview,height=min(5,len(mt)))
        lstbgv.config(yscrollcommand=tl.set)
        lstbgv.pack(fill="both", expand=1,side=tk.LEFT)
        tl.pack(side="right",fill="y")
        for smt in mt:
            lstbgv.insert(tk.END, smt)
        def ins(ev):
            i=lstbgv.get(lstbgv.curselection())
            textPad.focus_set()
            textPad.delete("insert"+"-"+str(len(k_prefix))+"c","insert")
            textPad.insert("insert", i)
            kp_win.destroy();return
        lstbgv.bind("<<ListboxSelect>>", ins)
        kp_win.bind("<Escape>",lambda e:kp_win.destroy())
    try:
        kp_win.destroy()
    except:
        pass
    if keyw.keysym in ("BackSpace","Space","Escape","Up","Down","Left","Right","Delete"):
        try:
            kp_win.destroy()
        except:pass
        return
    lin=textPad.get("insert linestart", "insert")
    if lin and (lin[-1].isalnum()or lin[-1] in (".","_")):
        index_0FF=textPad.index("insert")
        k_prefix=""
        for c in reversed(lin):
            if c.isalnum() or c in( ".","_"):
                k_prefix=c+k_prefix
            else:break
        bj=True
        tree = ast.parse(textPad.get("1.0", "end"))
        vst = VariableVisitor()
        vst.visit(tree)
        kwo=['False', 'None', 'True', 'and', 'as','assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del','elif', 'else', 'except','finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal','not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
        built=dir(builtins)
        kwo=built+kwo
        kwo.sort()
        kwo=list(vst.variables)+kwo
        kwo=list(set(kwo))
        kwo=sorted(kwo)
        if textPad.get("insert linestart", "insert lineend").startswith("import") or textPad.get("insert linestart","insert lineend").startswith("from"):
            kwo=[]
        try:
            d=os.listdir(os.path.dirname(os.__file__))
            for i in range(len(d)):
                if textPad.get("insert linestart","insert lineend").startswith("import")or textPad.get("insert linestart","insert lineend").startswith("from"):
                    kwo.append(d[i].replace(".py",""))
                    tx=1
        except Exception as e:
            print(e)
        for idx in kwo:
            if  idx.startswith(k_prefix)  and k_prefix!=idx:bj=False
        if bj:
            try:
                kp_win.destroy()
            except:
                pass
            return "break"
        mt_s=[wo for wo in kwo if wo.startswith(k_prefix) and k_prefix!=wo]
        if mt_s:
            show(mt_s)
    else:
        try:
            kp_win.destroy()
        except:pass
textPad.bind("<KeyPress>",on_k_rel)
def repl_all(ev=None):
    win=tkk.Toplevel(root)
    win.overrideredirect(True)
    win.place_window_center()
    tk.Label(win, text="Replace:").pack()
    itx=tk.Entry(win)
    itx.pack()
    tk.Label(win, text="Replace To:").pack()
    itx2=tk.Entry(win)
    itx2.pack()
    def ev2():
        repl_t=textPad.get("1.0","end")
        repl_t=repl_t.replace(itx.get(),itx2.get())
        textPad.focus_set()
        textPad.delete("1.0","end")
        textPad.insert("insert",repl_t)
        win.destroy()
        upd("")
        get__()
    tkk.Button(win, text="Replace All",command=ev2,bootstyle="outline").pack()
    tkk.Button(win, text="Close",command=lambda:win.destroy(),bootstyle="outline-warning").pack()
textPad.bind("<Control-R>",repl_all)
textPad.bind("<Control-r>",repl_all)
def get__(e=None):
    global imlt,k_prefix,lbs
    import re
    try:
        on_k_rel(e)
    except:pass
    textPad.tag_remove("at", "1.0","end")
    for match in re.finditer(b_num, textPad.get(1.0, tk.END), re.DOTALL):
        ST = f"1.0+{match.start()}c"
        ED = f"1.0+{match.end()}c"
        textPad.tag_add("at", ST, ED)
    textPad.tag_config("at", foreground="#2aacb8")
    textPad.tag_remove("mt", "1.0","end")
    for match in re.finditer(b_self, textPad.get(1.0, tk.END), re.DOTALL):
        ST = f"1.0+{match.start()}c"
        ED = f"1.0+{match.end()}c"
        textPad.tag_add("mt", ST, ED)
    textPad.tag_config("mt", foreground="#f35374")
    textPad.tag_remove("xt","1.0","end")
    for match in re.finditer(b_x, textPad.get(1.0, tk.END), re.DOTALL):
        ST = f"1.0+{match.start()}c"
        ED = f"1.0+{match.end()}c"
        textPad.tag_add("xt", ST, ED)
    textPad.tag_config("xt", foreground="#7d771e")
    textPad.tag_remove("lt","1.0","end")
    for mt in re.finditer(r"\b\w+\s*\(([^)]*)\)",textPad.get(1.0, tk.END)):
        st = f"1.0+{mt.start(1)}c"
        stri=mt.group(1)
        for p in re.finditer(r"(\w+)\s*=",stri):
            st0=f"{st}+{p.start(1)}c"
            ed=f"{st}+{p.end(1)}c"
            textPad.tag_add("lt", st0, ed)
    textPad.tag_config("lt", foreground="#aa4926")
    textPad.tag_remove("act", "1.0", "end")
    textPad.tag_add("act", "insert linestart", "insert lineend+1c")
    err = 0
    errs = ""
    try:
        compile(textPad.get(1.0, tk.END), "<string>", "exec")
    except SyntaxError as e:
        errs = f"     [SyntaxError]Error Line : {e.lineno}  ,  Error : {e.msg}"
        err = 1
    try:
        l, c = textPad.index("insert").split(".")
        cou = int(textPad.index("end-1c").split(".")[0])
        if dark == 1 or superhero == 1 or default == 1:
            t.config(
                text=f"{l} : {int(c) + 1}  |  Total lines:{cou}  |  {len(textPad.get('1.0', tk.END))} Bytes",
                foreground="white")
        else:
            t.config(
                text=f"{l} : {int(c) + 1}  |  Total lines:{cou}  |  {len(textPad.get('1.0', tk.END))} Bytes",
                foreground="black")
        t2.config(text=f"{os.path.basename(root.title())}")
        if err:
            t.config(
                text=f"{l} : {int(c) + 1}  |  Total lines:{cou}  |  {len(textPad.get('1.0', tk.END))} Bytes" + errs,
                foreground="red")
            t2.config(text=f"{os.path.basename(root.title())}[Please Check Error]")
    except:
        pass
    if dark == 1 or superhero == 1 or default == 1:
        textPad.tag_config("act", background="#474747")
    else:
        textPad.tag_config("act", background="#d8d8d8")
    upd("")
    textPad.tag_remove("self", "1.0", "end")
    start = "1.0"
    if not light:
        textPad.config(selectbackground="#214283")
    else:
        textPad.config(selectbackground="#a6d2ff",selectforeground="black")
    textPad.config(highlightcolor="#14375e",highlightthickness=2)
    textMess.config(highlightcolor="#14375e",highlightthickness=2)

    lbs.delete(0, "end")
    try:
        tree = ast.parse(textPad.get("1.0", "end"))
        vst = VariableVisitor()
        vst.visit(tree)

        for identfilter in vst.variables:
            lbs.insert(0,identfilter)
    except:
        pass
get__()
def bqkh(ev):textPad.insert(tk.INSERT,"()");pyautogui.press("left");return "break"
def b3qkh(ev):textPad.insert(tk.INSERT,"{}");pyautogui.press("left");return "break"
def b34qkh(ev):textPad.insert(tk.INSERT,"[]");pyautogui.press("left");return "break"
textPad.bind("<(>", bqkh)
textPad.bind("<{>", b3qkh)
textPad.bind("<[>", b34qkh)
word = """#This is a demo python code.
\"\"\"greet.func\"\"\"
def print_hi(w="HI"):
    print(\"#\"*10,\"Welcome!\",\"#\"*10)
    print(\"*\"*10,w,\"*\"*10)
    for i in range(10):
        for j in range(i):
            print(\"*\",end=\"\")
        print()
\"\"\"PyInt.class\"\"\"
class PyInt(int):
    def __init__(self,n):self.n=n
    def __str__(self):return str(self.n)+\"_PyInt\"
if __name__ == \"__main__\":
    print_hi()
    print(PyInt(100))
    n=input(\"Your Name:\")
    print(n)
\"\"\"[END]\"\"\"
"""
def comment():
    try:
        startf, endf = textPad.index("sel.first").split(".")[0], textPad.index("sel.last").split(".")[0]
        if startf and endf:
            for i in range(int(startf), int(endf) + 1):
                textPad.insert(f"{i}.0", "#")
    except:
        pass
    finally:
        upd("")
        get__()
textPad.insert(1.0, word)
textPad.config()
direct = [[], []]
for directs in os.listdir("./"):
    lstbox.insert(tk.END, str(directs))
    direct[0].append(os.path.abspath(directs))
    direct[1].append(directs)
flag = 0
try:
    with open("idleConf.edc", "r", encoding="utf-8") as ff:
        word = ff.read()
except:
    with open("idleConf.edc", "w", encoding="utf-8") as ff:
        ff.write("de");word = "de"
def to_light():
    TK("")
    tframek.config(fg="gray")
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwndx, DWA2, ctypes.byref(ctypes.c_int(0)),
                                               ctypes.sizeof(ctypes.c_int(0)))
    try:
        global light, dark, superhero, default, light, dark, superhero, word
        sty.theme_use("litera")
        textPad.tag_config("sel",background="#0161af")
        light = 1
        dark = 0
        default = 0
        superhero = 0
        with open("idleConf.edc", "w", encoding="utf-8") as ff:
            ff.write("lg");word = "lg"
        get__()
        TK("")
    except:
        pass
def to_dark():
    tframek.config(fg="gray")
    TK("")
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwndx, DWA2, ctypes.byref(ctypes.c_int(1)),
                                               ctypes.sizeof(ctypes.c_int(1)))
    try:
        global dark, light, superhero, default, word
        sty.theme_use("darkly")
        light = 0
        dark = 1
        textPad.tag_config("sel",selectbackground="#214283")
        default = 0
        superhero = 0
        get__()
        with open("idleConf.edc", "w", encoding="utf-8") as ff:
            ff.write("dk");word = "dk"
        TK("")
    except:
        pass
def to_blue():
    tframek.config(fg="gray")
    TK("")
    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwndx, DWA2, ctypes.byref(ctypes.c_int(1)),
                                               ctypes.sizeof(ctypes.c_int(1)))
    try:
        textPad.tag_config("sel",selectbackground="#214283")
        global light, dark, superhero, default
        light = 0
        dark = 0
        default = 0
        superhero = 1
        textPad.config(selectbackground="#214283")
        sty.theme_use("superhero")
        global word
        with open("idleConf.edc", "w", encoding="utf-8") as ff:
            ff.write("sup");word = "sup"
        get__()
        TK("")
    except:
        pass
def to_l():
    tframek.config(fg="gray")

    TK("")
    try:
        textPad.tag_config("sel",selectbackground="#214283")
        global light, dark, superhero, default, word
        light = 0
        dark = 0
        default = 1
        superhero = 0
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwndx, DWA2, ctypes.byref(ctypes.c_int(1)),
                                                   ctypes.sizeof(ctypes.c_int(1)))
        sty.theme_use("darkly")
        textPad.config(selectbackground="#214283")
        textMess.config(bg="#1e1f22")
        get__()
        with open("idleConf.edc", "w", encoding="utf-8") as ff:
            ff.write("de");word = "de"
        get__()
        TK("")
    except:
        pass
if "de" in word: to_l()
if "lg" in word: to_light()
if "dk" in word: to_dark()
if "sup" in word: to_blue()
o1 = sys.stdout
o2 = sys.stderr
TK("")
def exit_(event=None):
    global textPad, filename, flag,commandinp
    import ttkbootstrap.dialogs.dialogs
    if ttkbootstrap.dialogs.dialogs.Messagebox.show_question("Really Exit?","Exit",buttons=("Exit","Return"))=="Exit":
        try:
            try:
                commandinp.destroy()
            except:pass
            sys.stdout = o1
            sys.stderr = o2
            funcIII("")
            try:
                inp__.destroy()
            except:pass
            root.quit()
            exit(0)
        except:
            try:
                commandinp.destroy()
            except:pass
            root.quit()
            sys.stdout=o1
            sys.stderr=o2
            try:
                inp__.destroy()
            except:pass
            sys.exit()
    else:
        return
root.geometry("2290x1234")
ftn = 1234
global ase
ase = []
try:
    root.iconbitmap(".\\rrrr.ico")
except:
    with open("rrrr.ico", "wb") as ff:
        ff.write(
            b'\x00\x00\x01\x00\x01\x00\xc0\xc0\x00\x00\x01\x00 \x00g\x0b\x00\x00\x16\x00\x00\x00\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc0\x00\x00\x00\xc0\x08\x06\x00\x00\x00R\xdcl\x07\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\xb4eXIfII*\x00\x08\x00\x00\x00\x06\x00\x12\x01\x03\x00\x01\x00\x00\x00\x01\x00\x00\x00\x1a\x01\x05\x00\x01\x00\x00\x00V\x00\x00\x00\x1b\x01\x05\x00\x01\x00\x00\x00^\x00\x00\x00(\x01\x03\x00\x01\x00\x00\x00\x02\x00\x00\x00\x13\x02\x03\x00\x01\x00\x00\x00\x01\x00\x00\x00i\x87\x04\x00\x01\x00\x00\x00f\x00\x00\x00\x00\x00\x00\x00H\x00\x00\x00\x01\x00\x00\x00H\x00\x00\x00\x01\x00\x00\x00\x06\x00\x00\x90\x07\x00\x04\x00\x00\x000210\x01\x91\x07\x00\x04\x00\x00\x00\x01\x02\x03\x00\x00\xa0\x07\x00\x04\x00\x00\x000100\x01\xa0\x03\x00\x01\x00\x00\x00\xff\xff\x00\x00\x02\xa0\x04\x00\x01\x00\x00\x00\xc0\x00\x00\x00\x03\xa0\x04\x00\x01\x00\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00V\xdbA\x0f\x00\x00\nYIDATx\x9c\xed\x9d]\xac]E\x19\x86\x9f}Z \x84\n\xb1\x04\xb5\x95Xk(\x12.L5R\xc0D\xa2\xa7\xf1J\x05be\x036\x11bDn\xd0\x1a\x01I\x13bLH4j\xabb\xebO\x8b\x15\x15/4^\x99(j\xb8A\x83"\xa9\x9a\xf6B\x8b\x06\x10\xe3\x0f\xa2P\xb0\xa5J[\xdbeF\xe7\xa4\x9br~\xf6\xda\xe7\x9b\xff\xf7I\xe6b\xdf\xac\xf9\xd6\xac\xefY3k\xf6\x9a5\x03\xca\xe0\x15\xc04p1p\x01\xf0\x1a\xe0l`\x19pJ\xea\xe02\xe3(\xf0\x1c\xf0\x14\xf0\x18\xf00\xf0 p?\xf0d\xea\xe0\xc4\xf8\xb8\x04\xff\x10\xb0\x1b\xe8TL\x8a\x13\xe1&`y\xea\x8b+\xe6\xe6\\\xe0\xf3\xc0\xa1\x0c\x12\xa6\xd6\xe2z\x88\xcf\x01+S_lq\x027\x94\xd9\x04\x1c\xcc AZ)\x87\x80\x8f\x03\xa7\xa5\xbe\xf8\xad\xf3Z`O\x06\t\xd1j\xd9\xe3\xaf\x81H\xc0\x06\xdd\xf5\xb3(\x07\x81w\xa7N\x86\xd6\xb8\xde\xcfZ\xa4\xbe\xf8*\xfc\xaf\x1c\x07nN\x9d\x14\xadpc\x06\x17\\\x85Y\xcb\xed\xa9\x93\xa3\x85a\xcf\x7f2\xb8\xd0*\xccY6\xd3\x00K\x12\xd4y\x1ep/pz\x82\xba\xc5\xf8\xac\x07\x8e\x01?\xa5bb\x0bp*p\x1f\xb0*r\xbdb2\xa6\x81#\xc0\x03TJl\x01n\x056F\xaeS,\x8e\xf55\xf7\x041\x05x%\xf0]\xdf\x0b\x88\xb2\x98\xae\xb5\'\x88)\xc0\x1d\xc0\x9b#\xd6\'lY_cO\xb0$\xe2\x8bm\xdf\xd2\x9b\x9b\xc53][O\x10K\x80\x1b\x80\xcb#\xd5%\xc2\xb2\xbe\xa6\x9e \x96\x00\xdb\xf5\xe6aUL\xd7\xd6\x13\x84d\x85\xff\x8b=\xf5\x1f;*\xf6\xe5v\ngi\x84:\xde\x02\x0c\x0c\x8f\xe7\xfeA\xfe\xa6\x7f\xa6p\xab\x9d\x9e\xa7-\xf6\x93\x0fw\xf8\xe1\xd0\'S\x07\x923w\x1a\xdeq\xdc\x92\xbeKh\x9b.\xc3\xb29u\xa3\xe4\xcc\x8f\x8d\x1a\xd9\x8d9\xd7\xa5>\x99\x0cH\x9d\xec\x9d$\xe8\xc7\xa3F\r\xfc\xe5\xd4\'\x92\t\xa9\x13\xbd\x93\x04\xfdx\xda\xa8q/M}"\x99\x90:\xc9;I\xd0\x8f\xc3F\r\xeb>\x81"\xd2\'x\xd7\xc2\xec\x90%V\x8d*\xfeO\xea\xe4\xee\xd4\x13\xf4C\x02\xd8\x92:\xb1;\xf5\x04\xfd\x90\x00\xb6\xa4N\xeaN\x12\xf4C\x02\xd8\x92:\xa1;I\xd0\x0f\t`K\xead\xee$A?$\x80-\xa9\x13\xb9\x93\x04\xfd\x90\x00\xb6\xa4N\xe2N\x12\xf4C\x02\xd8\x92:\x81;I\xd0\x0f\t`K\xea\xe4\xed$A?$\x80-\xa9\x13\xb7\x93\x04\xfd\x90\x00\xb6\xa4N\xdaN\x12\xf4C\x02\xd8\xd2UX>L\xc5H\x00[\xba\n\xcb1\xe0\xaa\x14\x8di\xb9Tq.\xba\x82b-\x81Zo\x06\x87\x80\x8b\x80}1+\x9d\x8aY\x99\x10\xf3p\x06\xf0\xed\xd8\xdb5I\x00\x91\x13\xaf\x03>\x12\xb3B\r\x81\xca\xa3\xd6!\xd0\xe8P\xc8\xedW\xf6\x17"\xa0\x1e@\xe48\x14\xba%Ve\xea\x01\xca\xa3\xf6\x1e`\xa6\x17X\xe5\xd7\x93\x07E=\x80\xc8\xb5\x17\xb86FE\x12@\xe4J\x94\x8dT4\x04*\x8f\x16\x86@3\xe7\xb9\xc2\x7f\r0\x18\xea\x01D\xae\xb8\x1b\xdee\xa1+\x91\x00"g\xde\x14\xba\x02\tP\x1e\x07i\x87\xf3CW \x01\xca\xe3\t\xdaaM\xe8\n$@\x99\x1f\x1bn\x85\xe5\xa1+\x90\x00\xe5\xf1\x03\xda\xe1%\xa1+\xd04hy\x9c\x0b<\x9e`\x93\xf3T\x04\xbd\xee\xea\x01\xca\xe3\xcf\xc0\xdd\xa9\x83\xa8\x05\xf5\x00e\xb2\xd2\xef\x8f\x16|\x88\x90\x01\xea\x01\xc4\x8b\xf8+p\xb5_J(2Gk\x82\xc3\xf1A/AWq)\x1e5DX\xde\t\x1c\xc8 Q;\t0;j\x88\xf0\x9c\xe3\xb7\xa3=\x9aA\xc2v%\t\xa0\x87\xe0\xfa\xa6H\xaf\x00\xde\x0e\xac\xf6\xbfK\xdf[m@\xe1\x14q\'\x10\xa6\x0cK\xb9\xee\x9a\x05\x12M#\x01D\xd3H\x00\xd14\x12@4\x8d\x04\x10M#\x01D\xd3H\x00\xd14\x12@4\x8d\x04\x10M#\x01D\xd3H\x00\xd14\x12@4\x8d\x04\x10M#\x01D\xd3H\x00\xd14\x12@4\x8d\x04\x10M#\x01D\xd3H\x00\xd14\x12@4\x8d\x04\x10M#\x01D\xd3H\x00\xd14\x12@4\x8d\x04\x10M#\x01D\xd3H\x00\xd14\x12@4\x8d\x04\x10M#\x01D\xd3H\x00\xd14\x12@4\x8d\x04\x10M\xb3\x94\xb2\xb6\xca\xc9a\xa7\x18\xb7C\xfb\xc5\xc0\x1b\x81\xe5\xc0~\xe0!`7p<\xe2\x8d\xeb"`\x1d\xf0R\xe0\x19\x1f\xc3/#\xc6 \xc6\xc4j\xab\x9c\x1c\xf6\x8a\xba\x16xl\x8e\xf8~\x0fl\x88\x10\xc3U\xc0#\xf3\xc4\xf0.\xd23,e\x8b\xa4\x18\x1c\xaf@\x00w\xc7\xfd\xe2\x98qn\t\x14\x83;\xff\xadc\xc6\xb05q{\r%@=\x02\xb8\xe4\xffF\xcfX\xdf\x17 \x8e\xdbz\xc6\xb03a\x9b\r%\xc0\t\xac\x1ab\x90(\xf9\xbf>A\xacO\x02\xa7\x1b\xc6\xb1\nx~\x828v%\x9a\xe8\x18J\x80\xf2{\x80I\xee\xfc\xa3\xc5=/X\xf1\xe9E\xc4\x91\xa2\'\x18J\x80\xb2\x05Xl\xf2\xbb\xb2\xc30\x9e\xbd\x8b\x8c%\xb6\x04C\tp\x02\xab\x86\x18d>\xec9\xb9\xdck\x18\xd3\x01\x83xb\x0e\x87\x86\xa5\x08\xa0?\xc2^\xdc\x1e_\x03\xae38\x96\xe5\xc5\xb3\x98\xdbw\x0f\xe6w\xe9\x9a\xbf\x90\x18\x8d\xd1\x15\xd4\x16w\x1b%\xbf\xe3O\xd8\xf1\x07\xa3\xe38\t\xbe\x92\xc9\x7f*Y\xa0\xbb\xc1\x0b\x93\xff\xbd\x86\xc7\xfc\x89\xe1\xb1~dx\xac\x1b\xfc\xf3\xc9\xc0\xf0\x98\xa2\xe0g\x00\xab1\x7f\xc8i\xd0\x95\xc0\xbf\x8cc\xdc\x15\xf0\x06X\xcc3@\xeb\xb3@\x16\xb3=\xb1\xfe\x08\xdb\x14 \xce\x9d\x81\xdaU\x02\x14 @\xa8\xe4wI\x15\x8a/\x14"\xc1P\x02\x9c\xc0\xaa!\x06\x99\x0f{bL5\x0e\x02I\xb0\xcb8n\t\x90\xb1\x00\xa5&\xff\x0c\xae\x1d\xb6e\x1e\xffP\x02\xe4)@\xe9\xc9_\x8a\x04C\t\x90\x9f\x00\xb5$\x7f\t\x12\x0c%@^\x02\xd4\x96\xfc3\xb86\xd9\x9e\xe1y\r%@>\x02\xd4\x9a\xfc9K0\x94\x00yL\x83\x0e\x02%\x7fn\xef\xd4\x0c\xfc+\x0e\xd6\xe7\xb9c\xc2x$@&\x02|\xac\x81\xe4\x0f-\xc1\xad\x13\xc4"\x01F\xe8\x12\t\xb0\x068R\xe9\xb0g.\x06=\xd6.wc\x96\xc3\xc0\xea\x9eqH\x80\x0cz\x80;\x1b\xb9\xf3\x9f\xcc\xc0\x0f],\xcf\xfdS=c\x90\x00\x19\x08\xf0p\x83\xc9?\xc3\xc0\xbf\xe2`u\xfe{{\xd6/\x01F\xe8\x12\t0\xc9"\xf2\x12\x87=1\x86C\x07j\x15\xa0\xc4\x0b;.\xfaB\x9a\xdd\xeb#\x9d\xd1q\x9a$\xd5\x10\xe8\xb7\r\x0f\x81\xa6|\xccV\xe7\xbf\xb7g\xfd\xea\x012\xc0r\x15\xd5\xfb\xfd\x83e\t\xed5\xe5cu1\xe7\xd8\x96\xcd\xd1%\xea\x01^m\xf8\x1cP\xca\xf3\x80k\xa3/\x19\x9f\xf3\xbf\x81W\xd5\xda\x03\xd4\xfeG\xd8G\x8d\x93!\xe7\xe1\x90\xf5\xb0\xa7\xf3\xe5\xe6\tb\x91\x00\x19\xad\x08\xb3\x9e\x13\xef\xfc\x14\xe3T\x03\xc9\xbfc\xc2x$\xc0\x08]b\x01B\xfc;\x9a\xd3p(\xc4\xb0\xa7\x03\xbe\xaa\x97\xe1\xea\x10\xa0f\trL~\x87\x04\xc8L\x80\x1a%\xc85\xf9\x1d\x12 C\x01j\x92 \xe7\xe4wH\x80L\x05\xa8A\x82\xdc\x93\xdf!\x012\x16\xa0d\tJH~\x87\x04\x080\r:\x95\xf9\x1b\x93!\xf6\x0589\xde\x10S\x9d;\xf5a\xac6\x05\x08)\xc1$\xab\xa8\x16bs!\xc9\xef\x90\x00#\xe4\xfeq\xdc\\VQ-\xf4Z\xc7\xe1\xcc\x87=\xa3H\x80Bz\x80\x90=A\xdfUT\xf3\xf1Y\xe3\xd8Bo\x994\x94\x00e\t\x90\xc3*\xaa\xf9\xf8MA\xc9\xef\x90\x00#X5\xc4\xa0\xf2UT\xf3q\xa8\x80a\xcf(\x12\xa0P\x01,%\xf8\xa7aL\xcf\x15\x94\xfc\x0e\tP\xe0\x10\xc8z8\x94\xd3\x10H\xdb\xa4\xceA\x0eo3\xe6\x88k\xf8\x1b\xfd\xbc{\x0e\xab\xa8\x16s\xac\xbb\xfc\xb9Tq7-\x11\xab;A\x8aM\xdd&\x1d\x0eM\xb2\x8aj>VM\xb8\xba-\xe6\xb0\xa7\xc8\x1e \x06%\x0e\x81\x16;\x1c\x9ad\x15\xd5B\xdc\x96\xf9\xb0g\x14\tP\x91\x00\xf8D\xda2f\x9c\x9f\xc9 \x86-\x89\xb7A\x1dJ\x80\xba\x04\x98\xe1\n`\xdf\x1c\xf1\xb9\xcf\xb0\\\x1e!\x86+\xe7\xf9\xea]\xac\x18\xaa\x11`\x10I\x00\x8bz\x96d\xf2\xb1+w.\xaf\x07\xd6\x01g\x01\xcf\x00\xbb\x81=\x11\xefX9\xc4\xb0\x90\x00\xdf\xc1\x86\xe27\xf4\xb6\xba\x13\x14\xdf\x10\r1,\xa5\x07\xc8aX!D2$\x80h\x1a\t \x9aF\x02\x88\xa6\x91\x00\xa2i$\x80h\x1a\t \x9aF\x02\x88\xa6\x91\x00\xa2i$\x80h\x1a\t \x9aF\x02\x88\xa6\x91\x00\xa2i$\x80h\x1a\t \x9aF\x02\x88\xa6\x91\x00\xa2i$\x80h\x1a\t \x9aF\x02\x88\xa6\x91\x00B\x04f\x92O\xfa\xcdV\xceL}"bl\xce4\xba\xe6.w\x8a\xef\x01\xdc\xa7\xbd-\xb8\xd0\xe88"<\x17\x1a\x1d\xe7 \x15\x08\xe0>\xdad\xc1F\xa3\xe3\x88\xf0l4:\xce~*\xe0\x87\x86\xdd\xe1\xda\xd4\'#\x16d\xad\xe1\x86~\xdf\xa7\x82\x1e\xe0wF\xc79\xcd7\x88$\xc8\x97\xb5\xfe\x1a\x9d\x9aY\xee$\xe5\x1a\xc3\xcf\xe4u\xfe\xee\xb2\r\xb8\x14X\x96\xfa\xe4\x04\xcb\xfc\xb5\xd8\x16`+\xd7\r\xa1\x83\x8f\xf1\xbd\xcd\x97\x01\x7f\xd3\xb7=EO\xdc\x87\x90_\x0e<E\xe1C\xa0\xbf\xfb/\x17\x0b\xd1\x87\x9f\x87N\xfe\x98\x7f\x84\xdd\x13\xa9\x1eQ\x0f\xf7\xc4\xa8$\xd6\xb0\xe4l\xe0\x8f\xc0\x19\x91\xea\x13es\xc0\xef\xb1f\xb9\xd5l\xd2\x1e\xe0i\xbfg\x95\x10\xe3\xb0=F\xf2\x13\xf9\xc1t\xa5\x9f\xd6\xd2\xcc\x8d\x98\x8fg\x81\xf3\x81\x7f\x10\x01\xb7\xedP,\xdc\xdf\xda\xc7\x80\xb7E\xacS\x94\xc7-\xc0\xfd\xb1*\x8b=5y\n\xf0\x90\xdf\xdfJ\x88\xd9f~.\xf37\xca(\xa4\x98\x9b?\x0f\xf8\x95\xde\xee\x14\xb3\xbc3\xf6\x06\xe0q*_\x0f\xf0\x08p]L\xcbE\xf6\x1c\x01\xae\x8e\x9d\xfc\xb1\x9f\x01Fq\xfb\xdc>\x01\xbcC\xff\x107\xcfq\x7fC\xfc\x1e\rr=p\xd4\xf8\xfd\x11\x95r\xcaa\xe0=4\xce\x95~\xce7\xf5\xc5P!jq\xaf9hF\xd0\xb3\x06\xf8u\x06\x17E\x85(\xe5g\xfe\x9f^1\xc2R`\x93\xff\x1b<\xf5\x05R!Hy\xd6_\xe3T\xcf\x9eE\xb0\x02\xd8\xea\xd7\x12\xa7\xbe`*\x98\x147\xc4\xfd\x04pN\xea\xe4*\x89\xe5\xc0M\xc0/\xfcLA\xea\x8b\xa8B\xaf\xe2\xa6\xb9\x1f\x00>\x00\x9cE\xa6\x942\x05\xe9\x16\xd5\xbc\x15\xb8\x04\xb8\x00X\xed\xef&\xcb\x0c\x97\xdf\t&\xc2\xcd\xe1\xbb\xd7\\\xdcC\xed\xa3\xc0>\xe0A\xff:\x83{\t2k\xfe\x0b\xf4C\x90%\xc1K\xe3\x01\x00\x00\x00\x00IEND\xaeB`\x82')
root.iconbitmap("rrrr.ico")
fg = []
pos=""
lstbval=()
def exp(dn):
    global lstbval,pos
    d = directory_name
    lstbval=lstbox.get("0","end")
    posxy=list(lstbval).index(dn)
    pos=str(int(posxy)+1)
    if os.listdir(d.replace("/","\\") + f"\\{dn}")==[]:
        return
    if dn+"\\"+os.listdir(d + f"\\{dn}")[0] in lstbval:
        lstbox.delete(pos,str(int(pos)+len(os.listdir(d + f"\\{dn}"))-1))
        return
    for i in os.listdir(d + f"\\{dn}"):
        if dn + "\\" + i in lstbval:continue
        lstbox.insert(pos, dn + "\\" + i)
        askrq.append(dn + "\\" + i)
        ask.append(dn + "\\" + i)
        pos=str(int(pos)+1)
#
#此部分全部原创
#Copyright (C),2025,ZhouShenyu
#======
def cnt(event=None):
    global val, filename, flag, cdx, fg, ase, ASREPR, string,breakp
    breakp=set()
    old_filename = filename
    try:
        ref = 0
        filename = directory_name.replace("/", "\\") + "\\" + lstbox.get(lstbox.curselection())
        cdxval.append(filename.replace(".\\\\", ""))
        cdx["value"] = cdxval
        cdx.set(filename.replace(".\\\\", ""))
        ASREPR = os.path.basename(filename)
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".ico"):
            from PIL import ImageTk, Image
            mg = Image.open(filename)
            ym = ImageTk.PhotoImage(mg)
            filename=old_filename
            fx = tk.Toplevel(root)
            fx.grab_set()
            fx.focus_set()
            fx.transient(root)
            fx.title("Image")
            iml = tkk.Label(fx, image=ym)
            iml.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            iml.image = ym
            return
        with open(str(filename), 'r', encoding="utf-8") as f:
            ask2 = f.readlines()
            tl=""
            for i in ask2:
                tl+=i.rstrip()
                tl+="\n"
            ask2=tl
        textPad.delete("1.0", "end")
        textPad.insert(tk.END, ask2)
        root.title(f"{os.path.abspath(filename)} - {my_title}")
    except FileNotFoundError as e:
        Messagebox.show_error(title="Regrettable Error...", message="File Not Found...")
    except UnicodeDecodeError as e:
        filename=old_filename
        Messagebox.show_warning(title="Warning", message="Can't Open This File,Open With Another Program...")
        try:
            os.startfile(directory_name + "\\" + lstbox.get(lstbox.curselection()))
        except:
            pass
    except PermissionError:
        try:
            exp(lstbox.get(lstbox.curselection()))
            filename=old_filename
        except:
            Messagebox.show_error(title="Error", message="Access Denied")
    except PIL.UnidentifiedImageError:
        pass
    except _tkinter.TclError:
        pass
    flag = 1
    upd(None)
    get__()
lstbox.bind("<Double-Button-1>", cnt)
#======

lst_pyz.pack(side="left",fill="y")
lst_pyz.configure(command=lstbox.yview)
lstbox.config(yscrollcommand=lst_pyz.set)
lstbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=0, anchor=tk.SW)
fee.pack(side=tk.LEFT, fill=tk.BOTH, anchor=tk.SW)
val = tk.StringVar()
mapf = tk.StringVar()
lb = tk.Label(root)
lb.pack(side=tk.LEFT)
for directed in os.listdir("./"):
    askrq.append(directed)
for directed in os.listdir("./"):
    ask.append(os.path.abspath(directed))
def open_direct(event=None):
    global sy, askrq, ask, askrq, directory_name
    try:
        global lstbox
        askrq = []
        ask = []
        a = askdirectory(title="Open Dir")
        directory_name = a
        if a != "":
            filels = os.listdir(a)
            sy = os.path.abspath(a)
            os.system(f"cd {sy}")
            lstbox.delete(0, tk.END)
            for i in filels:
                filep = os.path.join(a, i)
                lstbox.insert(tk.END, os.path.basename(filep))
                askrq.append(os.path.basename(filep))
                ask.append(filep)
        else:
            return
    except Exception as e:
        Messagebox.show_error(title="Error", message="OpenError: " + str(e))
# (btn1,btn2,btn3,btn22,,btnIV,btn,btn5,btn6,btn55,lb1,btn56,com)
btn1 = tkk.Button(frame, text="📄", bootstyle="outline-success", )
Tip(btn1, "New File")
btn2 = tkk.Button(frame, text="📖", bootstyle="outline-success", )
Tip(btn2, "Open File")
btn22 = tkk.Button(frame, text="📂", bootstyle="outline-success", command=open_direct, )
Tip(btn22, "Open Directory")
btn3 = tkk.Button(frame, text="💾", bootstyle="outline-success")
Tip(btn3, "Save")
from ttkbootstrap import constants
btnIV = tkk.Button(frame, text="⧉", bootstyle=f"outline-{constants.PRIMARY}")
Tip(btnIV, "Save As...")
btn4 = tkk.Button(frame, text="▶", bootstyle=f"outline-{constants.PRIMARY}")
Tip(btn4, "Run Python Code")
btn5 = tkk.Button(frame, text="🗑", bootstyle=f"outline-{constants.PRIMARY}")
Tip(btn5, "Clear Control Console")
btn6 = tkk.Button(frame, text="⏏", command=exit_, bootstyle="outline-warning")
Tip(btn6, "Exit IDEA")
btn56 = tkk.Button(frame, text="🔍", bootstyle=f"{constants.PRIMARY}-outline", command=lambda: filter_A())
Tip(btn56, "Filter Text")
btn55 = tkk.Button(frame, text="🎨", bootstyle=f"-{constants.PRIMARY}-outline",
                   command=lambda: textPad.insert(tk.INSERT, f''
                                                             f'\"{askcolor(title="Filter Color")[1]}\"'), )
Tip(btn55, "Filter Color")
btn1.pack(side=tk.LEFT, padx=2, pady=2)
btn2.pack(side=tk.LEFT, padx=2, pady=2)
btn3.pack(side=tk.LEFT, padx=2, pady=2)
btn22.pack(side=tk.LEFT, padx=2, pady=2)
btnIV.pack(side=tk.LEFT, padx=2, pady=2)
btn5.pack(side=tk.LEFT, padx=2, pady=2)
btn56.pack(side=tk.LEFT, padx=2, pady=2)
btn55.pack(side=tk.LEFT, padx=2, pady=2)
btn4.pack(side=tk.LEFT, padx=2, pady=2)
tkk.Button(frame, text="⬅", bootstyle="outline", command=__undo__).pack(side=tk.LEFT, padx=2, pady=2)
tkk.Button(frame, text="↪", bootstyle="outline", command=__redo__).pack(side=tk.LEFT, padx=2, pady=2)
btn6.pack(side=tk.LEFT, padx=2, pady=2)
tk.Label(frame, text="Tab:      ").pack(side=tk.LEFT, padx=2, pady=2)
cdx.pack(side=tk.LEFT, padx=2, pady=2, fill="both",expand=True)
frame.pack(side=tk.TOP, fill="x")
n.pack(fill=tk.BOTH, expand=True)
g = colorizer.ColorDelegator()
import re
g.prog = re.compile(r"\b(?P<MYGROUP>tkinter)\b|" + colorizer.make_pat(), re.S)
g.idprog = re.compile(r"\s+(\w+)", re.S)
g.tagdefs["COMMENT"] = {"foreground": "#787d7d"}
g.tagdefs["KEYWORD"] = {"foreground": "#cf8e6d"}
g.tagdefs["BUILTIN"] = {"foreground": "#8787b7"}
g.tagdefs["STRING"] = {"foreground": "#6aab73", }
g.tagdefs["DEFINITION"] = {"foreground": "#55a7e2"}
percolator.Percolator(textPad).insertfilter(g)
import tkinter.font as tkfont
fo = tkfont.Font(font=textPad["font"])
siz = fo.measure("   ")
textPad.config(tabs=siz)
def process(k):
    lnt, colt = textPad.index("insert").split(".");
    gcc = 0
    if k.keycode == 13:
        lst = int(lnt)
        nps = 0
        las = textPad.get(f"{lst}.0", f"{lst}.end")
        if re.search(r":\s*(#.*)?$", las):
            nps += 1
        if las.startswith("\t") or las.startswith("    "):
            i = 1
            while las.startswith("\t" * i) or las.startswith("    " * i):
                nps += 1
                i += 1
                if las.startswith("    "):
                    gcc = 1
        for i in ["continue", "return", "break", "raise","continue;", "return;", "break;", "raise;","pass","pass;"]:
            if las.replace("\t", "").replace("    ","").startswith(i):
                nps -= 1
        if gcc == 1:
            stri = "    "
        else:
            stri = "\t"
        textPad.insert(f"{int(lnt)}.{colt}", "\n" + nps * stri)
        textPad.see("end")
        upd("")
        get__()
        return "break"
textPad.bind("<Return>", process)
textPad.bind("<KeyPress>", upd)
def newfile(ev=None):
    try:
        fn=lstbox.get(lstbox.curselection())
        t=0
    except:
        fn=directory_name
        t=1
    if not  t:
        fn=directory_name+"\\"+fn
    if  not os.path.isdir(fn):
        return
    tople=tkk.Toplevel(root)
    tople.overrideredirect(True)
    tople.place_window_center()
    tk.Label(tople,text="File Name:").pack()
    tkkk=tk.Entry(tople)
    tkkk.pack()
    def new():
        with open(fn+"\\"+tkkk.get(),"w",encoding="utf-8") as hwnd:
            hwnd.write("")
            lstbox.insert(0,tkkk.get())
        tople.destroy()
    tk.Button(tople, text="New", command=new).pack()
def filter_A(event=None):
    global p
    search_val = tkk.Toplevel(root)
    search_val.grab_set()
    search_val.place_window_center()
    search_val.overrideredirect(1)
    search_val.config()
    search_val.resizable(False, False)
    search_val.title("Filter Text")
    tk.Label(search_val, text="Filter Text:     ").grid(row=1, column=0, sticky=tk.E)
    et = tkk.Entry(search_val, width=25, )
    et.grid(row=1, column=1, padx=2, pady=2, sticky="we")
    et.focus_set()
    et.insert(0, "Your Text")
    et.event_generate("<<SelectAll>>")
    value = tk.IntVar()
    a = tkk.Checkbutton(search_val, text="Ignore Case", variable=value, bootstyle="success-round-toggle")
    a.grid(row=4, column=0)
    tkk.Button(search_val, text="Begin Filter", bootstyle="success",
               command=lambda: output(et.get(), value.get(), textPad, search_val, et)).grid(row=5, column=0)
    tkk.Button(search_val, text="Close", bootstyle="warning",
               command=lambda: close()).grid(row=5, column=1)
    def close():
        textPad.tag_remove("match", "1.0", tk.END)
        search_val.destroy()
        return "break"
    tkk.Button(search_val, text="Close", bootstyle="warning",
               command=lambda: close()).grid(row=5, column=1)
    search_val.protocol("WM_DELETE_WINDOW", close)
def output(a, b, c, d, e):
    textPad.tag_remove("match", "1.0", tk.END)
    fou = 0
    if a:
        start = "1.0"
        while 1:
            start = textPad.search(a, start, nocase=b, stopindex=tk.END)
            if not start: break
            end = f"{start}+{len(a)}c"
            textPad.tag_add("match", start, end)
            fou += 1
            start = end
            textPad.tag_config("match", foreground="red", background="yellow")
            d.focus_set()
            d.title(f"{fou} matches found")
            textPad.see(end)
I = 7
upd(None)
s = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
     'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
     'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
pd.pack(fill="both", expand=True, )
y_scrl = customtkinter.CTkScrollbar(tab, orientation=tk.HORIZONTAL)
textPad.configure(xscrollcommand=y_scrl.set)
x_sc = customtkinter.CTkScrollbar(tab, orientation=tk.VERTICAL)
x_sc.configure(command=textPad.yview)
textPad.configure(yscrollcommand=x_sc.set)
x_sc.pack(fill="y", side="right")
sty.configure("Vertical.TScrollbar", gripcount=0, sliderlength=50)
y_scrl.pack(fill="x", side="bottom")
y_scrl.configure(command=textPad.xview)
line.pack(side=tk.LEFT, fill=tk.Y)
textPad.pack(fill=tk.BOTH, expand=True, side="left")
ft = "Consolas"
textPad.config(font=(ft, ii))
textPad.bind("<KeyPress>", upd)
textPad.bind("<Enter>", upd)
textPad.bind("<Leave>", upd)
root.bind("<MouseWheel>", upd)
textPad.config(width=12, height=28)
root.bind("<B1-Motion>", upd)
def funcI(event=None):
    global textPad, filename,breakp
    textPad.delete("1.0", tk.END)
    breakp=set()
    filename = ""
    root.title("[UnTitled] - Python3 Editor")
    get__()
upd(0)
def funcII(event=None):
    global textPad, filename, flag, val,breakp
    filename2 = askopenfilename(defaultextension=".py", title="Open File",
                                filetypes=[("Python Files", "*.py *.pyw *.pyi"), ("All Files", "*.*")])
    breakp=set()
    try:
        filename = filename2
        if filename2 != "":
            textPad.delete("1.0", tk.END)
            with open(filename2,"r",encoding="utf-8")as texIo:
                tmp=texIo.readlines()
                t=""
                for i in tmp:
                    t+=i.rstrip()
                    t+="\n"
                tmp=t
            textPad.insert("end", tmp)
            cdxval.append(filename2.replace("/", "\\"))
            cdx["value"] = cdxval
            cdx.set(filename2.replace("/", "\\"))
            filename = filename2
            tm = "\\"
            root.title(f"{filename2.replace('/', tm)} - {my_title}")
            flag = 1
            upd(None)
            get__()
        else:
            return
    except Exception as e:
        Messagebox.show_warning(title="Warning", message="Can\'t Open This File,Open With Another Program...")
        os.startfile(filename2)
    get__()
textPad.bind("<Key>", upd)
def funcIV(event=None):
    global filename, textPad, flag
    filename = asksaveasfilename(defaultextension=".py",
                                 filetypes=[("Python Files", "*.py *.pyw *.pyi")], title="Save As...")
    if filename != "":
        fh = open(filename, "w", encoding="utf-8", errors="ignore")
        msg = textPad.get("1.0", tk.END)
        fh.write(msg)
        fh.close()
        tfr = "\\"
        root.title(f"{filename.replace('/', tfr)} - {my_title}")
        flag = 1
        fg.append(os.path.basename(filename))
btn1["command"] = lambda: funcI()
btn2["command"] = lambda: funcII()
btn3["command"] = lambda: funcIII(None)
btnIV["command"] = lambda: funcIV(None)
frame2.pack(fill=tk.X)
def copyo():
    textMess.event_generate("<<Copy>>")
def _22(event):
    ___cj.post(event.x_root, event.y_root)
tls=customtkinter.CTkScrollbar(fr)
tls.configure(command=textMess.yview)
textMess.configure(yscrollcommand=tls.set)
tls.pack(side=tk.RIGHT,fill="y")
textMess.pack(fill="both",expand=True )
def goto(e=None):
    frav = tkk.Toplevel(root)
    frav.title("Goto")
    frav.focus_set()
    frav.overrideredirect(True)
    frav.place_window_center()
    tk.Label(frav, text="Line:").pack()
    t = tk.Entry(frav)
    t.pack()
    def go():
        mes = t.get()
        textPad.see(str(mes) + ".0")
        upd("")
        get__()
        frav.destroy()
    tk.Button(frav, text="Goto", command=go).pack()
def change_line(e):
    l = textPad.index("insert").split(".")[0]
    textPad.insert(f"{l}.end", "\n" + textPad.get(f"{l}.0", f"{l}.end"))
    upd(0)
textPad.bind("<Alt-L>", change_line)
textPad.bind("<Alt-l>", change_line)
tkk.Label(root, relief="ridge",text="Status Bar").pack(fill="both",side="left")
t = tkk.Label(root,relief="ridge" )
get__()
t2 = tkk.Label(root, text=f"{root.title()}",relief="ridge")
t.pack(fill=tk.BOTH, side="left")
t2.pack(fill=tk.BOTH, side="right")
textPad.bind("<Button-1>", get__)
textPad.bind("<KeyRelease>", get__)
___cj = tk.Menu(root, tearoff=0)
___cj.add_command(label="Copy", command=copyo, accelerator="Ctrl+C")
textMess.bind("<Control-D>", lambda event: textMess.delete("1.0", tk.END))
textMess.config(height=16)
textMess.bind("<Control-d>", lambda event: textMess.delete("1.0", tk.END))
upd("sdedfv")
def cle(e=None):
    global textMess
    textMess.config(state=tk.NORMAL)
    textMess.delete(1.0, tk.END)
    textMess.config(state=tk.DISABLED)
def mypri(txt):
    global textMess
    if textMess != None:
        textMess.insert(tk.END, txt)
        textMess.see(tk.END)
___cj.add_command(label="Clear All", command=cle, accelerator="Ctrl+D")
textMess.bind("<Control-D>", cle)
textMess.bind("<Control-d>", cle)
def mypr(txt, color="yellow"):
    global textMess
    if textMess != None:
        if color != None:
            textMess.tag_config(color, foreground=color)
        textMess.config(state="normal")
        textMess.insert(tk.END, txt, color)
        textMess.see(tk.END)
        textMess.config(state="disabled")
upd(None)
def _open_out():
    with open("Output.txt", "r+", encoding="utf-8", errors="ignore") as f:
        fra = tk.Toplevel(root)
        fra.transient(root)
        fra.grab_set()
        fra.focus_set()
        fra.title("Output")
        tt =tk.Text(fra)
        tt.insert(tk.END, f.read())
        tt.pack(fill=tk.BOTH, expand=True)
        tk.Button(fra, text="Close", command=fra.destroy).pack()
class RedirectectText:
    def __init__(self, txt_wof):
        self.txt_wof = txt_wof
    def write(self, txt):
        self.txt_wof.config(state=tk.NORMAL)
        self.txt_wof.insert(tk.END, txt)
        self.txt_wof.see(tk.END)
        self.txt_wof.config(state=tk.DISABLED)
    def flush(self):
        pass
sys.stdout = RedirectectText(textMess)
sys.stderr = RedirectectText(textMess)
def in_put2(aaaaaaa=""):
    global inp,commandinp
    inp=""
    commandinp=tk.Entry(textMess,relief="flat",borderwidth=0)
    commandinp.focus_set()
    textMess.window_create("end",window=commandinp)
    def go(e):
        global inp
        if e.keycode==13:
            inp=commandinp.get()
            commandinp.destroy()
    textMess.see("end")
    commandinp.bind("<KeyRelease>",go)
    commandinp.wait_window(commandinp)
    print(inp)
    return inp
def in_put(__prompt=""):
    if __prompt != "":
        print(__prompt, end="")
    inp = in_put2()
    return inp
ct_inp = input
input = in_put
state = " | Ready"
def run_python3_(event=None):
    global textMess, textPad, filename, state
    ret = 1
    textMess.config(state="normal")
    textMess.delete("1.0", tk.END)
    print(f"Python {sys.version}\n\nRun...\n")
    try:
        msg = textPad.get("1.0", "end")
        for i in ["import ttkbootstrap", "from tkinter", "from ttkbootstrap","import tkinter"]:
            if i in msg:
                print("This is a tkinter program,run in terminal...")
                with open("tmptm.py", "w+", encoding="utf-8") as ftk:
                    ftk.write(msg)
                os.startfile(".\\tmptm.py")
                return
        run_code = compile(msg, "<string>", "exec")
        exec(run_code)
        print("\nProcess Finished")
        root.update()
    except SyntaxError as e:
        ret = 0
        textPad.see(str(e.lineno) + '.0')
        textPad.tag_add("t", str(e.lineno) + f'.0', str(e.lineno) + f'.end', )
        textPad.tag_config("t", foreground="red", background="yellow")
        xp = e.lineno
        Messagebox.show_error(title="SyntaxError", message="SyntaxError: " + str(e))
        textPad.bind("<KeyPress>", lambda event: textPad.tag_remove("t", "1.0", tk.END))
        print("\nProcess Finished")
        return
    except Exception as e:
        ret = 0
        ref = '\''
        import traceback
        mypr(
            f'\n{str(type(e)).replace(ref, "").replace(">", "").replace("<", "").replace(" ", "").replace("class", "")}: {traceback.format_exc()}', color="#ee4e45")
        print("\n[Runtime Error]")
        print("\nProcess Finished")
        return 3
    finally:
        textMess.see(tk.END);
        textMess.config(state="disabled")
        with open("Output.txt", "a+", encoding="utf-8") as f:
            f.write(
                f"=========={time.localtime().tm_year}/{time.localtime().tm_mon}/{time.localtime().tm_mday} {time.localtime().tm_hour}:{time.localtime().tm_min}==========\n{textMess.get('1.0', tk.END)}\n")
def runpy(event=None):
    global textPad, filename, state
    textMess.config(state=tk.NORMAL)
    run_python3_()
    textMess.config(state=tk.DISABLED)
def new_dir(e=None):
    farval = tkk.Toplevel(root)
    farval.overrideredirect(True)
    farval.place_window_center()
    ev = tk.Entry(farval)
    tk.Label(farval, text="Project Path").pack()
    ev.pack(fill="x")
    def jjj():
        if not os.path.exists( ev.get()):
            os.makedirs(ev.get())
            farval.destroy()
        else:
            Messagebox.show_error(title="Error", message="Project Already Exists")
            ev.event_generate("<<SelectAll>>")
    tk.Button(farval, text="OK", command=jjj).pack()
btn4["command"] = lambda: runpy(None)
menu = tk.Menu(root, tearoff=0)
btn5["command"] = lambda: cle()
def tw_mod():
    upd("dcxvcvb")
    get__()
def copy():
    textPad.event_generate("<<Copy>>")
def cut():
    textPad.event_generate("<<Cut>>")
    upd("")
def paste():
    textPad.event_generate("<<Paste>>")
    upd("")
def undo():
    textPad.edit_undo()
    upd("")
def redo():
    textPad.edit_redo()
    upd("")
menu.add_command(label="New File", command=funcI, accelerator="Ctrl+N")
textPad.focus_set()
menu.add_command(label="Save File", command=lambda: funcIII(None), accelerator="Ctrl+S")
menu.add_command(label="Save As... File", command=lambda: funcIV(None), accelerator="Ctrl+Shift+S")
menu.add_separator()
menu.add_command(label="Open File", command=funcII, accelerator="Ctrl+O")
menu.add_command(label="Open Dir", command=open_direct, accelerator="Ctrl+Shift+O")
menu.add_command(label="New Project", command=new_dir, accelerator="Ctrl+Shift+N")
menu.add_command(label="View Output", command=_open_out, accelerator="-")
menu.add_separator()
menu.add_command(label="Exit IDEA", command=exit_, accelerator="Ctrl+Q")
root.bind("<Control-q>", exit_)
root.bind("<Control-Q>", exit_)
root.bind("<Control-n>", funcI)
root.bind("<Control-N>", funcI)
root.bind("<Control-o>", funcII)
root.bind("<Control-O>", funcII)
root.bind("<Control-Shift-S>", funcIV)
root.bind("<Control-Shift-s>", funcIV)
root.bind("<Control-S>", funcIII)
root.bind("<Control-s>", funcIII)
root.bind("<Control-Shift-O>", open_direct)
root.bind("<Control-Shift-o>", open_direct)
root.bind("<Control-Shift-N>", new_dir)
root.bind("<Control-Shift-n>", new_dir)
mai = tkk.Menu(master=root)
root.config(menu=mai)
mai.add_cascade(label="File", menu=menu)
menu2 = tk.Menu(root, tearoff=0)
def select_all():
    textPad.event_generate("<<SelectAll>>")
menu2.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
menu2.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
menu2.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
menu2.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
menu2.add_separator()
menu2.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
menu2.add_command(label="Redo", command=redo, accelerator="Ctrl+Y")
menu2.add_command(label="Copy Line", command=lambda: change_line(0), accelerator="Alt+L")
menu2.add_command(label="Goto...", command=lambda: goto(), accelerator="Ctrl+G")
menu2.add_separator()
menu2.add_command(label="Filter Color", command=lambda: fun(None), accelerator="Ctrl+/")
menu2.add_command(label="Filter Text", command=lambda: filter_A(None), accelerator="Ctrl+F")
menu2.add_separator()
menu2.add_command(label="Replace All",command=repl_all,accelerator="Ctrl+R")
mai.add_cascade(label="Edit", menu=menu2)
maint = tk.Menu(mai)
maint.add_command(label="Run", command=lambda: runpy(), accelerator="F5")
def rt():
    with open(f"rungcvxfcfvffd.py", "w+", encoding="utf-8") as f:
        f.write(textPad.get("1.0", "end"))
    os.startfile("rungcvxfcfvffd.py")
maint.add_command(label="Run In Terminal", command=lambda: rt())
mai.add_cascade(label="Run", menu=maint)
arg = tk.Menu()
textPad.bind("<Control-g>", goto)
textPad.bind("<Control-G>", goto)
g = tk.BooleanVar()
g.set(0)
def toogle(e=""):
    if g.get():
        root.attributes("-topmost", True)
        root.geometry("1555x606")
    else:
        root.attributes("-topmost", False)
        root.geometry("2290x1147")
arg.add_cascade(label="Min size     ", command=root.iconify, accelerator="_")
arg.add_checkbutton(label="Top", variable=g, command=toogle)
ii = 10
def zoom_up():
    global ii, ftn
    ii += 1
    textPad.config(font=(ft, ii))
    ftn += 2
    tw_mod()
    root.geometry(f"2290x{ftn}")
def zoom_dn():
    global ii, ftn
    ii -= 1
    textPad.config(font=(ft, ii))
    ftn -= 2
    tw_mod()
    root.geometry(f"2290x{ftn}")
def __add__(event):
    try:
        with open(cdx.get(), "r", encoding="utf-8") as file:
            textPad.delete('1.0', "end")
            textPad.insert("end", file.read())
            root.title(cdx.get())
    except:
        pass
    get__()
    upd(0xff000a0dF0CFAB)
cdx.bind("<<ComboboxSelected>>", __add__)
def winls():
    import pygetwindow
    wind = pygetwindow.getAllTitles()
    pye_dv_lst = []
    topl = tkk.Toplevel(root)
    topl.place_window_center()
    topl.title("Window List")
    topl.geometry("1000x350")
    lstb = tk.Listbox(topl)
    lstb.pack(fill="both", expand=True)
    ij = 1
    for i in wind:
        if "Python3 Editor" in i:
            pye_dv_lst.append(i)
            lstb.insert("end", "#" + str(ij) + "                                                       " + i)
            ij += 1
arg.add_command(label="Window List", command=winls)
men = tk.Menu()
def __i(event=None):
    help_docs="""QuickStart
1 FILE MENU->NEW FILE
2 Edit your file
3 FILE MENU->SAVE FILE
Move Forward
You can click line number to add breakpoint and press \"🐞\" to debug.
"""
    Messagebox.show_info(title="Help",
    message=help_docs)
menus = tk.Menu(men)
menus.add_command(label="Default", command=to_l)
menus.add_command(label="Dark", command=to_dark)
menus.add_command(label="Light", command=to_light)
menus.add_command(label="Superhero", command=to_blue)
men.add_cascade(label="Themes", menu=menus)
men.add_command(label="Zoom+", command=zoom_up)
men.add_command(label="Zoom-", command=zoom_dn)
mai.add_cascade(label="View", menu=men)
mai.add_cascade(menu=arg, label="Window")
def fun(event):
    textPad.insert(tk.INSERT, f'\"{askcolor(title="Filter Color")[1]}\"')
men = tk.Menu()
menus = tk.Menu(men)
menus.add_command(label="Default", command=to_l)
menus.add_command(label="Dark", command=to_dark)
menus.add_command(label="Light", command=to_light)
menus.add_command(label="Superhero", command=to_blue)
aaaa = """#!usr/bin/env python3
#-*- coding:utf-8 -*-
"""
def ai_assimp():
    textPad.insert("1.0", aaaa)
    get__()
    upd("")
mai1 = tk.Menu(root, tearoff=0)
def __(event):
    msg = """
Python3 Editor About\n    ————————————
Version:0.0.1-π
╔═══╗╔╗╔╗╔════╗╔╗╔╗╔══╗╔╗─╔╗
║╔═╗║║║║║╚═╗╔═╝║║║║║╔╗║║╚═╝║
║╚═╝║║╚╝║──║║──║╚╝║║║║║║╔╗─║
║╔══╝╚═╗║──║║──║╔╗║║║║║║║╚╗║
║║────╔╝║──║║──║║║║║╚╝║║║─║║
╚╝────╚═╝──╚╝──╚╝╚╝╚══╝╚╝─╚╝
MIT LICENSE:
Copyright (c) 2025 Zhoushenyu Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
"""
    val = tk.Toplevel(root)
    val.transient(root)
    val.focus_set()
    val.geometry("800x267")
    val.grab_set()
    val.title("About")
    def destory():
        val.destroy()
    r = tk.Text(val, font="楷体", height=8)
    r.pack(fill=tk.BOTH, expand=1)
    r.insert(tk.INSERT, msg)
    r["state"]="d"
    tk.Button(val, text="Close", command=destory).pack()
mai1.add_command(label="About", command=lambda: __(" s"))
mai1.add_command(label="Help", accelerator="F1",
                 command=__i)
mai1.add_command(label="Python Docs", command=lambda: webbrowser.open("https://docs.python.org/"))
root.bind("<Control-/>", fun)
root.bind("<Control-f>", filter_A)
root.bind("<Control-F>", filter_A)
mai.add_cascade(label="Help", menu=mai1)
root.bind("<F5>", runpy)
root.bind("<Control-s>", funcIII)
root.bind("<Control-S>", funcIII)
___ = tk.Menu(root, tearoff=0)
___.add_command(label="Run", command=runpy, accelerator="F5")
___.add_separator()
___.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
___.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
___.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
___.add_separator()
___.add_command(label="Undo", command=undo, accelerator="Ctrl+Z")
___.add_command(label="Redo", command=redo, accelerator="Ctrl+Y")
___.add_separator()
___.add_command(label="Comment Header", command=ai_assimp, )
___.add_command(label="Add Comment", command=comment, )
def _(event):
    ___.post(event.x_root, event.y_root)
o = tk.Menu(lstbox, tearoff=0)
o.add_command(label="Open", command=cnt, accelerator="Alt+O")
o.add_command(label="New", command=newfile, accelerator="Alt+N")
lstbox.bind("<Alt-N>",newfile)
lstbox.bind("<Alt-n>",newfile)
def _0_(event=None):
    global lstbox, fg, cdx, textPad
    try:
        if Messagebox.show_question(title="Remove" + "\"" + directory_name.replace("/", "\\").replace(".\\","") + "\\" + lstbox.get(
                lstbox.curselection()) + "\"",
                               message="Do You Want Remove" + "\"" + directory_name.replace("/", "\\").replace(".\\","") + "\\" + lstbox.get(
                                   lstbox.curselection()) + "\"?",buttons=("Yes,I do","No,I don\'t"))=="Yes,I do":
            os.remove(directory_name + "\\" + lstbox.get(lstbox.curselection()))
            root.title(my_title)
            itr = lstbox.curselection()
            index32=0
            for ind in lstbox.get(0,"end"):
                if lstbox.get(0,"end")[index32]==itr:
                    try:
                        lstbox.delete(index32)
                    except Exception as e:print(e)
                index32+=1
    except:
        pass
o.add_command(label="Remove", command=_0_, accelerator="Delete")
lstbox.bind("<Delete>", _0_)
textPad.focus_set()
lstbox.bind("<Alt-O>", cnt)
lstbox.bind("<Alt-o>", cnt)
def _2(event):
    o.post(event.x_root, event.y_root)
textPad.bind("<Button-3>", _)
lstbox.bind("<Button-3>", _2)
root.bind("<F1>", __i)
root.bind("<Key>", upd)
root.bind("<Button>", upd)
textMess.bind("<Button-3>", _22)
textPad.bind("<KeyPress>", get__)
textPad.bind("<MouseWheel>", get__)
textPad.bind("<B1-Motion>", get__)
textPad.bind("<KeyRelease>", get__)
def ru():
    global debug
    try:
        with open("___DEBUG_TMP__.py","r",encoding="utf-8")as textio:
            cd=textio.read()
        dbc=compile(cd,"___DEBUG_TMP__.py","exec")
        debug.run(dbc)
        sto_db()
    except Exception as e:
        print(e)
    finally:
        sto_db()
        return
def start_db():
    try:
        global debug,isdebug
        if isdebug:
            return
        code=textPad.get(1.0,"end")
        with open ("___DEBUG_TMP__.py","w",encoding="utf-8") as texio:
            texio.write(textPad.get("1.0","end"))
        debug=EditorDB()
        for bp in breakp:
            debug.set_break("___DEBUG_TMP__.py",bp)
        print("[EDB]:Starting...")
        isdebug=True
        import threading
        db_t=threading.Thread(target=ru)
        db_t.daemon=True
        db_t.start()
    except Exception as e:pass
    finally:return
def stp_over():
    global debug
    if debug and isdebug:
        debug.set_next(curr_frame)
        debug.set_continue()
def stp_into():
    global debug
    if debug and isdebug:
        debug.set_step()
        debug.set_continue()
def st():
    global debug
    if debug and isdebug:
        debug.set_return(curr_frame)
        debug.set_continue()
def ct_db():
    global debug
    if debug and isdebug:
        debug.set_continue()
def kk(eb):
    textPad.insert(tk.INSERT, "\"")
    pyautogui.press("left");
def ksk(eb):
    textPad.insert(tk.INSERT, "\'")
    pyautogui.press("left");
root.bind("<\">", kk)
root.bind("<\'>", ksk)#
def highlight_current_line(lineno):
    textPad.tag_remove("curr","1.0","end")
    textPad.tag_add("curr",f"{lineno}.0",f"{lineno}.end+1c")
    textPad.tag_config("curr",underline=True,underlinefg="red")
    textPad.see(f"{lineno}.0")
db_frame=ttk.Frame(frame2)
db_frame.pack(fill="both", expand=True)
db_frame2=tk.LabelFrame(db_frame,text="Control")
db_frame2.pack(side="left",padx=3)
tkk.Button(db_frame2,text="🐞",bootstyle="outline",command=start_db).pack(pady=2)
tkk.Button(db_frame2,text="→",command=stp_over,bootstyle="outline",).pack(pady=2)
tkk.Button(db_frame2,text="↓",command=stp_into,bootstyle="outline",).pack(pady=2)
tkk.Button(db_frame2,text="⬆",command=st,bootstyle="outline",).pack(pady=2)
tkk.Button(db_frame2,text="▶",command=ct_db,bootstyle="outline",).pack(pady=2)
tkk.Button(db_frame2,text="⏸",command=sto_db,bootstyle="outline",).pack(pady=2)
var_tree=tkk.Treeview(db_frame,columns=("Value","Type"),show="headings")
var_tree.heading("#0",text="Name")
var_tree.heading("Value",text="Value")
var_tree.heading("Type",text="Type")
var_tree.column("#0",width=150)
var_tree.column("Value",width=200)
var_tree.column("Type",width=100)
var_tree.pack(side="left",fill="both",expand=True)
stack_=tk.LabelFrame(db_frame,text="Call Stack")
frame2.add(db_frame,text="Debug")
stack_.pack(side="left",fill="x",expand=True)
stack=tk.Listbox(stack_)
stack.pack(fill="x",expand=True)
root.protocol("WM_DELETE_WINDOW", exit_)
def update_vari(frx):
    for it in var_tree.get_children():
        var_tree.delete(it)
    local=frx.f_locals
    globals=frx.f_globals
    for n,v in local.items():
        try:
            value=str(v)
            ty=type(v).__name__
            if len(value)>50:
                value=value[:50]+"..."
            var_tree.insert("", "end", text=n, values=(value, ty))
        except:pass
    for n,v in globals.items():
        if n not in local and not n.startswith("_"):
            try:
                vs=str(v)
                t=type(v).__name__
                if len(vs)>50:
                    vs=vs[:50]+"..."
                var_tree.insert("","end",text=n,values=(vs,t))
            except:pass
def update_stack_viewer(Fr):
    frame=Fr
    stack.delete(0,"end")
    depth=0
    db_stack.clear()
    while frame:
        func=frame.f_code.co_name
        lineno=frame.f_lineno
        stack.insert(0,f"{func}(line:{lineno})")
        db_stack.insert(0,frame)
        frame=frame.f_back
        depth+=1
        if depth>20:
            break
lbs.pack(fill="both",expand=1)
frame2.add(lbs,text="Structure")
#=====================
root.mainloop()
#TOTAL 1586 LINES
#MADE IN CHINA,FREE,2025
#感谢CSDN&DeepSeek以及所有中国开发博客的贡献

