import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the default directory from the environment variable
default_directory = os.getenv("DEFAULT_DIRECTORY")

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_file_extension_and_update_text(text):
    # Define file type mappings
    file_types = {
        "python file": ".py",
        "java file": ".java",
        "text file": ".txt",
        "html file": ".html",
        "css file": ".css",
        "javascript file": ".js",
        "json file": ".json",
        "xml file": ".xml",
        "csv file": ".csv",
        "markdown file": ".md",
        "yaml file": ".yaml",
        "image file": ".jpg",  # Common image formats
        "png file": ".png",
        "gif file": ".gif",
        "webp file": ".webp",
        "video file": ".mp4",  # Common video formats
        "avi file": ".avi",
        "mov file": ".mov",
        "mkv file": ".mkv",
        "audio file": ".mp3",  # Common audio formats
        "wav file": ".wav",
        "ogg file": ".ogg",
        "flac file": ".flac",
        "pdf file": ".pdf",
        "word file": ".docx",
        "excel file": ".xlsx",
        "powerpoint file": ".pptx",
        "text file": ".txt",  # For consistency
        "zip file": ".zip",
        "tar file": ".tar",
        "gzip file": ".gz",
        "rar file": ".rar",
        "7z file": ".7z",
        "docker file": ".dockerfile",
        "sql file": ".sql",
        "bat file": ".bat",
        "sh file": ".sh",
        "config file": ".conf",
        "properties file": ".properties"
    }

    # Initialize extension and cleaned text
    selected_ex = ""
    
    # Iterate over file types to find the matching extension and update text
    for file_type, ext in file_types.items():
        if file_type in text:
            selected_ex = ext
            text = text.replace(file_type, "")
            break

    # Clean up the text for file name, removing articles and extra spaces
    text = text.replace("named", "").replace("with name", "").replace("create", "").strip()
    # Remove articles "a", "an", "the" if they are at the beginning of the text
    text = ' '.join(word for word in text.split() if word.lower() not in {"a", "an", "the"})
    return selected_ex, text

def create_file(text, directory=None):
    # Use the directory from the function parameter or default to the environment variable
    directory = directory or default_directory
    
    # Ensure the directory exists
    ensure_directory_exists(directory)
    
    # Get file extension and clean text
    selected_ex, clean_text = get_file_extension_and_update_text(text)

    # Define the file name based on whether "named" or "with name" was specified
    file_name = clean_text if clean_text else "demo"
    
    file_path = os.path.join(directory, f"{file_name}{selected_ex}")
    
    try:
        with open(file_path, "w") as file:
            pass
        print(f"File '{file_path}' created successfully.")
    except IOError as e:
        print(f"Error creating file: {e}")

# Example usage
create_file("create a python file named example")
create_file("create an image file")
create_file("create a video file named movie")
create_file("create a properties file named config")
