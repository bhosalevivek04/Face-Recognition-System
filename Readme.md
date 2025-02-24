# Face Recognition Project

This project is a face recognition system that allows users to register their faces and recognize them using images. It also includes speech-to-text functionality to extract names from audio files during registration.

## Project Structure

```plaintext
audio/
    - Manas.wav
    - Navnath.wav
    - Vivek.wav
data/
    - face_db.pkl
face_module.py
main.py
photo/
    - Manas1.jpg
    - Manas2.jpg
    - Manas3.jpg
    - Navnath1.jpg
    - Vivek1.jpg
    - Vivek2.jpg
    - Vivek3.jpg
    - Vivek4.jpg
recognized_name.mp3
requirements.txt
test_recognize.py
test_register.py
utils.py
```

## Requirements

- Python 3.6+
- Flask==2.2.3
- face_recognition==1.3.0
- SpeechRecognition==3.8.1
- gTTS==2.2.4
- opencv-python==4.7.0.72
- numpy==1.23.5
- pydub==0.25.1

Install the required packages using:

```sh
pip install -r requirements.txt
```

## Running the Server

To start the Flask server, run:

```sh
python main.py
```

The server will start on [http://localhost:5000](http://localhost:5000).

## API Endpoints

### Register

- **URL:** `/register`
- **Method:** `POST`
- **Description:** Registers a new face with an associated name extracted from an audio file.

**Form Data:**

- `image`: Image file (JPEG/PNG) containing the person's face.
- `audio`: Audio file (mp3, m4a, or wav) with the person speaking their name.

**Response:**

- `200 OK`: Registration successful.
- `400 Bad Request`: Missing image or audio file, or other validation errors.
- `500 Internal Server Error`: Server error.

### Recognize

- **URL:** `/recognize`
- **Method:** `POST`
- **Description:** Recognizes a face from an image and returns the recognized name and a base64-encoded MP3 of the name.

**Form Data:**

- `image`: Image file to be recognized.

**Response:**

- `200 OK`: Recognition successful.
- `400 Bad Request`: Missing image file or no face detected.
- `500 Internal Server Error`: Server error.

## Testing

### Register Test

To test the registration endpoint, run:

```sh
python test_register.py
```

### Recognize Test

To test the recognition endpoint, run:

```sh
python test_recognize.py
```

## Utility Functions

### utils.py

- `prepare_audio(audio_file_path)`: Converts audio files to WAV format if necessary.
- `speech_to_text(audio_file_path)`: Converts audio files to text using SpeechRecognition.
- `load_face_db()`: Loads the face database from a pickle file.
- `save_face_db(face_db)`: Saves the face database to a pickle file.

### face_module.py

- `preprocess_image(image)`: Preprocesses images by converting to grayscale and applying histogram equalization.
- `extract_face_encoding(image_path)`: Extracts face encodings from images.
- `compare_face(query_encoding, face_db, tolerance=0.5)`: Compares face encodings with the stored face database.
