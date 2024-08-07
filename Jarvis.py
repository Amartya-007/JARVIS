import threading
import random
import os
from dotenv import load_dotenv

from net_cheak import is_online
from Alert import Alert
from Dialogs.Jaru_speaks import online_dlg, offline_dlg
from Cobrain import Jarvis
from Text_Speak.Fast_DF_TTS import speak
from Automation.Battery import check_plug
from Alarm_and_timeSchedule.throw_alert import check_schedule, check_Alam

# Load environment variables
load_dotenv()

# Paths and URLs from .env file
ALAM_PATH = os.getenv("ALARM_FILE_PATH")
FILE_PATH = os.getenv("SCHEDULE_FILE_PATH")


ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)

def wish():
    t1 = threading.Thread(target=speak, args=(ran_online_dlg,))
    t2 = threading.Thread(target=Alert, args=(ran_online_dlg,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def main():
    if is_online():
        wish()
        t3 = threading.Thread(target=check_plug)
        t4 = threading.Thread(target=check_schedule, args=(FILE_PATH,))
        t5 = threading.Thread(target=Jarvis)
        t6 = threading.Thread(target=check_Alam, args=(ALAM_PATH,))
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
    else:
        Alert(ran_offline_dlg)

main()
