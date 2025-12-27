import requests, os

from dotenv import load_dotenv

load_dotenv()

url = "https://ocr43.p.rapidapi.com/v1/results"

headers = {
	"x-rapidapi-key": os.environ.get("X_RAPIDAPI_KEY"),
	"x-rapidapi-host": "ocr43.p.rapidapi.com",
}

file_path = "./app/images/test_reciept.png"

def get_output():
    try:
        with open(file_path, "rb") as image_file:
            files = {"image": image_file}
            response = requests.post(url, files=files, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # print(data)
            text = data['results'][0]['entities'][0]['objects'][0]['entities'][0]['text']
            with open("output.txt", "w") as output_file:
                output_file.write(text)
        else:
            error_detail = response.json().get('detail')
            print(f"Error ({response.status_code}): {error_detail}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API")
    except FileNotFoundError:
        print("Error: The local image file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
