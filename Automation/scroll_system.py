import pyautogui

def scroll_up(presses=5):
    # Scroll up by pressing the Up arrow key a specified number of times
    try:
        pyautogui.press('up', presses=presses)
    except Exception as e:
        print(f"An error occurred: {e}")

def scroll_down(presses=5):
    # Scroll down by pressing the Down arrow key a specified number of times
    try:
        pyautogui.press('down', presses=presses)
    except Exception as e:
        print(f"An error occurred: {e}")

def scroll_to_top():
    # Scroll to the top of the page.
    try:
        pyautogui.hotkey('home')
    except Exception as e:
        print(f"An error occurred: {e}")

def scroll_to_bottom():
    
    # Scroll to the bottom of the page
    
    try:
        pyautogui.hotkey('end')
    except Exception as e:
        print(f"An error occurred: {e}")

def perform_scroll_action(text):
    
    #* Perform a scroll action based on the provided text command.
    
    if "scroll up" in text or "upar scroll karo" in text:
        scroll_up()
    elif "scroll down" in text or "neeche scroll karo" in text:
        scroll_down()
    elif "scroll to top" in text or "shuruat par jao" in text:
        scroll_to_top()
    elif "scroll to bottom" in text or "ant par jao" in text:
        scroll_to_bottom()
    else:
        print("Unknown command")

