import pyautogui

def open_new_tab():
    #* Open a new browser tab.
    try:
        pyautogui.hotkey('ctrl', 't')
    except Exception as e:
        print(f"An error occurred: {e}")

def close_tab():
    #* Close the current browser tab.
    try:
        pyautogui.hotkey('ctrl', 'w')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_browser_menu():
    #* Open the browser menu.
    try:
        pyautogui.hotkey('alt', 'f')
    except Exception as e:
        print(f"An error occurred: {e}")

def zoom_in():
    #* Zoom in on the current page.
    try:
        pyautogui.hotkey('ctrl', '+')
    except Exception as e:
        print(f"An error occurred: {e}")

def zoom_out():
    #* Zoom out on the current page.
    try:
        pyautogui.hotkey('ctrl', '-')
    except Exception as e:
        print(f"An error occurred: {e}")

def refresh_page():
    #* Refresh the current page.
    try:
        pyautogui.hotkey('ctrl', 'r')
    except Exception as e:
        print(f"An error occurred: {e}")

def switch_to_next_tab():
    #* Switch to the next browser tab.
    try:
        pyautogui.hotkey('ctrl', 'tab')
    except Exception as e:
        print(f"An error occurred: {e}")

def switch_to_previous_tab():
    #* Switch to the previous browser tab.
    try:
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_history():
    #* Open the browser history.
    try:
        pyautogui.hotkey('ctrl', 'h')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_bookmarks():
    #* Open the bookmarks bar.
    try:
        pyautogui.hotkey('ctrl', 'b')
    except Exception as e:
        print(f"An error occurred: {e}")

def go_back():
    #* Go back to the previous page.
    try:
        pyautogui.hotkey('alt', 'left')
    except Exception as e:
        print(f"An error occurred: {e}")

def go_forward():
    #* Go forward to the next page.
    try:
        pyautogui.hotkey('alt', 'right')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_dev_tools():
    #* Open the browser's developer tools.
    try:
        pyautogui.hotkey('ctrl', 'shift', 'i')
    except Exception as e:
        print(f"An error occurred: {e}")

def toggle_full_screen():
    #* Toggle full screen mode.
    try:
        pyautogui.hotkey('f11')
    except Exception as e:
        print(f"An error occurred: {e}")

def open_private_window():
    #* Open a new private browsing window.
    try:
        pyautogui.hotkey('ctrl', 'shift', 'n')
    except Exception as e:
        print(f"An error occurred: {e}")

def perform_browser_action(text):
    #* Perform a browser action based on the given text command.
    if "open new tab" in text or "new tab kholo" in text:
        open_new_tab()
    elif "close tab" in text or "tab band karo" in text:
        close_tab()
    elif "open browser menu" in text or "browser menu kholo" in text:
        open_browser_menu()
    elif "zoom in" in text or "zoom in karo" in text:
        zoom_in()
    elif "zoom out" in text or "zoom out karo" in text:
        zoom_out()
    elif "refresh page" in text or "page refresh karo" in text:
        refresh_page()
    elif "switch to next tab" in text or "next tab par jao" in text:
        switch_to_next_tab()
    elif "switch to previous tab" in text or "previous tab par jao" in text:
        switch_to_previous_tab()
    elif "open history" in text or "history kholo" in text:
        open_history()
    elif "open bookmarks" in text or "bookmarks kholo" in text:
        open_bookmarks()
    elif "go back" in text or "peeche jao" in text:
        go_back()
    elif "go forward" in text or "aage jao" in text:
        go_forward()
    elif "open dev tools" in text or "dev tools kholo" in text:
        open_dev_tools()
    elif "toggle full screen" in text or "full screen karo" in text:
        toggle_full_screen()
    elif "open private window" in text or "private window kholo" in text:
        open_private_window()
    else:
        pass 
