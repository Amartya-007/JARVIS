import requests 
from playsound import playsound  
import os
from dotenv import load_dotenv  # pip install python-dotenv
from typing import Union

# Load environment variables from .env file
load_dotenv()

# Retrieve the API URL and User-Agent from environment variables
API_URL = os.getenv("API_URL")
USER_AGENT = os.getenv("USER_AGENT")


def generate_audio(message: str, voice: str = "Matthew") -> Union[bytes, None]:
    """
    Generates audio content from a text message using the specified voice.

    Args:
        message (str): The text message to convert to speech.
        voice (str): The voice to use for the speech synthesis.

    Returns:
        Union[bytes, None]: The binary audio content or None if an error occurs.
    """
    url: str = f"{API_URL}?voice={voice}&text={requests.utils.quote(message)}"
    headers = {
        'User-Agent': USER_AGENT
    }

    try:
        result = requests.get(url=url, headers=headers)
        result.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return result.content
    except requests.RequestException as e:
        print(f"An error occurred while generating audio: {e}")
        return None


def speak(message: str, voice: str = "Matthew", folder: str = "", extension: str = ".mp3") -> Union[None, str]:
    """
    Converts a text message to speech, plays it, and then removes the temporary audio file.

    Args:
        message (str): The text message to convert to speech.
        voice (str): The voice to use for the speech synthesis.
        folder (str): The folder to save the temporary audio file.
        extension (str): The file extension for the audio file.

    Returns:
        Union[None, str]: None if successful, or an error message string if an error occurs.
    """
    try:
        result_content = generate_audio(message, voice)
        if result_content is None:
            raise ValueError("Failed to generate audio content.")
        
        file_path = os.path.join(folder, f"{voice}{extension}")
        with open(file_path, "wb") as file:
            file.write(result_content)
        
        playsound(file_path)
        os.remove(file_path)
        return None
    except Exception as e:
        print(f"An error occurred while speaking: {e}")
        return str(e)


# Example usage
speak("I am being build again by amartya vishwakarma.")
