from pushbullet import Pushbullet
import requests
from datetime import datetime

with open('bullet_api_token.txt', 'r') as file:
    bullet_api_token = file.read().strip()

with open('fact_api_token.txt', 'r') as file:
    fact_api_token = file.read().strip()

current_date = datetime.now()
formatted_date = f"{current_date.strftime('%B')}, {current_date.day}, {current_date.year}"
limit = 1
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': f"{fact_api_token}"})
if response.status_code == requests.codes.ok:
    text=response.text[11:len(response.text)-3]
else:
    text="Error:"+ response.status_code+ ""+ response.text

heading="Fact of the day for "+ formatted_date +":"
pb=Pushbullet(f"{bullet_api_token}")
push=pb.push_note(heading ,text)