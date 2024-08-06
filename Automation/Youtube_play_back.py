import pyautogui

def volume_up():
    #* Increase the volume by pressing the 'up' arrow key.
    pyautogui.press('up')

def volume_down():
    #* Decrease the volume by pressing the 'down' arrow key.
    pyautogui.press('down')

def seek_forward():
    #* Seek forward by pressing the 'right' arrow key.
    pyautogui.press('right')

def seek_backward():
    #* Seek backward by pressing the 'left' arrow key.
    pyautogui.press('left')

def seek_forward_10s():
    #* Seek forward 10 seconds by pressing the 'l' key.
    pyautogui.press('l')

def seek_backward_10s():
    #* Seek backward 10 seconds by pressing the 'j' key.
    pyautogui.press('j')

def seek_backward_frame():
    #* Seek backward by one frame by pressing the ',' key.
    pyautogui.press(',')

def seek_forward_frame():
    #* Seek forward by one frame by pressing the '.' key.
    pyautogui.press('.')

def seek_to_beginning():
    #* Seek to the beginning by pressing the 'home' key.
    pyautogui.press('home')

def seek_to_end():
    #* Seek to the end by pressing the 'end' key.
    pyautogui.press('end')

def seek_to_previous_chapter():
    #* Seek to the previous chapter by pressing 'ctrl' + 'left' arrow key.
    pyautogui.hotkey('ctrl', 'left')

def seek_to_next_chapter():
    #* Seek to the next chapter by pressing 'ctrl' + 'right' arrow key.
    pyautogui.hotkey('ctrl', 'right')

def decrease_playback_speed():
    #* Decrease playback speed by pressing 'shift' + ',' key.
    pyautogui.hotkey('shift', ',')

def increase_playback_speed():
    #* Increase playback speed by pressing 'shift' + '.' key.
    pyautogui.hotkey('shift', '.')

def move_to_next_video():
    #* Move to the next video by pressing 'shift' + 'n' key.
    pyautogui.hotkey('shift', 'n')

def move_to_previous_video():
    #* Move to the previous video by pressing 'shift' + 'p' key.
    pyautogui.hotkey('shift', 'p')

def perform_media_action(text):
    #* Perform the appropriate media action based on the input text.
    if "volume up" in text or "volume badhao" in text:
        volume_up()
    elif "volume down" in text or "volume ghatao" in text:
        volume_down()
    elif "seek forward" in text or "aage badhao" in text:
        seek_forward()
    elif "seek backward" in text or "peeche karo" in text:
        seek_backward()
    elif "seek forward 10 seconds" in text or "10 second aage badhao" in text:
        seek_forward_10s()
    elif "seek backward 10 seconds" in text or "10 second peeche karo" in text:
        seek_backward_10s()
    elif "seek backward frame" in text or "frame peeche karo" in text:
        seek_backward_frame()
    elif "seek forward frame" in text or "frame aage badhao" in text:
        seek_forward_frame()
    elif "seek to beginning" in text or "shuruat par jao" in text:
        seek_to_beginning()
    elif "seek to end" in text or "ant par jao" in text:
        seek_to_end()
    elif "seek to previous chapter" in text or "previous chapter par jao" in text:
        seek_to_previous_chapter()
    elif "seek to next chapter" in text or "next chapter par jao" in text:
        seek_to_next_chapter()
    elif "decrease playback speed" in text or "speed kam karo" in text:
        decrease_playback_speed()
    elif "increase playback speed" in text or "speed badhao" in text:
        increase_playback_speed()
    elif "move to next video" in text or "next video par jao" in text:
        move_to_next_video()
    elif "move to previous video" in text or "previous video par jao" in text:
        move_to_previous_video()
    else:
        pass
