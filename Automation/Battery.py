import psutil
import time
import threading
 
from Alert import Alert
from Text_Speak.Fast_DF_TTS import speak

def battery_Alert():
    while True:
        battery = psutil.sensors_battery()
        percentage = int(battery.percent)
        if percentage == 100:
            Alert("100% charge")
            speak("100% charged. Please unplug it.")
        elif percentage <= 20:
            Alert("Battery Low")
            speak("Sir, sorry to disturb you but battery is low now.")
        elif percentage <= 10:
            Alert("Battery is too Low")
            speak("Sir, sorry to disturb you but we are running on very low battery power.")
        elif percentage <= 5:
            Alert("Battery is going to die")
            speak("Sir, sorry to disturb you but this is your last chance, charge your system now.")
        time.sleep(10)

def check_plug():
    previous_state = psutil.sensors_battery().power_plugged
    while True:
        battery = psutil.sensors_battery()
        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                Alert("Charging **STARTED**")
                speak("Charging Started")
            else:
                Alert("Charging **STOP**")
                speak("Charging Stopped")
            previous_state = battery.power_plugged
        time.sleep(10)

def check_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    Alert(f"The device is running on {percent}% power")
    speak(f"The device is running on {percent}% power")

# Starting threads
threading.Thread(target=battery_Alert, daemon=True).start()
threading.Thread(target=check_plug, daemon=True).start()
threading.Thread(target=check_percentage, daemon=True).start()
