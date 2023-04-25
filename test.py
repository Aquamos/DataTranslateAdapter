import subprocess
import pyautogui
import pyperclip
import time
import re


manga_name_prefix = "English name of rus manga"
program_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
program_name = "msedge.exe"
args = [program_path, "/maximize"]


def get_manga_name(name):
    process = subprocess.Popen(args)
    process.wait()

    # Maximize window
    time.sleep(0.5)
    pyautogui.hotkey('win', 'up')

    # Type in the search query
    time.sleep(0.5)
    pyperclip.copy(f"{manga_name_prefix} {name}")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.hotkey('enter')

    # Wait for the search results to load
    time.sleep(3)

    # Navigate to the bing chat result
    special_position = pyautogui.locateCenterOnScreen('bing_chat_icon.png', confidence=.65)
    x,y = special_position
    y += 44
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(20)

    # Copy the text from the chat
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    copied_text = pyperclip.paste()
    match = re.search(r'[ia]s\s+“?([^”]*)”?', copied_text)

    # Close window
    pyautogui.hotkey('ctrl', 'w')

    return match.group(1)


'''
# Check if the program is still running
if process.poll() is None:
    print(f"{program_name} is still running.")
else:
    print(f"{program_name} has exited.")
'''

