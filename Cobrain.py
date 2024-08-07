import random
import threading
from Automation.tab_automation import *
from Automation.Automation_Brain import Auto_main_brain, clear_file
from Speech_to_text.listen import listen
from Text_Speak.Fast_DF_TTS import speak
from Dialogs.Jaru_speaks import online_dlg, offline_dlg
from Automation.Battery import battery_Alert
from Alarm_and_timeSchedule.brain import input_manage, input_manage_alarm
from Features.internet import get_internet_speed
from Brain.brain import Main_Brain
from Features.create_files import create_file
from Automation.Battery import check_plug
from Vision.Vbrain import *

numbers = ["1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:", "9:"]
spl_numbers = ["11:", "12:"]

ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)

def check_inputs():
    output_text = ""
    while True:
        with open("input.txt","r") as file:
            input_text = file.read().lower() 
        if input_text != output_text:
            output_text = input_text
            if output_text.startswith("tell me"):
                output_text = output_text.replace(" p.m.","PM")
                output_text = output_text.replace(" a.m.","AM")
                if "11:" in output_text or "12:" in output_text:
                    input_manage(output_text)
                    clear_file()
                else:
                    for number in numbers:
                        if number in output_text:
                           output_text = output_text.replace(number,f"0{number}")
                           input_manage(output_text)
                           clear_file()
            elif output_text.startswith("set alarm"):
                output_text = output_text.replace(" p.m.","PM")
                output_text = output_text.replace(" a.m.","AM")
                if "11:" in output_text or "12:" in output_text:
                    input_manage_alarm(output_text)
                    clear_file()
                else:
                    for number in numbers:
                        if number in output_text:
                           output_text = output_text.replace(number,f"0{number}")
                           input_manage_alarm(output_text)
                           clear_file()
            elif "check internet speed" in output_text:
                speak("checking your internet speed")
                speed = get_internet_speed()
                speak(f"the device is running on {speed} Mbps internet speed")
            elif "jarvis" in output_text:
                response = Main_Brain(output_text)
                speak(response)
            elif output_text.startswith("create"):
                if "file" in output_text:
                    create_file(output_text)
            elif "battery" in output_text:
                battery_Alert()
            elif "what is this" in output_text or "what can you see" in output_text:
                    img_path = "captured_image.png"
                    if capture_image_and_save(img_path):
                        encoded_image = encode_image_to_base64(img_path)
                        ans = vbrain(encoded_image)
                        speak(ans)
            elif "open new tab" in output_text or "close tab" in output_text or "open browser menu" in output_text or "zoom in" in output_text or "zoom out" in output_text or "refresh page" in output_text or "switch to next tab" in output_text or "switch to previous tab" in output_text or "open history" in output_text or "open bookmarks" in output_text or "go back" in output_text or "go forward" in output_text or "open dev tools" in output_text or "toggle full screen" in output_text or "open private window" in output_text:
                perform_browser_action(output_text)
            else:
                Auto_main_brain(output_text)

def Jarvis():
    clear_file()
    t1 = threading.Thread(target=listen)
    t2 = threading.Thread(target=check_inputs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    

