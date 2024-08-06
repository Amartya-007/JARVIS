import pywhatkit as pw

def play_music_on_youtube(song_name):
    """Play a song on YouTube using the provided song name."""
    try:
        pw.playonyt(song_name)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# play_music_on_youtube("Its been a long day without you my friend")

#* Well u dont have to litrally remember the song name, just say the lyrics and it will play the song for you.