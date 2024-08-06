import pyautogui as gui
import subprocess
import time

def open_App(text):
    try:
        # Try to open the application using subprocess
        subprocess.run(text, shell=True, check=True)
    except Exception as e:
        # Print exception details for debugging
        print(f"Error opening app with subprocess: {e}")
        
        # Fallback to pyautogui if subprocess fails
        gui.press("win")
        time.sleep(0.5)  # Adjusted delay
        gui.write(text)
        time.sleep(0.5)  # Adjusted delay
        gui.press("enter")
