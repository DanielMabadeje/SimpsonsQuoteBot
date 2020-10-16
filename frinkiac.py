import schedule
import requests
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException

account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token  = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
client = TwilioRestClient(account_sid, auth_token)def get_quote():
    r = requests.get("https://frinkiac.com/api/random")
    if r.status_code == 200:
        json = r.json()
        # Extract the episode number and timestamp from the API response
        # and convert them both to strings.
        timestamp, episode, _ = map(str, json["Frame"].values())

        image_url = "https://frinkiac.com/meme/" + episode + "/" + timestamp
        # Combine each line of subtitles into one string.
        caption = "\n".join([subtitle["Content"] for subtitle in json["Subtitles"]])
        return image_url, caption 