import os
from winotify import Notification, audio
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve the JARVIS_LOGO path from environment variables
logo_path = os.getenv("JARVIS_LOGO")

def Alert(Text):
    # Use the logo_path retrieved from the .env file
    icon_path = logo_path

    toast = Notification(
        app_id="🧑‍💼 J A R V I S ",
        title=Text,
        duration="long",
        icon=icon_path
    )

    toast.set_audio(audio.Default, loop=False)

    toast.add_actions(label="Click me", launch="https://www.google.com")
    toast.add_actions(label="Dismiss", launch="https://www.google.com")

    toast.show()
