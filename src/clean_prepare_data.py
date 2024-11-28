import pandas as pd


def get_ties_matches():
    try:
        # loading and preparing data per match tied
        dt_tied_matches = pd.read_csv("../data/originalDataset.csv")
        filtered_df = dt_tied_matches[dt_tied_matches['Winner'] == 'tied']

        # counting tied matches per team
        team_tied_counts = filtered_df.melt(
            id_vars=['Winner'],
            value_vars=['Team 1', 'Team 2'],
            value_name='team'
        )['team'].value_counts().reset_index()

        # Redefining the dataframe columns name.
        team_tied_counts.columns = ['Teams', 'Total Tieds']
        return team_tied_counts

    except Exception as e:
        print(f"Error processing tied matches: {e}")
        raise


class CleanPrepareMatchesData:
    def __init__(self, dt_matches: pd.DataFrame):
        self.dt_matches = dt_matches

    def calc_total_matches(self):

        print("Calculating total matches per team")

        # filtering the dataframe per teams
        df_matches_teams = self.dt_matches.filter(regex='^Team 1_|^Team 2_')

        # Calculating total matches per team
        total_matches = {}

        for col in df_matches_teams:
            time = col.split('_')[1]

            if time in total_matches:
                total_matches[time] += df_matches_teams[col].sum()
            else:
                total_matches[time] = df_matches_teams[col].sum()

        total_matches_df = pd.DataFrame(list(total_matches.items()), columns=['Teams', 'Total Matches'])

        # Geting Total Ties matches
        total_tied_teams = get_ties_matches()

        # Merging tied matches and total matches
        merged_df = pd.merge(total_matches_df, total_tied_teams, on='Teams', how='left')
        merged_df['Total Tieds'] = merged_df['Total Tieds'].fillna(0).astype(int)

        # Recalculating total matches and cleaning the total tieds column
        merged_df['Total Matches'] = merged_df['Total Matches'] + merged_df['Total Tieds']
        merged_df.drop(['Total Tieds'], axis=1, inplace=True)

        total_matches_number = merged_df["Total Matches"].sum()
        print(f"Total Matches calculated: {total_matches_number}")
        print(f"Total matches per team: {merged_df}")

        return merged_df

    def cal_win_loss_ties_per_team(self, total_matches):
        print("Counting wins, losses, and ties per team...")

        print("Getting the winners column")
        df_winners = self.dt_matches.filter(regex='^Winner_')

        print("Summarizing the total of wins per team.")
        total_wins = df_winners.sum()

        # reorganizing and renaming the dataframe
        total_stats_df = total_wins.reset_index()
        total_stats_df.columns = ['Team', 'Total Wins']
        total_stats_df['Teams'] = total_stats_df['Team'].str.replace('Winner_', '', regex=False)

        # Calculating total matches tied per team
        total_tied_teams = get_ties_matches()

        # Joing the dataframes per team
        merged_matches_df = pd.merge(
            total_stats_df,  # original dataframe
            total_tied_teams,  # dataframe with ties matches per team
            left_on='Teams',  # column in total_stats_df
            right_on='Teams',  # column in total_tied_teams
            how='left'  # type of join
        )

        # Dealing with the tied numbers that are nan, due the teams that didn't had an tied match
        merged_matches_df['Total Tieds'] = merged_matches_df['Total Tieds'].fillna(0).astype(int)

        # Removing teams duplicate column
        merged_matches_df.drop(columns=['Team'], inplace=True)

        # Calculing total losses
        merged_matches_df['Total Losses'] = total_matches['Total Matches'] - (
                merged_matches_df['Total Wins'] + merged_matches_df['Total Tieds']
        )

        return merged_matches_df

    def cal_total_matches_home_away_played(self, total_matches, dt_matches_home_away):

        # Inicializando dicionários para contagem de jogos em casa e fora
        home_games = {team: 0 for team in total_matches['Teams']}
        away_games = {team: 0 for team in total_matches['Teams']}

        # Iterando sobre o DataFrame de partidas
        for _, row in dt_matches_home_away.iterrows():
            # Verificando para o Time 1
            if row['Host_Country'] == row['Team 1'] and row['Venue_Team1'] == 'Home':
                home_games[row['Team 1']] += 1  # Time 1 jogou em casa
            else:
                away_games[row['Team 1']] += 1  # Time 1 jogou fora

            # Verificando para o Time 2
            if row['Host_Country'] == row['Team 2'] and row['Venue_Team2'] == 'Home':
                home_games[row['Team 2']] += 1  # Time 2 jogou em casa
            else:
                away_games[row['Team 2']] += 1  # Time 2 jogou fora

        # Criando um DataFrame com as contagens de jogos em casa e fora
        games_data = {
            'Teams': list(home_games.keys()),
            'Home Games': list(home_games.values()),
            'Away Games': list(away_games.values())
        }

        games_df = pd.DataFrame(games_data)

        # Exibindo o DataFrame com os resultados
        print(games_df)
        return games_df

