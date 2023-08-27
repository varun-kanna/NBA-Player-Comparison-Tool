import re
import time
from header import h
import numpy as np
import pandas as pd
import requests
pd.set_option("display.max_columns", None)

class Player:
    def __init__(self) -> None:
        pass

    def season(self):
        condition = True
        while condition:
            season = (input("Enter NBA Season (ex: '2022-23'): "))
            if len(season) > 7:
                return "Invalid season type, try again"
            pattern = r"^\d{4}-\d{2}$"
            if re.match(pattern, season):
                condition = False
                return season
            else:
                print("Incorrect year type, please try again")

    def season_type(self):
        condition = True
        while condition:
            season_type = (input("Do you want to see Playoff Stats (p) or Regular Season stats (r): \n"))
            if season_type== "p":
                condition = False
                return "Playoffs"
            elif season_type== "r":
                condition = False
                return "Regular Season"
            else:
                print("Incorrect year type, please try again")
                continue
    def generate_player(self, season, season_type):
        return 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+season+'&SeasonType='+season_type+'&StatCategory=PTS' 

    def actual_player(self):
        while True:
            player = input("Input the player's stats you want to see (Case Sensitive): ")
            condition = input("Is this the correct player? type 'y' or 'n': ")
            if condition == "y":
                return player
            else:
                continue
    def generate_player_dataframes(self, players):
        players_df = {}
        for p in players:
            player = p[0]
            player_input = p[1]
            lag = np.random.uniform(low=5, high=10)
            time.sleep(lag)
            # Setting up the DataFrame
            r = requests.get(url=player, headers=h).json()
            table_headers = r["resultSet"]["headers"]
            #Looking through all the available players to find the player we chose
            specific_player = ""
            for i in (r["resultSet"]["rowSet"]):
                if player_input in i:
                    specific_player = i  
            #Checking whether the player chosen is valid
            if not (specific_player):
                print("Sorry, your player of choice didn't play this year, or wasn't in the playoffs this year")
            else:
                players_df[player_input] = pd.DataFrame([specific_player], columns=table_headers)
        return players_df


if __name__ == "__main__":
    p = Player()
    p.actual_player()
