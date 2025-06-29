import time
import random
import pyautogui
import pyperclip
import tkinter as tk
from tkinter import messagebox, ttk
is_stopping = False  # 添加一个全局变量来控制停止状态
def simulate_user_input(message):
    # 确保目标窗口已聚焦
    pyautogui.click()  # 单击确保聚焦到目标窗口
    pyperclip.copy(message)  # 将消息复制到剪贴板
    pyautogui.hotkey('ctrl', 'v')  # 粘贴消息
    pyautogui.press('enter')  # 按回车键发送
def send_message(message, count, use_random):

    """发送消息的函数"""
    global is_stopping
    for _ in range(count):
        if is_stopping:
            break
        if use_random:
            message = str(random.randint(1, 100))  # 生成 1 到 100 的随机数
        simulate_user_input(message)
def stop_sending():
    """停止发送消息的函数"""
    global is_stopping
    if messagebox.askyesno("确认", "您确定要停止发送消息吗？"):
        is_stopping = True  # 设置停止状态

def start_sending():
    """开始发送消息的函数"""
    global is_stopping
    is_stopping = False
    message = message_entry.get().strip()  # 获取并去除前后空格
    count_str = count_entry.get().strip()
    wait_str = wait_entry.get().strip()
    use_random = random_var.get()  # 获取复选框的值

    # 输入验证
    if not message and not use_random:
        show_error_box("您未输入有效信息或未选择随机数")
        return
    if not count_str.isdigit() or int(count_str) <= 0:
        show_error_box("请输入有效的发送次数")
        return
    if not wait_str.replace('.', '', 1).isdigit() or float(wait_str) < 0:
        show_error_box("请输入有效的等待时间")
        return

    count = int(count_str)
    time_wait = float(wait_str)

    # 警告提示
    if time_wait > 60 and not show_warning_box("您输入的等待时间超过 60 秒"):
        return
    if count > 1000 and not show_warning_box("您输入的发送次数超过 1000 次"):
        return

    label.config(text="准备发送消息...")
    root.after(100, lambda: message_wait_print(time_wait, label))

    start_time = time.time()
    root.after(int(time_wait * 1000) + 100, lambda: send_message(message, count, use_random))
    root.after(int(time_wait * 1000) + 100 + 1000 * count, lambda: show_time(start_time, count))

def message_wait_print(time_wait, label):
    """在 GUI 中更新等待信息"""
    if is_stopping:
        label.config(text="发送已停止")
        return
    if time_wait > 0:
        label.config(text=f"还有 {int(time_wait)} 秒发送信息")
        root.after(1000, lambda: message_wait_print(time_wait - 1, label))
    else:
        label.config(text="开始发送消息...")

def show_error_box(message):
    """显示错误提示框"""
    messagebox.showerror("错误", message)

def show_warning_box(message):
    """显示警告提示框"""
    return messagebox.askyesno("警告", message + "\n是否继续？")

def show_time(start_time, count):
    """显示发送用时的函数"""
    end_time = time.time()
    elapsed_time = end_time - start_time
    messagebox.showinfo("完成", f"消息发送完毕！\n发送次数: {count}\n用时: {elapsed_time:.2f} 秒")

# 创建主窗口

root = tk.Tk()
root.title("北海信息轰炸程序")
root.geometry("400x600")  # 调整窗口大小
root.attributes('-topmost', True)
root.resizable(False, False)  # 禁止调整窗口大小
root.protocol("WM_DELETE_WINDOW", lambda: root.quit())  # 关闭窗口时退出程序
# 右键菜单
right_click_menu = tk.Menu(root, tearoff=0)  # 创建右键菜单
right_click_menu.add_command(label="停止发送", command=stop_sending)  # 添加菜单项
root.bind('<Button-3>', lambda e: right_click_menu.post(e.x_root, e.y_root))  # 绑定右键菜单

# 右键菜单
right_click_menu = tk.Menu(root, tearoff=0)  # 创建右键菜单
right_click_menu.add_command(label="停止发送", command=stop_sending)  # 添加菜单项
root.bind('<Button-3>', lambda e: right_click_menu.post(e.x_root, e.y_root))  # 绑定右键菜单

# 绑定回车键发送消息
root.bind('<Return>', lambda e: start_sending())

