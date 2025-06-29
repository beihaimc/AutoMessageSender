# 💬 AutoMessageSender

This is a GUI-based auto message sender developed by **Beihai**, written in Python.  
It uses `tkinter` for the user interface, combined with `pyautogui` and `pyperclip` to automate copying, pasting, and sending messages.  
It supports custom messages, hotkeys, a random number mode, right-click controls, and more.

---

## 🛠 Features

- Customize message content
- Adjustable message interval (in seconds)
- One-click start/stop
- Supports any characters: Chinese, English, symbols, etc.
- Set number of messages and delay time
- Multiple keyboard shortcuts
- Right-click menu to stop sending
- Error & overflow warnings
- Can be packaged as `.exe` (no need for Python environment)
- Built-in usage disclaimer 🚫

---

## 🔧 Tech Stack

- Python 3.11 (or your version)
- `tkinter` – GUI
- `pyautogui` – automatic keyboard control
- `pyperclip` – clipboard operations
- `pyinstaller` – packaging to EXE (optional)

---

## 🛠️ How It Works

The program automates message sending using the following process:

1. The user enters the message in the input box  
2. On clicking the Start button (or using a shortcut), the program:
   - Copies the message using `pyperclip.copy()`
   - Pastes it into the focused window using `pyautogui.hotkey('ctrl', 'v')`
   - Sends it by simulating an Enter key press with `pyautogui.press('enter')`
3. If multiple sends are set, the above steps repeat with a delay between each message

This method is faster and more stable than `typewrite()` and is suitable for text box automation.

---

## ⌨️ Default Shortcuts

| Shortcut       | Action                      |
|----------------|-----------------------------|
| Ctrl + S       | Start sending               |
| Ctrl + E       | Stop sending                |
| Ctrl + R       | Toggle random number mode   |
| Ctrl + F       | Focus on input field        |
| Ctrl + H       | Clear message input         |
| Ctrl + A       | Select all text             |
| Ctrl + Q / W   | Exit or close window        |

---

## 🚀 How to Use

### 🧩 Method 1: Download `.exe` (no setup required)

👉 [Click here to download the release](https://github.com/minecraftbeihai/AutoMessageSender/releases/tag/message)

---

### 🧰 Method 2: Run the source code

1. Install dependencies:
   ```bash
   pip install pyautogui pyperclip

2. Run the script:

python main.py


3. Make sure the program window stays on top, then switch to your target chat window.




---

⚠️ Legal & Ethical Disclaimer (MUST READ)

This program is for educational, testing, and research purposes only.
Any form of misuse—such as spamming, harassment, fraud, or disrupting public order—is strictly prohibited.

This tool simulates keyboard input and may interfere with real-world environments.
Please use it only in private testing environments or with explicit permission.

The developer is not responsible for any misuse or consequences arising from this tool.
Users are solely responsible for all actions performed using this program.


> ❗ A sincere reminder: Technology has no inherent morality—
it's the user who must act with responsibility and conscience.
