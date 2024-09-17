from flask import Flask, render_template, request, session, redirect, url_for
from chatbot import predict_class, get_response
import json, random, csv
from  get_playlist import get_latest_releases
# import request
from sentiment_analysis import get_emotion

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Abhyoday'

intents = json.loads(open("backend/intents.json", encoding="utf8").read())

chat_history = []
suggestion_list = []
latest_releases = get_latest_releases()

def random_songs(emotion):
        global suggestion_list
        with open('Spotify-Machine-Learning/data/data.csv', 'r', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            json_list = []
            for row in reader:
                json_list.append(dict(row))
        classified_data = {
            'Calm': [],
            'Happy': [],
            'Sad': [],
            'Energetic': []
        }

        for obj in json_list:
            mood = obj['mood']
            classified_data[mood].append(obj)
        
        if emotion == "joy":
            suggestion_list = random.sample(classified_data['Happy'], 10)
        elif emotion == "anger":
            suggestion_list = random.sample(classified_data['Energetic'], 10)
        elif emotion == "sadness":
            suggestion_list = random.sample(classified_data['Sad'], 10)
        elif emotion == "disgust":
            suggestion_list = random.sample(classified_data['Calm'], 10)
        elif emotion == "fear":
            suggestion_list = random.sample(classified_data['Calm'], 10)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    global suggestion_list
    if request.method == 'POST':
        message = request.form["message"]
        ints = predict_class(message)
        res = get_response(ints, intents)
        emotion = get_emotion(message)
        random_songs(emotion)

        temp = {"res": res, "emotion": emotion}
        print("req:", message)
        print(temp)
        get_latest_releases()
        chat_history.append({"req": message, "res": res})
        return redirect(url_for('chatbot'))
    return render_template('chatbot.html', chat_history=chat_history, suggestion_list=suggestion_list,latest_releases = latest_releases)
#     # return json.dumps(temp)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
