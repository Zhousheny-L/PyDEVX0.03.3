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

一个功能 __较为__ 丰富的 PYTHON IDEA

>![Alt text](rrrr.ico)

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
    #基于关键字和库的代码补全
    pass

#状态&高亮
def get__(e=None):
    #语法高亮升级和更新结构、状态栏和高亮当前行
    pass
```
---

**许可证**
---
>__遵循[MIT](https://www.mit-license.org/)许可证 ，见LICENSE.md__
