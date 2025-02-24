import cv2
import face_recognition
import numpy as np

def preprocess_image(image):
    """
    Preprocess the image by converting it to grayscale and applying histogram equalization,
    then converting back to RGB.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    equalized = cv2.equalizeHist(gray)
    processed = cv2.cvtColor(equalized, cv2.COLOR_GRAY2RGB)
    return processed

def extract_face_encoding(image_path):
    """
    Load an image from the given path, preprocess it, and extract the face encoding.
    Returns the first encoding found, or None if no face is detected.
    """
    image = face_recognition.load_image_file(image_path)
    processed_image = preprocess_image(image)
    encodings = face_recognition.face_encodings(processed_image)
    return encodings[0] if encodings else None

def compare_face(query_encoding, face_db, tolerance=0.5):
    """
    Compare the query face encoding against the stored face encodings in face_db.
    Returns the recognized name and the best (lowest) distance. If no match is found,
    returns ("Unknown", None).
    """
    recognized_name = "Unknown"
    best_distance = None
    for name, enc_list in face_db.items():
        results = face_recognition.compare_faces(enc_list, query_encoding, tolerance=tolerance)
        distances = face_recognition.face_distance(enc_list, query_encoding)
        if any(results):
            idx = np.argmin(distances)
            distance = distances[idx]
            if best_distance is None or distance < best_distance:
                best_distance = distance
                recognized_name = name
    return recognized_name, best_distance
