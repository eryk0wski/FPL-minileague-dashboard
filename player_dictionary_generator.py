import json
import requests

URL = 'https://fantasy.premierleague.com/api/bootstrap-static/'
page = requests.get(URL)
data = json.loads(page.text)

id = []
name = []

for i in range(data['elements']):
    id.append(data['elements'][i]['id'])
    name.append(data['elements'][i]['web_name'])

players_dict = dict(zip(id,name))

with open('fpl_pd.json'.format(1), 'w', encoding='utf-8') as file:
    json.dump(players_dict, file, ensure_ascii=False)


