# backend/features/tts.py

from gtts import gTTS
from io import BytesIO

def generate_audio_from_text(text: str, language: str = 'en'):
    """
    Generates an MP3 audio file from the given text and language.
    
    Args:
        text: The text to be converted to speech.
        language: The language of the text (e.g., 'en' for English, 'hi' for Hindi).
        
    Returns:
        BytesIO: An in-memory binary stream of the MP3 audio file.
    """
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=language, slow=False)
        
        # Create an in-memory file-like object
        audio_fp = BytesIO()
        
        # Write the audio data to the in-memory file
        tts.write_to_fp(audio_fp)
        
        # Rewind the file pointer to the beginning
        audio_fp.seek(0)
        
        return audio_fp
        
    except Exception as e:
        print(f"Error generating TTS audio: {e}")
        return None

