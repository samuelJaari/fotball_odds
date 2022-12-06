import requests

standings_url ="https://fbref.com/en/comps/9/Premier-League-Stats"

data= requests.get(standings_url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(data.text)

standings_table = soup.select('table.stats_table')[0]


links = standings_table.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if '/squads/' in l]
team_urls = [f"https://fbref.com{l}" for l in links]

team_arsenal = team_urls[0]
data2 = requests.get(team_arsenal)

import pandas as pd

games = pd.read_html(data2.text, game="Scores & Fixtures")

games