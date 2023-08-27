class Pickstat:
    def __init__(self) -> None:
        pass

    def pick_stats(self):
        """Pick which stat to compare between the players"""
        choice = input("\nChoose a statistic to compare between the players:\n\
        Individual Player Efficiency               - IPF\n\
        Effective Field Goal Percentage            - EFG\n\
        True Shooting Percentage                   - TS\n").upper().strip()
        if choice == 'IPF':
            return 'individual_player_efficiency' 
        elif choice == 'EFG':
            return 'effective_field_goal_percentage'
        elif choice == 'TS':
            return 'true_shooting_percentage'
     
    def individual_player_efficiency(self, player1, player2, player1_season, player2_season):
     """Prints which player had the higher individual player efficiency"""
     player1_eff = (player1.PTS + player1.REB + player1.AST + player1.STL + player1.BLK - (player1.FGA - player1.FGM) - (player1.FTA - player1.FTM) - player1.TOV) / player1.GP
     player2_eff = (player2.PTS + player2.REB + player2.AST + player2.STL + player2.BLK - (player2.FGA - player2.FGM) - (player2.FTA - player2.FTM) - player2.TOV) / player2.GP
     player1_eff = round(float(player1_eff.item()), 3)
     player2_eff = round(float(player2_eff.item()), 3)
     if player1_eff > player2_eff:
        print(f"{player1.PLAYER[0]}: {player1_eff:.3f} in {player1_season} had a higher player efficiency than {player2.PLAYER[0]}: {player2_eff:.3f} in {player2_season}.")
     else:
        print(f"{player2.PLAYER[0]}: {player2_eff:.3f} in {player2_season} had a higher player efficiency than {player1.PLAYER[0]}: {player1_eff:.3f} in {player1_season}.")

    def true_shooting_percentage(self, player1, player2, player1_season, player2_season):
        """Prints which player had the higher true shooting percentage"""
        player1_ts = (player1.PTS /(2 * (player1.FGA + (0.44 * player1.FTA)))) * 100
        player2_ts = (player2.PTS /(2 * (player2.FGA + (0.44 * player2.FTA)))) * 100
        player1_ts = round(float(player1_ts.item()), 3)
        player2_ts = round(float(player2_ts.item()), 3)
        if player1_ts > player2_ts:
            print(f"{player1.PLAYER[0]}: {player1_ts:.3f}% in {player1_season} had a higher true shooting percentage than {player2.PLAYER[0]}: {player2_ts:.3f}% in {player2_season}.")
        else:
            print(f"{player2.PLAYER[0]}: {player2_ts:.3f}% in {player2_season} had a higher true shooting percentage than {player1.PLAYER[0]}: {player1_ts:.3f}% in {player1_season}.")

    def effective_field_goal_percentage(self, player1, player2, player1_season, player2_season):
        """Prints which player had the higher field goal percentage"""
        player1_efg = ((player1.FGM + (0.5 * player1.FG3M)) / player1.FGA) * 100
        player2_efg = ((player2.FGM + (0.5 * player2.FG3M)) / player2.FGA) * 100
        player1_efg = round(float(player1_efg.item()), 3)
        player2_efg = round(float(player2_efg.item()), 3)
        if player1_efg > player2_efg:
            print(f"{player1.PLAYER[0]}: {player1_efg:.3f}% in {player1_season} had a higher true shooting percentage than {player2.PLAYER[0]}: {player2_efg:.3f}% in {player2_season}.")
        else:
            print(f"{player2.PLAYER[0]}: {player2_efg:.3f}% in {player2_season} had a higher true shooting percentage than {player1.PLAYER[0]}: {player1_efg:.3f}% in {player1_season}.")
