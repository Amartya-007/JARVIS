import re
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set default paths if environment variables are not set
SCHEDULE_FILE_PATH = os.getenv('SCHEDULE_FILE_PATH')
ALARM_FILE_PATH = os.getenv('ALARM_FILE_PATH')

# Global variable to store the last write date
last_write_date = None

def get_current_date():
    return datetime.now().strftime('%d/%m/%Y')

def get_current_time():
    return datetime.now().strftime('%H:%M:%S')

def parse_input(input_text):
    time_regex = r'(\d{1,2}:\d{2} ?(?:AM|PM|am|pm))'
    times = re.findall(time_regex, input_text)
    
    if times:
        time_match = times[0]
        formatted_time = time_match.strip().replace(" ", "").upper()
        updated_input_text = re.sub(time_regex, "", input_text).replace("at", "").replace("tell me", "").replace("Tell me", "").replace("to", "").strip()
        formatted_output = f"{formatted_time} = Sir, this is your {updated_input_text} time"
        return formatted_output, formatted_time
    else:
        return "No valid time found in input", None

def parse_input_alarm(input_text):
    time_regex = r'(\d{1,2}:\d{2} ?(?:AM|PM|am|pm))'
    times = re.findall(time_regex, input_text)
    
    if times:
        time_match = times[0]
        formatted_time = time_match.strip().replace(" ", "").upper()
        return formatted_time
    else:
        return "No valid time found in input"

def read_last_date(filename):
    if not os.path.exists(filename):
        return None
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Check from the bottom
    for line in reversed(lines):
        if line.startswith('------'):
            return line.strip().split('---')[1].strip()
    
    return None

def get_last_entry(filename):
    if not os.path.exists(filename):
        return None
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Read from the bottom
    for line in reversed(lines):
        if line.strip():
            return line.strip()
    
    return None

def write_header(filename):
    global last_write_date
    current_date = get_current_date()
    current_time = get_current_time()
    
    if last_write_date != current_date:
        with open(filename, 'a') as file:
            file.write(f"\n------ {current_date} {current_time} ---\n")
        last_write_date = current_date

def write_data(output_text, filename):
    last_entry = get_last_entry(filename)
    
    with open(filename, 'a') as file:
        if last_entry :
            file.write('\n')  # Add a blank line if the last entry is the same
        file.write(output_text + '\n')

def save_to_file(output_text, filename):
    global last_write_date
    last_date_in_file = read_last_date(filename)
    current_date = get_current_date()

    if last_date_in_file != current_date:
        write_header(filename)
        write_data(output_text, filename)
    else:
        write_data(output_text, filename)

def save_to_alarm_file(time, filename):
    global last_write_date
    last_date_in_file = read_last_date(filename)
    current_date = get_current_date()

    if last_date_in_file != current_date:
        write_header(filename)
        write_data(time, filename)
    else:
        write_data(time, filename)

def input_manage(input_text):
    output, time = parse_input(input_text)
    if output != "No valid time found in input":
        save_to_file(output, SCHEDULE_FILE_PATH)
        print("Schedule_Data_Saved")
    else:
        print(output)

def input_manage_alarm(input_text):
    time = parse_input_alarm(input_text)
    if time != "No valid time found in input":
        save_to_alarm_file(time, ALARM_FILE_PATH)
        print("Alarm_Data_Saved")
    else:
        print("No valid time found in input")

