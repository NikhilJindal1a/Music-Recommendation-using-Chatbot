import json
import os, random
from dotenv import load_dotenv
import requests

load_dotenv()

apikey = os.environ.get("X-RapidAPI-Key")
host = os.environ.get("X-RapidAPI-Host")
url = "https://spotify23.p.rapidapi.com/playlist_tracks/"

querystring = {"id":"37i9dQZF1DWXJfnUiYjUKT","offset":"0","limit":"8"}

headers = {
	"X-RapidAPI-Key": apikey,
	"X-RapidAPI-Host": host
}

def get_latest_releases():
  response = requests.get(url, headers=headers, params=querystring)
  data = response.json()
  tracks = data["items"]
  latest_releases = []
  for track in tracks:
    latest_releases.append(track["track"]["id"])
  return latest_releases

