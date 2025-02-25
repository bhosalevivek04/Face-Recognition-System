import requests

# URL of the running server
BASE_URL = "http://localhost:5000"
reg_url = f"{BASE_URL}/register"

# Update these paths to point to your test registration files:
reg_image_path = "photo/Navnath1.jpg"   # Registration image (JPEG/PNG) in the "photo" folder
reg_audio_path = "audio/Navnath.wav"  # Registration audio file (WAV or MP3)

try:
    with open(reg_image_path, "rb") as img_file, open(reg_audio_path, "rb") as audio_file:
        files = {
            "image": img_file,
            "audio": audio_file
        }
        response = requests.post(reg_url, files=files)
    
    print("Status Code:", response.status_code)
    try:
        json_response = response.json()
        print("Registration Response:")
        print(json_response)
    except Exception as e:
        print("Failed to decode JSON. Raw response:")
        print(response.text)
        print("Error:", e)
except Exception as ex:
    print("An error occurred:", ex)
