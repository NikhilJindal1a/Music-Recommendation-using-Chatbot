import json
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ.get("apikey")
url = os.environ.get("url")


authenticator = IAMAuthenticator(apikey)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator)

natural_language_understanding.set_service_url(url)
# msg = `IBM is an American multinational technology company 'headquartered in Armonk, New York, United States, '
# 'with operations in over 170 countries`


def get_emotion(msg):
    response = natural_language_understanding.analyze(
        text=msg,
        features=Features(
            entities=EntitiesOptions(emotion=True, sentiment=True, limit=2),
            keywords=KeywordsOptions(emotion=True, sentiment=True,
                                     limit=2))).get_result()

    # output = json.dumps(response, indent=2)
    # output = json.loads(output)
    emotion = {"sadness": 0,
               "joy": 0,
               "fear": 0,
               "disgust": 0,
               "anger": 0}
    keywords = response["keywords"]
    for keyword in keywords:
        emo = keyword["emotion"]
        emotion["sadness"] = max(emo["sadness"], emotion["sadness"])
        emotion["joy"] = max(emo["joy"], emotion["joy"])
        emotion["fear"] = max(emo["fear"], emotion["fear"])
        emotion["disgust"] = max(emo["disgust"], emotion["disgust"])
        emotion["anger"] = max(emo["anger"], emotion["anger"])

    Keymax = max(emotion, key=lambda x: emotion[x])
    return Keymax
