import pyautogui
import pyperclip
import time

# Step 1: Click on the icon at (704, 751)
pyautogui.moveTo(704, 751, duration=0.5)
pyautogui.click()

# Give it time to open WhatsApp or load
time.sleep(2)

# Step 2: Drag from (492, 159) to (1333, 642)
pyautogui.moveTo(492, 159, duration=0.5)
pyautogui.mouseDown()
pyautogui.moveTo(1333, 642, duration=0.5)
pyautogui.mouseUp()

# Step 3: Copy selected text to clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Allow time for clipboard update

# Step 4: Get clipboard content
copied_text = pyperclip.paste()

print("Copied text from WhatsApp:")
print(copied_text)
