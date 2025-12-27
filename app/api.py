import requests
import os

from dotenv import load_dotenv

load_dotenv()

url = "https://ocr43.p.rapidapi.com/v1/results"

payload = '''-----011000010111000001101001r
Content-Disposition: form-data; name="image"r
r
gcc-commands.jpgr
-----011000010111000001101001r
Content-Disposition: form-data; name="url"r
r
https://storage.googleapis.com/api4ai-static/samples/ocr-1.pngr
-----011000010111000001101001--r
r
'''

headers = {
	"x-rapidapi-key": os.environ.get("X_RAPIDAPI_KEY"),
	"x-rapidapi-host": "ocr43.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}

try:
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        error_detail = response.json().get('detail')
        print(f"Error ({response.status_code}): {error_detail}")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the API")
