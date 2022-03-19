"""
Get GoT characters with api
Part of DataRockie - Data Sciences Bootcamp
link : https://colab.research.google.com/gist/risgmf74/7939adf1893c803c22cbbca21f149b10/api-homework.ipynb
"""

import pandas as pd
import requests
import time

# Endpoint - Base URL
url = "https://anapioficeandfire.com/api/characters/"

# Request data with get
response = requests.get(url)
print(response) # For test response, should get "200"

# Get character name, From 1 to 2137 characters

characters_list = []

def getCharacter():
"""getCharacter function will print result after fuction completed"""

  print("Enter your value (Numbers must between 1 to 2137)")
  start = int(input("Start: "))
  end = int(input("End: "))

  for i in range(start, end):
    new_url = url + str(i)
    response = requests.get(new_url)
    response_json = response.json()
    data = [
        response_json['name'],
        response_json['gender'],
        response_json['culture'],
        response_json['died'],
        response_json['titles']
    ]
    characters_list.append(data)
    time.sleep(2)

  print(characters_list)

# Convert characters_list to DataFrame with Pandas
characters_df = pd.DataFrame(characters_list, columns = ["name", "gender", "culture", "died", "titles"])
