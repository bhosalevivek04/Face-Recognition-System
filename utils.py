import os
import pickle
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

DB_PATH = os.path.join("data", "face_db.pkl")

def prepare_audio(audio_file_path):
    """
    Check if the provided audio file is in mp3 or m4a format.
    If yes, convert it to WAV (using PCM 16-bit little-endian,
    with a sample rate of 16000 Hz and mono channel) and return the new file path.
    If the file is already WAV, return the original file path.
    """
    ext = os.path.splitext(audio_file_path)[1].lower()
    if ext in [".mp3", ".m4a"]:
        wav_path = os.path.splitext(audio_file_path)[0] + ".wav"
        try:
            audio = AudioSegment.from_file(audio_file_path, format=ext[1:])
            # Export with desired parameters: PCM 16-bit little-endian, 16000 Hz, mono.
            audio.export(wav_path, format="wav", codec="pcm_s16le", parameters=["-ar", "16000", "-ac", "1"])
            logger.info(f"Converted {audio_file_path} to {wav_path}")
            return wav_path
        except Exception as e:
            logger.error(f"Audio conversion failed for {audio_file_path}: {e}")
            return audio_file_path
    return audio_file_path

def speech_to_text(audio_file_path):
    """
    Convert an audio file (expected to be in WAV format) to text using SpeechRecognition.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        text = ""
    except sr.RequestError:
        text = ""
    return text.strip()

def load_face_db():
    """
    Load the face database from the pickle file.
    If the file does not exist, return an empty dictionary.
    """
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "rb") as f:
        return pickle.load(f)

def save_face_db(face_db):
    """
    Save the face database (a dictionary) to the pickle file.
    """
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "wb") as f:
        pickle.dump(face_db, f)