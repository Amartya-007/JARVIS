from webscout import PhindSearch as brain
from rich import print
from webscout.AIutel import RawDog
from dotenv import load_dotenv
import os

load_dotenv()
file_path = os.getenv("FILE_PATH")


# Ensure the file path is provided and check if the file exists; if not, create it
if file_path is None:
    raise ValueError("The FILE_PATH environment variable is not set.")


rawdog = RawDog()
intro_prompt = rawdog.intro_prompt

ai = brain(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=intro_prompt,
    filepath=file_path,
    update_file=True,
    proxies={},
    history_offset=10250,
    act=None,
)

def Main_Brain(text):
    try:
        response = ai.chat(text)
        rawdog_feedback = rawdog.main(response)
        if rawdog_feedback:
            print(rawdog_feedback)
            ai.chat(rawdog_feedback)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
