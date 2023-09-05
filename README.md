# FPL-minileague-dashboard

![image](https://github.com/eryk0wski/FPL-minileague-dashboard/assets/121037666/63321d47-0d85-4b6a-a55e-d824c99c8306)

## About Project

It is small, easy to deploy web-app dashboard.
Its main target is to make your fantasy fpl mini-league experience more enjoable. 
Dashboard consists of 3 tables and 2 pie charts. First table shows overall best managers in your mini league with total points and overall rank among all of the players.
The second one shows the last gameweek performance and the third shows how the chip situation looks like across the players.
First pie chart shows the captain percent ownership and the second one shows goalkeepers percent ownership.

## Screenshots

Few chosen - not all -  of the graphs and dataframes in the app.

![image](https://github.com/eryk0wski/FPL-minileague-dashboard/assets/121037666/97b363f3-e3f5-471c-b6b8-d25444c18c4f)

![image](https://github.com/eryk0wski/FPL-minileague-dashboard/assets/121037666/2a8d2e6f-61fe-43cd-8168-3bf900e5f27f)

![image](https://github.com/eryk0wski/FPL-minileague-dashboard/assets/121037666/85b218bd-dc4b-4793-9360-f38bc237f9fd)


## Project implementation
You can look up one of the implementations for my fpl mini league under the link:
https://fantasy-dashboard-a4e1d12920e7.herokuapp.com/

## Usage
To run the app locally you need to type in the the cmd in your project folder:

    streamlit run fantasy_dashboard.py
 In case of blocked port you could change port manually by typing:
		
    streamlit run fantasy_dashboard.py --server.port 8503

## Instalation
For dashboard to work you need to first install libraries used in the project.
The recomended way to do this is to use `pip`

    pip install numpy
    pip install pandas
    pip install plotly
    pip install streamlit

 ## Configuration for your mini league
To configure the app for your mini league it is necessary to:

1. Change `classicleague_number` to id of your mini league, it can be found in the url
in your mini-league tab e.g.: `https://fantasy.premierleague.com/leagues/615541/standings/c`
1. Change `player_id_number` to id of random player in your league - it can be you, if you are in the league you want to create dashboard to.
1. Change prize values for prize values in your mini-league or it you don't have any change the values for 0 or just comment full section. 
1. Change real name changing loop for real names or your mates or just comment the section.