# 修正快捷键绑定问题
# 绑定 Ctrl + C 复制
root.bind('<Control-c>', lambda e: pyperclip.copy(message_entry.get().strip()))
# 绑定 Ctrl + V 粘贴
root.bind('<Control-v>', lambda e: pyautogui.hotkey('ctrl', 'v'))
# 绑定 Ctrl + X 剪切
root.bind('<Control-x>', lambda e: message_entry.event_generate("<<Cut>>"))

# 绑定 Ctrl + A 全选输入框
root.bind('<Control-a>', lambda e: message_entry.select_range(0, 'end'))
# 绑定 Ctrl + Z 撤销输入
root.bind('<Control-z>', lambda e: message_entry.event_generate("<<Undo>>"))
# 绑定 Ctrl + Y 重做输入
root.bind('<Control-y>', lambda e: message_entry.event_generate("<<Redo>>"))
# 绑定 Ctrl + F 聚焦输入框
root.bind('<Control-f>', lambda e: message_entry.focus_set())
# 绑定 Ctrl + H 清空输入框
root.bind('<Control-h>', lambda e: message_entry.delete(0, 'end'))
# 绑定 Ctrl + S 开始发送
root.bind('<Control-s>', lambda e: start_sending())
# 绑定 Ctrl + E 停止发送
root.bind('<Control-e>', lambda e: stop_sending())
# 绑定 Ctrl + R 切换随机数
root.bind('<Control-r>', lambda e: random_var.set(not random_var.get()))
# 绑定 Ctrl + Q 退出程序
root.bind('<Control-q>', lambda e: root.quit())
# 绑定 Ctrl + W 关闭窗口
root.bind('<Control-w>', lambda e: root.destroy())
# 绑定 Ctrl + P 粘贴
root.bind('<Control-p>', lambda e: pyautogui.hotkey('ctrl', 'v'))
# 绑定 Ctrl + B 剪切
root.bind('<Control-b>', lambda e: message_entry.event_generate("<<Cut>>"))
# 绑定 Ctrl + D 删除
root.bind('<Control-d>', lambda e: message_entry.event_generate("<<Clear>>"))
# 绑定 Ctrl + N 选中下一个字符
root.bind('<Control-n>', lambda e: message_entry.event_generate("<<SelectNextChar>>"))
# 绑定 Ctrl + M 选中下一行
root.bind('<Control-m>', lambda e: message_entry.event_generate("<<SelectNextLine>>"))
# 绑定 Ctrl + U 撤销
root.bind('<Control-u>', lambda e: message_entry.event_generate("<<Undo>>"))
# 绑定 Ctrl + T 交换字符
root.bind('<Control-t>', lambda e: message_entry.event_generate("<<TransposeChars>>"))

# 设置全局样式
style = ttk.Style()
style.configure('TLabel', font=('SimSun', 10))  # 使用宋体
style.configure('TEntry', font=('SimSun', 10), borderwidth=2, relief="groove")
style.configure('TButton', font=('SimSun', 10), padding=5)

# 创建框架
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)
# 创建输入框和标签
tk.Label(frame, text="请输入信息内容:").pack(anchor='w', pady=5)
message_entry = ttk.Entry(frame, width=40,font='simpsun')
message_entry.pack(pady=5)

tk.Label(frame, text="请输入发送次数:").pack(anchor='w', pady=5)
count_entry = ttk.Entry(frame, width=40,font='simpsun')
count_entry.pack(pady=5)

tk.Label(frame, text="请输入等待时间(秒):").pack(anchor='w', pady=5)
wait_entry = ttk.Entry(frame, width=40,font='simpsun')
wait_entry.pack(pady=5)

# 创建复选框
random_var = tk.BooleanVar()
random_checkbox = ttk.Checkbutton(frame, text="使用随机数", variable=random_var)
random_checkbox.pack(anchor='w', pady=5)

# 创建开始按钮
start_button = ttk.Button(frame, text="开始发送", command=start_sending)
start_button.pack(anchor='e', pady=20)

# 创建停止按钮
stop_button = ttk.Button(frame, text="停止发送", command=stop_sending)
stop_button.pack(anchor='e', pady=5)

# 创建状态标签
label = ttk.Label(frame, text="")
label.pack(pady=10)

# 创建底部标签
# 创建底部标签
footer_label = ttk.Label(
    root,
    text="本程序由北海制作，请勿用于骚扰等非法用途，本程序仅供学习使用，与开发者无关",
    wraplength=320,
    justify='center',
    foreground='gray',  # 修改此行
    font=('SimSun', 8)
)
footer_label.pack(side='bottom', pady=10)

footer_label.pack(side='bottom', pady=10)

# 运行主循环
root.mainloop()