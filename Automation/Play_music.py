import pywhatkit as pw

def play_music_on_youtube(song_name):
    """Play a song on YouTube using the provided song name."""
    try:
        pw.playonyt(song_name)
    except Exception as e:
        print(f"An error occurred: {e}")
