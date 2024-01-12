import pyautogui
import time

long_code = """
import time\n
time_=time.ctime()\n
print(f"time :{time_}")\n
    
"""


pyautogui.write(long_code, interval=0.1) 


time.sleep(1)
