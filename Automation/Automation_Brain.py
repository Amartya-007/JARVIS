from Automation.open_App import open_App
from Automation.web_open import openweb
import pyautogui as gui
from Automation.Play_music import play_music_on_youtube
from Text_Speak import Fast_DF_TTS
from Automation.Spotify_music import play_music_on_spotify
from Automation.Battery import check_percentage
from os import getcwd
import time
from Automation.tab_automation import perform_browser_action
from Automation.Youtube_play_back import perform_media_action
import pywhatkit
from Automation.scroll_system import perform_scroll_action
import threading
from Text_Speak.Fast_DF_TTS import speak

def play():
    gui.press("space")

def pause():
    gui.press("space")

def search_google(query):
    pywhatkit.search(query)
    

def close():
    gui.hotkey('alt','f4')
    
def search(text):
    gui.press("/")
    time.sleep(0.3)
    gui.write(text)

def Open_Brain(text):
    if "website" in text or "open website name" in text:
        text = text.replace("open","").strip()
        text = text.replace("website","").strip()
        text = text.replace("open website name","").strip()
        t1 = threading.Thread(target=speak,args=(f"Navigating {text} website",))
        t2 = threading.Thread(target=openweb,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        text = text.replace("open","").strip()
        text = text.replace("app","").strip()
        t1 = threading.Thread(target=speak,args=(f"Navigating {text} application",))
        t2 = threading.Thread(target=open_App,args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        

def delete_history_chrome():
    gui.hotkey("ctrl","shift","del")
    time.sleep(0.5)
    gui.press("enter")
    

def clear_file():
    with open(f"{getcwd()}\\input.txt","w") as file:
        file.truncate(0)

def Auto_main_brain(text):
    """
    Main function to handle various commands and perform corresponding actions.
    """
    try:
        if text.startswith("open"):
            Open_Brain(text)
        elif "close" in text:
            close()
        elif "play music" in text or "play music on youtube" in text:
            Fast_DF_TTS.speak("Which song do you want to play, sir.")
            clear_file()
            output_text = ""
            while True:
                with open("input.txt", "r") as file:
                    input_text = file.read().lower().strip()
                if input_text != output_text:
                    output_text = input_text
                    if output_text.endswith("song"):
                        play_music_on_youtube(output_text)
                        break
        elif "play some music" in text or "play music on spotify" in text:
            Fast_DF_TTS.speak("Which song do you want to play, sir.")
            clear_file()
            output_text = ""
            while True:
                with open("input.txt", "r") as file:
                    input_text = file.read().lower().strip()
                if input_text != output_text:
                    output_text = input_text
                    if output_text.endswith("song"):
                        play_music_on_spotify(output_text)
                        break
        elif "check battery percentage" in text or "check battery level" in text:
            check_percentage()
        elif text.startswith("search"):
            search_term = text.replace("search", "").strip()
            t1 = threading.Thread(target=speak, args=(f"Doing research about {search_term}",))
            t2 = threading.Thread(target=search, args=(search_term,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
            time.sleep(0.5)
            gui.press("enter")
        elif "search in google" in text:
            search_term = text.replace("search in google", "").strip()
            t1 = threading.Thread(target=speak, args=(f"Performing research about {search_term} in Google search engine",))
            t2 = threading.Thread(target=search_google, args=(search_term,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()
        elif "play" in text:
            play()
        elif "stop" in text or "pause" in text:
            pause()
        elif "delete history" in text:
            delete_history_chrome()
        else:
            perform_browser_action(text)
            perform_media_action(text)
            perform_scroll_action(text)
    except Exception as e:
        print("Error: " + str(e))
