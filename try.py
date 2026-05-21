import playsound
import requests
import os


def speak(text: str, model: str="aura-luna-en", filename :str="data.mp3"):
        url = "https://api.deepai.org/speech_response"

        payload = {
            "model": model,
            "text": text
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200: return f"Error: {response.status_code} - {response.text}"
        else:
            with open(filename, 'wb') as f:
                f.write(response.content)
            playsound.playsound(filename)
            os.remove(filename)

