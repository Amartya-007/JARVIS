import os
import time
import threading
from Alert import Alert
from Text_Speak.Fast_DF_TTS import speak
from os import getcwd

# Load schedule from the file
def load_schedule(file_path):
    schedule = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    line_time, activity = line.strip().split(' = ')
                    schedule[line_time.strip()] = activity.strip()
    except Exception as e:
        print(f"Error loading schedule: {e}")
    return schedule

# Check the schedule file for updates and trigger alerts if needed
def check_schedule(file_path):
    last_modified = 0
    while True:
        current_time = time.strftime("%I:%M%p")
        try:
            modified = os.path.getmtime(file_path)
            if modified != last_modified:
                last_modified = modified
                schedule = load_schedule(file_path)
            
            if current_time in schedule:
                text = schedule[current_time]
                threading.Thread(target=Alert, args=(text,)).start()
                threading.Thread(target=speak, args=(text,)).start()
        
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(60)

# Load alarm times from the file
def load_AlamTime(file_path):
    schedule = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                time_str = line.strip()
                if time_str:
                    schedule[time_str] = "This is Alarm"
    except Exception as e:
        print(f"Error loading alarm file: {e}")
    return schedule

Alam_path = os.path.join(getcwd(), 'Alam_data.txt')

# Check the alarm file for updates and trigger alarms if needed
def check_Alam(Alam_path):
    last_modified = 0
    while True:
        current_time = time.strftime("%I:%M%p")
        try:
            modified = os.path.getmtime(Alam_path)
            if modified != last_modified:
                last_modified = modified
                schedule = load_AlamTime(Alam_path)
            
            if current_time in schedule:
                text = schedule[current_time]
                threading.Thread(target=Alert, args=(text,)).start()
                threading.Thread(target=speak, args=(text,)).start()
        
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(10)

# Example usage
if __name__ == "__main__":
    # Start monitoring the schedule and alarm files in separate threads
    schedule_thread = threading.Thread(target=check_schedule, args=(os.path.join(getcwd(), 'schedule.txt'),))
    alarm_thread = threading.Thread(target=check_Alam, args=(Alam_path,))
    
    schedule_thread.start()
    alarm_thread.start()
    
    schedule_thread.join()
    alarm_thread.join()
