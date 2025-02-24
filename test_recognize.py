import requests
import base64

# URL of the running Flask server
BASE_URL = "http://localhost:5000"
rec_url = f"{BASE_URL}/recognize"

# Path to your test recognition image (adjust the filename if needed)
rec_image_path = "photo/Manas3.jpg"

# Open the recognition image file in binary mode and send a POST request
with open(rec_image_path, "rb") as rec_file:
    files = {"image": rec_file}
    response = requests.post(rec_url, files=files)

print("Status Code:", response.status_code)
print("Raw Response Text:", response.text)

try:
    result = response.json()
    print("Recognition Response:")
    print(result)

    # If an audio MP3 is returned, decode and save it for playback
    audio_data = result.get("audio_mp3_base64")
    if audio_data:
        with open("recognized_name.mp3", "wb") as f:
            f.write(base64.b64decode(audio_data))
        print("Audio file saved as recognized_name.mp3")
except Exception as e:
    print("Error decoding JSON:", e)
