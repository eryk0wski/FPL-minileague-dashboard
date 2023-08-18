import streamlit as st
import pandas as pd
import requests
import json
import numpy as np

#league number
classicleague_number = 615541
URL = 'https://fantasy.premierleague.com/api/leagues-classic/' + str(classicleague_number) + '/standings/'
page = requests.get(URL)
data = json.loads(page.text)

#league data - upade day and hour and league name
league_name = data['league']['name']
last_update = data['last_updated_data'][0:10]
last_update_hour = data['last_updated_data'][11:16]
league_table = pd.DataFrame(data = data['standings']['results'])
league_table.columns.to_list()
league_table = league_table.drop(columns = ['rank_sort'])



overall_rank = []
team_value = []
lists = {
    'wildcard': [],
    '3xc': [],
    'bboost': [],
    'freehit': []
}
possible_chips = ['3xc','wildcard','freehit', 'bboost']

#very funky code that checks for wildcards avalible for each player and their overall_rank and team value

for entry in league_table['entry']:
  manager_url = 'https://fantasy.premierleague.com/api/entry/'+ str(entry) +'/history'
  manager_site = requests.get(manager_url)
  manager_profile = json.loads(manager_site.text)
  overall_rank.append(manager_profile['current'][0]['overall_rank'])
  team_value.append(manager_profile['current'][0]['value'])
  if len(manager_profile['chips']) == 0:
    lists['bboost'].append('Dostepny')
    lists['3xc'].append('Dostepny')
    lists['freehit'].append('Dostepny')
    lists['wildcard'].append('Dostepny')
  elif len(manager_profile['chips']) == 1:
    for string in possible_chips:
      if string == manager_profile['chips'][0]['name'] :
        lists[string].append('Niedostepny')
      else:
        lists[string].append('Dostepny')
  elif len(manager_profile['chips']) > 1 :
    for i in range(len(manager_profile['chips']) - 1):
      for string in possible_chips:
        if string == manager_profile['chips'][i]['name'] :
          lists[string].append('Niedostepny')
        else:
          lists[string].append('Dostepny')


team_value = np.array(team_value) / 10

league_table['overall_rank'] = overall_rank
league_table['team_value'] = team_value
league_table['bench_boost'] = lists['bboost']
league_table['wildcard'] = lists['wildcard']
league_table['free_hit'] = lists['freehit']
league_table['tripple_captain']= lists['3xc']



league_table = league_table.drop(columns = ['id','entry'])
league_table['rank_change'] = league_table['last_rank'] - league_table['rank']
league_table = league_table.rename(columns = {"event_total":"gw_points", "total":"total_points","entry_name":"team_name"})

#tried changing font colour to green if rank progress and red if you deranked
#rank_change = []
#for rank in league_table['rack_change']:
#  if rank >= 0:
#    rank_change.append('green:[' + str(rank) + ']')
#  else:
#    rank_change.append('red:[' + str(rank) + ']')
#league_table['rank_change'] = rank_change

# change columns order
league_table = league_table[['rank','rank_change','player_name', 'gw_points', 'last_rank', 'total_points', 'team_name', 'overall_rank', 'team_value', 'bench_boost', 'wildcard', 'free_hit', 'tripple_captain']]
players = []

#changing nick to real name if they specify otherwise
for player in league_table['player_name']:
  if player == 'SOJA SOJA':
    players.append("Kuba Sojka")
  elif player == 'Pisula One':
    players.append('Hubert Goc')
  else:
    players.append(player)

#adding prize money winning to our mini league (due * amount_of_players*winning share ( 50% winner, 30% second place, 20% third place)
prize1 = 50*10*0.5
prize2 = 50*10*0.3
prize3 = 50*10*0.2

#adding prizes
prizes = []
for i in range(len(league_table['rank'])):
  if i == 0:
    prizes.append(int(prize1))
  elif i == 1:
    prizes.append(int(prize2))
  elif i == 2:
    prizes.append(int(prize3))
  else:
    prizes.append(int(0))

league_table['player'] = players
league_table['prize'] = prizes

URLfunny = 'https://fantasy.premierleague.com/api/bootstrap-static/'
page_players = requests.get(URLfunny)
data_players = json.loads(page_players.text)
amount_of_players =  data_players['total_players']
league_table['top_percent[%]'] = round((100 *  league_table['overall_rank']) / amount_of_players ,1)

winner_table = league_table[['rank','rank_change','player','team_name','total_points','prize']]
teams_table = league_table[['player','gw_points','overall_rank','bench_boost', 'wildcard', 'free_hit', 'tripple_captain']]

#######################################################STREAMLIT#############################################################################3

header = st.container()
dataset = st.container()
team_stats = st.container()

def color_survived(val):
    color = '#59eb00' if val == 'Dostepny' else '#EE4B2B'
    return f'background-color: {color}'



def highlight_winners(s):
    return ['background-color: #59eb00']*len(s) if s.prize> 0 else ['background-color: #FFFFFF']*len(s)


with header:
    st.title('FPL mini-league dashboard')
    st.text("Test site for our mini league")
    st.text("Last updated: " + last_update + ' ' + last_update_hour)
    st.divider()

with st.sidebar:
    st.write("***FPL mini-league dashboard***")
    st.write("version 0.1.0 18.08.2023")
    league_url = ":soccer:[FPL mini-league link](https://fantasy.premierleague.com/leagues/" + str(classicleague_number) + "/standings/c):soccer:"
    st.write(league_url)
    st.write(":smiling_imp:[Creators github](https://github.com/eryk0wski):smiling_imp:")
    st.write("Thats fully customizable minileague dashboard \n. You can use it freely, just ")
    
    
    
    
with dataset:
    st.title('Winners table')
    st.dataframe(winner_table.head(11).style.apply(highlight_winners, axis=1))
    st.divider()

with team_stats:
    st.title('Team stats')
    st.dataframe(teams_table.style.applymap(color_survived, subset=['bench_boost', 'wildcard', 'free_hit', 'tripple_captain']))

