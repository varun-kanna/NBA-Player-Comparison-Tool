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


# This either runs the script or not
condition = True
y_n = input("Hello, would you like to see stats for any player from any year? 'yes' or 'no': ")
if y_n.lower() == "no":
    condition = False
if y_n.lower() == "true":
    condition = True

while condition:
    # If we want stats from the Playoffs or the Regular Season
    y = str(input("Enter NBA Season (ex: '2022-23'): "))
    s = str(input("Do you want to see Playoff Stats or Regular Season stats\n'Regular Season' or 'Playoffs': "))
    test_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+y+'&SeasonType='+s+'&StatCategory=PTS'
    lag = np.random.uniform(low=5, high=30)
    time.sleep(lag)

    # Setting up the DataFrame
    r = requests.get(url=test_url, headers=headers).json()
    table_headers = r["resultSet"]["headers"]
    pd.DataFrame(r["resultSet"]["rowSet"], columns=table_headers)

    temp_df1 = pd.DataFrame(r["resultSet"]["rowSet"], columns=table_headers)

    temp_df2 = pd.DataFrame({"Year": [y for i in range((len(temp_df1)))],
                            "Season_type": [s for i in range((len(temp_df1)))]})
    
    #The final DataFrame
    temp_df3 = pd.concat([temp_df2, temp_df1], axis=1)

    #Looking through all the available players to find the player we chose
    specific_player = None
    player_input = input("Input the player's stats you want to see (Case Sensitive): ")
    for i in (r["resultSet"]["rowSet"]):
        if player_input in i:
            specific_player = i  
            k = pd.DataFrame(i)

    #Checking whether the player chosen is valid
    if not (specific_player):
        print("Sorry, your player of choice didn't play this year, or wasn't in the playoffs this year")
    else:
        df5 = pd.DataFrame([specific_player], columns=table_headers)
        print(df5)

    yes_no = str(input("Would you like to continue? 'yes'/'no': "))
    print()
    print()
    if yes_no.lower() == "no":
        condition = False