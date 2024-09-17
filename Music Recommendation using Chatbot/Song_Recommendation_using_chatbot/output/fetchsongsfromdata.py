import pandas as pd
import random
import csv
import json

# Open the CSV file and create a DictReader object
def random_songs():
    with open('../Spotify-Machine-Learning/data/data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        json_list = []
        for row in reader:
            json_list.append(dict(row))
    #     with open('output.json', 'w') as jsonfile:
    #         json.dump(json_list, jsonfile, indent=4)

    # output = json.loads(json_list)
    classified_data = {
        'Calm': [],
        'Happy': [],
        'Sad': [],
        'Energetic': []
    }

    # Iterate over the JSON objects and classify them based on the "mood" key
    for obj in json_list:
        mood = obj['mood']
        classified_data[mood].append(obj)


    suggestion_list = []
    if emotion == "joy":
        suggestion_list = random.sample(classified_data['Energetic'], 10)
    elif emotion == "happy":
        suggestion_list = random.sample(classified_data['Happy'], 10)
    elif emotion == "sad":
        suggestion_list = random.sample(classified_data['Sad'], 10)
    elif emotion == "disgust":
        suggestion_list = random.sample(classified_data['Calm'], 10)
    elif emotion == "fear":
        suggestion_list = random.sample(classified_data['Calm'], 10)


# Write the classified data to separate JSON files
# for mood, objects in classified_data.items():
#     filename = f'{mood}.json'
#     with open(filename, 'w') as f:
#         json.dump(objects, f, indent=4)
