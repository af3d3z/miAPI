from ascii_magic import AsciiArt
import requests

pkm_name = input("Enter Pokemon name: ")

api_url = "https://pokeapi.co/api/v2/pokemon/" + pkm_name
response_json = requests.get(api_url).json()
img_url = response_json['sprites']['front_default']

img = requests.get(img_url)

pkm_sprite = AsciiArt.from_url(url=img_url)
pkm_sprite.to_terminal()

print("Data:")
print("ID: ", response_json['id'])
print("Height: ",  response_json['height'])
print("Weight: ",  response_json['height'])
print("Type 1: ", response_json['types'][0]['type']['name'])
if len(response_json['types']) > 1:
    print("Type 2: ", response_json['types'][1]['type']['name'])
