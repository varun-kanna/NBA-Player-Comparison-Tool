import pandas as pd
import requests
pd.set_option("display.max_columns", None) # so we can see all the columns in a wide DataFrame
import time
import numpy as np

headers =  {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Host": "stats.nba.com",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

def pick_stats():
        choice = input("\nChoose a statistic to compare between the players:\n\
        Individual Player Efficency                - EFF\n\
        Effective Field Goal Percentage            - EFG\n\
        True Shooting Percentage                   - TS\n").upper().strip()
                        
        if choice == 'EFF':
            return 'individual_player_efficiency' 
        elif choice == 'UR':
            return 'usage_rate' 
        elif choice == 'EFG':
            return 'effective_field_goal_percentage'
        elif choice == 'TS':
            return 'true_shooting_percentage'
        
def individual_player_efficiency(player1, player2, player1_season, player2_season):
     player1_eff = (player1.PTS + player1.REB + player1.AST + player1.STL + player1.BLK - (player1.FGA - player1.FGM) - (player1.FTA - player1.FTM) - player1.TOV) / player1.GP
     player2_eff = (player2.PTS + player2.REB + player2.AST + player2.STL + player2.BLK - (player2.FGA - player2.FGM) - (player2.FTA - player2.FTM) - player2.TOV) / player2.GP
     player1_eff = round(float(player1_eff.item()), 3)
     player2_eff = round(float(player2_eff.item()), 3)
     if player1_eff > player2_eff:
        print(f"{player1.PLAYER[0]}: {player1_eff:.3f} in {player1_season} had a higher player efficiency than {player2.PLAYER[0]}: {player2_eff:.3f} in {player2_season}.")
     else:
        print(f"{player2.PLAYER[0]}: {player2_eff:.3f} in {player2_season} had a higher player efficiency than {player1.PLAYER[0]}: {player1_eff:.3f} in {player1_season}.")

def true_shooting_percentage(player1, player2, player1_season, player2_season):
     player1_ts = (player1.PTS /(2 * (player1.FGA + (0.44 * player1.FTA)))) * 100
     player2_ts = (player2.PTS /(2 * (player2.FGA + (0.44 * player2.FTA)))) * 100
     player1_ts = round(float(player1_ts.item()), 3)
     player2_ts = round(float(player2_ts.item()), 3)
     if player1_ts > player2_ts:
        print(f"{player1.PLAYER[0]}: {player1_ts:.3f}% in {player1_season} had a higher true shooting percentage than {player2.PLAYER[0]}: {player2_ts:.3f}% in {player2_season}.")
     else:
        print(f"{player2.PLAYER[0]}: {player2_ts:.3f}% in {player2_season} had a higher true shooting percentage than {player1.PLAYER[0]}: {player1_ts:.3f}% in {player1_season}.")

def effective_field_goal_percentage(player1, player2, player1_season, player2_season):
     player1_efg = ((player1.FGM + (0.5 * player1.FG3M)) / player1.FGA) * 100
     player2_efg = ((player2.FGM + (0.5 * player2.FG3M)) / player2.FGA) * 100
     player1_efg = round(float(player1_efg.item()), 3)
     player2_efg = round(float(player2_efg.item()), 3)
     if player1_efg > player2_efg:
        print(f"{player1.PLAYER[0]}: {player1_efg:.3f}% in {player1_season} had a higher true shooting percentage than {player2.PLAYER[0]}: {player2_efg:.3f}% in {player2_season}.")
     else:
        print(f"{player2.PLAYER[0]}: {player2_efg:.3f}% in {player2_season} had a higher true shooting percentage than {player1.PLAYER[0]}: {player1_efg:.3f}% in {player1_season}.")

def main_menu():
    print("Lets compare NBA players' stats!")
    condition = True
    while condition:
        # If we want stats from the Playoffs or the Regular Season
        print(f"Please enter the details of the first player")
        player1_season = str(input("Enter NBA Season (ex: '2022-23'): "))
        player1_season_type = str(input("Do you want to see Playoff Stats (p) or Regular Season stats (r): \n"))
        if player1_season_type == "p":
            player1_season_type = "Playoffs"
        else:
           player1_season_type = "Regular Season"
        player1 = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+player1_season+'&SeasonType='+player1_season_type+'&StatCategory=PTS'
        player1_input = input("Input the player's stats you want to see (Case Sensitive): ")

        print(f"\nPlease enter the details of the second player")
        player2_season = str(input("Enter NBA Season (ex: '2022-23'): "))
        player2_season_type = str(input("Do you want to see Playoff Stats (p) or Regular Season stats (r): \n"))
        if player2_season_type == "p":
            player2_season_type = "Playoffs"
        else:
           player2_season_type = "Regular Season"
        player2 = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+player2_season+'&SeasonType='+player2_season_type+'&StatCategory=PTS'
        player2_input = input("Input the player's stats you want to see (Case Sensitive and Space Sensitive): ")
        print("Initializing data...")

        players = [[player1, player1_input],[player2, player2_input]]
        players_df = {}
        for p in players:
            player = p[0]
            player_input = p[1]
            lag = np.random.uniform(low=5, high=10)
            time.sleep(lag)
            # Setting up the DataFrame
            r = requests.get(url=player, headers=headers).json()
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

        player1 = players_df[player1_input]
        player2 = players_df[player2_input]
        print(player1)
        print(player2)

        i = pick_stats()
        if i == "individual_player_efficiency":
            individual_player_efficiency(player1, player2, player1_season, player2_season)
        if i == "true_shooting_percentage":
            true_shooting_percentage(player1, player2, player1_season, player2_season)
        if i == "effective_field_goal_percentage":
            effective_field_goal_percentage(player1, player2, player1_season, player2_season)

        y_n = str(input("Would you like to continue? 'yes'/'no': "))
        print()
        print()
        if y_n.lower() == "no":
            condition = False

if __name__ == "__main__":
    main_menu()