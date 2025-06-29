<p align="center">
🌐 Language | 语言切换: [🇨🇳 中文](#简易自动信息发送器auto-message-sender) | [🇺🇸 English](#automessagesender)
</p>

---

<details open>
<summary>🇨🇳 中文说明</summary>

# 简易自动信息发送器（AutoMessageSender）

这是一个由北海制作的带 GUI 的自动信息发送工具，基于 Python 编写，使用 `tkinter` 构建界面，配合 `pyautogui` + `pyperclip` 实现消息的自动复制粘贴与发送。支持快捷键、随机数模式与右键控制等多种功能。

---

## 🛠 功能介绍

- 自定义发送内容  
- 设置发送间隔（单位：秒）  
- 一键启动/停止  
- 支持中文、英文、符号等任意字符  
- 可选等待时间与发送次数  
- 多种快捷键绑定  
- 右键菜单控制  
- 错误与超限提醒  
- 打包为 `.exe` 文件，免Python环境运行  
- 自带温馨声明 🚫骚扰用途  

---

## 🔧 技术栈

- Python 3.11（或你使用的版本）  
- `tkinter` 图形界面  
- `pyautogui` 实现自动输入  
- `pyperclip` 实现复制粘贴  
- `pyinstaller` 打包成 EXE（可选）

---

## 🛠️ 运行原理

本程序通过以下流程自动化发送信息：

1. 用户在输入框中填写要发送的消息  
2. 点击开始按钮（或使用快捷键），程序会执行：
   - 使用 `pyperclip.copy()` 将消息复制到剪贴板  
   - 使用 `pyautogui.hotkey('ctrl', 'v')` 粘贴消息到当前窗口  
   - 使用 `pyautogui.press('enter')` 模拟按下回车，发送消息  
3. 如果设置多次发送，程序将按设定次数循环发送（每条之间可设置间隔）

这种方式比 `typewrite()` 更稳定快速，适合用于聊天窗口自动化处理。

---

## ⌨️ 快捷键一览（默认）

| 快捷键        | 功能             |
|--------------|------------------|
| Ctrl + S     | 开始发送         |
| Ctrl + E     | 停止发送         |
| Ctrl + R     | 切换随机数模式   |
| Ctrl + F     | 聚焦输入框       |
| Ctrl + H     | 清空输入框       |
| Ctrl + A     | 全选内容         |
| Ctrl + Q/W   | 退出或关闭窗口   |

---

## 🚀 如何运行？

### 🧩 方法一：直接下载 `.exe` 文件（免安装）

👉 [点击这里下载 Release](https://github.com/minecraftbeihai/AutoMessageSender/releases/tag/message)

---

### 🧰 方法二：运行源代码

1. 安装依赖：

```bash
pip install pyautogui pyperclip

2. 运行主程序：



python main.py

3. 保证窗口置顶，并将焦点切换到聊天框等目标区域。




---

⚠️ 法律与道德声明（必读！）

本程序仅供学习、测试和技术研究使用，禁止用于任何形式的骚扰、刷屏、诈骗、扰乱公共秩序等非法用途！

本工具模拟键盘操作，可能会干扰正常使用环境，请在私人测试环境或明确许可的前提下使用。

开发者不对任何滥用行为负责，使用者需自行承担由使用本程序带来的全部后果。


> ❗郑重提醒：技术没有善恶，但使用它的人必须有边界和良知。



</details>
---

<details>
<summary>🇺🇸 English Docs</summary>AutoMessageSender

This is a GUI-based auto message sender developed by Beihai, written in Python.
It uses tkinter for the UI, combined with pyautogui and pyperclip to automate copying, pasting, and sending messages.
Supports custom messages, random number mode, hotkeys, right-click menu, and more.


---

🛠 Features

Customize message content

Adjustable message interval (in seconds)

One-click start/stop

Supports all characters: Chinese, English, symbols

Optional delay and send count

Multiple keyboard shortcuts

Right-click menu support

Error & overflow alerts

Can be packaged as .exe

Built-in warning: 🚫 Not for harassment



---

🔧 Tech Stack

Python 3.11 (or your version)

tkinter – GUI

pyautogui – auto typing & hotkeys

pyperclip – clipboard handling

pyinstaller – EXE packaging



---

🛠️ How It Works

The program works as follows:

1. User inputs message in the text box


2. On pressing Start or a shortcut:

The message is copied via pyperclip.copy()

It is pasted into the focused window via pyautogui.hotkey('ctrl', 'v')

The Enter key is simulated using pyautogui.press('enter')



3. The steps repeat based on message count & interval



This is more stable and faster than typewrite() for most UI inputs.


---

⌨️ Default Shortcuts

Shortcut	Function

Ctrl + S	Start sending
Ctrl + E	Stop sending
Ctrl + R	Toggle random number
Ctrl + F	Focus input field
Ctrl + H	Clear input
Ctrl + A	Select all
Ctrl + Q/W	Quit / close window



---

🚀 How to Use

🧩 Method 1: Download .exe (no setup required)

👉 Click here to download Release


---

🧰 Method 2: Run the source code

1. Install dependencies:



pip install pyautogui pyperclip

2. Run the script:



python main.py

3. Make sure the program window stays on top and target chat window is focused.




---

⚠️ Legal & Ethical Notice

This program is for educational, testing, and research use only.
Any misuse—such as harassment, spamming, scamming, or disruption—is strictly forbidden.

It simulates keyboard behavior, which may interfere with real usage. Only use it in test environments or with clear permission.

The developer is not responsible for any misuse or consequences. Users assume full responsibility.


> ❗Reminder: Technology itself is neutral. The user must act with responsibility and boundaries.



</details>
```
---
