# Face Recognition Project

This project is designed to demonstrate the fundamental principles of face recognition. It utilizes face embeddings to identify and recognize individuals, and includes speech-to-text to extract names from audio during registration.

## Project Structure

The project is organized as follows:

```plaintext
audio/
    - Recorded audio files
face_module.py
main.py
photo/
    - Face images for recognition
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

```
pip install -r requirements.txt
```

## Running the Server

To start the Flask server, run the following command:

```
python main.py
```

The server will run on [http://localhost:5000](http://localhost:5000).

## API Endpoints

### Register

**URL:** `/register`
**Method:** `POST`
**Payload:**

- `image`: Image file (JPEG/PNG) containing the person's face.
- `audio`: Audio file (mp3, m4a, or wav) with the person speaking their name.

**Response:**

- `200 OK`: Registration successful, along with total registered samples.
- `400 Bad Request`: Missing image or audio file, or other validation errors.
- `500 Internal Server Error`: Server error.

### Recognize

**URL:** `/recognize`
**Method:** `POST`
**Payload:**

- `image`: Image file to be recognized.

**Response:**

- `200 OK`: Recognition successful, including recognized name, matching distance, and a base64-encoded MP3 of the recognized name.
- `400 Bad Request`: Missing image file or no face detected.
- `500 Internal Server Error`: Server error.

## Testing

### Register Test

To test the registration endpoint, run:

```
python test_register.py
```

### Recognize Test

To test the recognition endpoint, run:

```
python test_recognize.py
```

## Utility Functions

### utils.py

- `prepare_audio(audio_file_path)`: Converts audio files to WAV format if necessary.
- `speech_to_text(audio_file_path)`: Extracts text from audio files using SpeechRecognition.
- `load_face_db()`: Loads the face database from a file.
- `save_face_db(face_db)`: Saves the face database to a file.

### face_module.py

- `preprocess_image(image)`: Preprocesses images by converting to grayscale and applying histogram equalization.
- `extract_face_encoding(image_path)`: Extracts face encodings from images.
- `compare_face(query_encoding, face_db, tolerance=0.5)`: Compares face encodings to the stored database and returns a match.

## Online Database

In addition to the local face database, this project also supports storing face encodings in MongoDB. To enable this, make sure to set the MongoDB connection details in `.env` and modify `main.py` to load from MongoDB instead of a local file.

## Conclusion

This project provides a comprehensive demonstration of face recognition using face embeddings. It includes detailed documentation, testing, and support for both local and online face databases.