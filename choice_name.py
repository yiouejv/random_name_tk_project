import random
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
names = []  # 全局变量保存学生名单
flag = True  # 标记提示框是否被关闭, 默认没有弹出提示框为True

def read_file():
    '''读取文件，初始化学生名单'''
    try:
        fname = tk.filedialog.askopenfilename()
        with open(fname, 'r', encoding='utf-8') as rf:
            s = rf.read()
        s.strip()  # 去掉左右空格
        global names
        names = s.split('\n')  # 把每个名字存入列表
        names = [name.strip()[:-1] for name in names]  # 把名字里的空格去掉生成新的列表
        names = list(filter(lambda name: name != '', names))
        print(names)
        tkinter.messagebox.showinfo('提示', '名单导入成功')
    except:
        pass


def tip_destroy(tip):
    global flag
    flag = True
    tip.destroy()


def tip_window():
    global flag
    if flag:  # 如果上一个提示框被关闭才允许生成
        print('tip_window flag=', flag)
        tip_window = tk.Tk()
        tip_window.geometry('180x100')
        lbl = tk.Label(tip_window, text='请该同学上台', width=10, height=3).pack()
        btn = tk.Button(tip_window, text='确定', width=6, height=1,
                        command=lambda : tip_destroy(tip_window)).place(x = 100, y = 60)
        flag = False
        return tip_window


def choice_name(var):
    '''随机选择一个名字, 然后把选过的名字删除'''
    global flag
    if flag:  # 如果关闭了上一个窗口才允许再次抽名字
        global names
        if len(names) == 0:
            tkinter.messagebox.showinfo('提示', '所以的学生都上来过了')
        else:
            name = random.choice(names)
            names.remove(name)
            var.set(name)
            # 弹出提示框
            print('choice_name flag =', flag)
            tip = tip_window()
            # flag = False  # 打开了一个提示框，flag = False
            tip.mainloop()
    else:
        return


def ui():
    window = tk.Tk()

    window.title('随机点名程序')
    window.geometry('800x380')
    window.maxsize(800, 380)

    btn = tk.Button(window, text='导入名单', width=10, height=2, font=('Arial', 15), command=read_file)
    btn.pack(side='left', anchor='n', padx=10, pady=10)

    var = tk.StringVar()
    lbl = tk.Label(window, textvariable=var, bg='yellow', font=('Arial', 42), width=15, height=2)
    lbl.pack(anchor='center', padx=5, pady=80)

    btn_choice = tk.Button(window, text='点名', width=15, height=6, font=('Arial', 15), command=lambda : choice_name(var))
    btn_choice.pack(side='right', anchor='n', padx=10, pady=10)
    return window


if __name__ == '__main__':
    window = ui()
    window.mainloop()
