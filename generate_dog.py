import requests
from time import sleep
from PIL import Image
from urllib.request import urlopen
from random import randint

breeds = {
    "pomeranian": "Smol doggo",
    "husky": "Husky",
    "shiba": "Shiba",
    "corgi": "Corgo",
    "germanshepherd": "German shephard",
    "retriever/golden": "Golden boi"
    }

breed_length = len(breeds)
random_int = randint(0,breed_length-1)
my_breed = list(breeds.keys())[random_int]                      ##select random breed

url = "https://dog.ceo/api/breed/{}/images/random".format(my_breed)

print("generating dog...")
response = requests.get(url)                #api call

if response.status_code == 200:             #response check
    print("SUCCESS")
else:
    print("ERROR\ncode {}".format(response.status_code))
    print("Exiting...")
    sleep(2)
    exit()

data = response.json()                      #get data json

with urlopen(data["message"]) as dataUrl:   #read from url, write binary to local jpg
    with open("dog.jpg", 'wb') as f:
        f.write(dataUrl.read())

print("{} generated!".format(breeds[my_breed]))
image = Image.open("dog.jpg")               #display
image.show()    
