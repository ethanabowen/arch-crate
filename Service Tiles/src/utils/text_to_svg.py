import requests

def get_text_to_svg(text:str):
    api_url = "http://localhost:8080/text-to-svg/" + text
    response = requests.get(api_url)
    return response.text