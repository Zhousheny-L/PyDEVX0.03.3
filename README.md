Python3 Editor README
=
---
**目录**
---
1.[简介](#简介)\
2.[依赖](#依赖)\
3.[关键部分实现](#关键部分实现)\
4.[许可证](#许可证)

---
**简介**
--- 
一个功能 __较为__ 丰富的 PYTHON IDEA\
有许多功能,如下

| 文件     | __代码__  | 编辑    |
|:-------|:--------|:------| 
| 新建     | 补全      | 复制    | 
| 打开     | 高亮      | 剪切    |
| 保存     | 行号      | 粘贴    |
| 文件夹... | __状态栏__ | 撤销/恢复 |
| ...    | ...     | ...   |
---
依赖
---
>键入并运行命令 ```pip install pyautogui pillow customtkinter ttkbootstrap pygetwindow```
---
**关键部分实现**
---
```python
#代码补全
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

#状态&高亮
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
```
---

**许可证**
---
>__遵循[MIT](https://opensource.org/license/mit/)许可证 ，见LICENSE.md__
