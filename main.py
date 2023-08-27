from pickstat import Pickstat
from player import Player
from header import h

headers = h
pickstat = Pickstat()
player = Player()

def main_menu():
    print("Lets compare NBA players' stats!\n")
    condition = True
    while condition:
        # First player's stats
        player1 = Player()
        player1_season = player1.season()
        player1_season_type = player1.season_type()
        player1_link = player1.generate_player(player1_season, player1_season_type)
        player1_input = player1.actual_player()

        # Second player's stats
        player2 = Player()
        player2_season = player2.season()
        player2_season_type = player2.season_type()
        player2_link = player2.generate_player(player2_season, player2_season_type)
        player2_input = player2.actual_player()
        print("Initializing data...")
        print()
        players = [[player1_link, player1_input],[player2_link, player2_input]]
        
        # Generate dataframes for each player
        dataframes = player.generate_player_dataframes(players)
        player1, player2 = dataframes[player1_input], dataframes[player2_input]
        print(f"Stats for {player1.PLAYER[0]}:\n {player1} in the {player1_season}")
        print()
        print(f"Stats for {player2.PLAYER[0]}:\n {player2} in the {player2_season}")

        # Pick which stat to compare between the players
        i = pickstat.pick_stats()
        if i == "individual_player_efficiency":
            pickstat.individual_player_efficiency(player1, player2, player1_season, player2_season)
        if i == "true_shooting_percentage":
            pickstat.true_shooting_percentage(player1, player2, player1_season, player2_season)
        if i == "effective_field_goal_percentage":
            pickstat.effective_field_goal_percentage(player1, player2, player1_season, player2_season)

        y_n = str(input("Would you like to continue? 'yes'/'no': "))
        print()
        print()
        if y_n.lower() == "no":
            condition = False

if __name__ == "__main__":
    main_menu()