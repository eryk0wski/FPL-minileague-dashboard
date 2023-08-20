# FPL-minileague-dashboard

![image](https://github.com/eryk0wski/FPL-minileague-dashboard/assets/121037666/63321d47-0d85-4b6a-a55e-d824c99c8306)

## About Project

It is small, easy to deploy web-app dashboard.
Its main target is to make your fantasy fpl mini-league experience more enjoable. 
Dashboard consists of 3 tables and 2 pie charts. First table shows overall best managers in your mini league with total points and overall rank among all of the players.
The second one shows the last gameweek performance and the third shows how the chip situation looks like across the players.
First pie chart shows the captain percent ownership and the second one shows goalkeepers percent ownership.

## Usage
To run the app locally you need to type in the the cmd in your project folder:

    `streamlit run fantasy_dashboard.py`
 In case of blocked port you could change port manually by typing:
		
    `streamlit run fantasy_dashboard.py --server.port 8503`

## Instalation
For dashboard to work you need to first install libraries used in the project.
The recomended way to do this is to use `pip`

    `pip install numpy`
    `pip install pandas`
    `pip install plotly`
    `pip install streamlit`
    

