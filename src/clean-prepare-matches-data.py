import pandas as pd


def get_ties_matches():
    try:
        dt_tied_matches = pd.read_csv("../data/originalDataset.csv")
        filtered_df = dt_tied_matches[dt_tied_matches['Winner'] == 'tied']

        # Contar empates por time
        team_tied_counts = filtered_df.melt(
            id_vars=['Winner'],
            value_vars=['Team 1', 'Team 2'],
            value_name='team'
        )['team'].value_counts().reset_index()

        team_tied_counts.columns = ['teams', 'tied_matches']
        return team_tied_counts

    except Exception as e:
        raise f"Eroor to read csv file: {e}"


class CleanPrepareMatchesData:
    def __init__(self, dt_matches: pd.DataFrame):
        self.dt_matches = dt_matches

    def calc_total_matches(self):
        print("filtering the dataframe per teams")
        df_matches_teams = self.dt_matches.filter(regex='^Team 1_|^Team 2_')

        # Criando um dicionário para contar o total de jogos por time
        total_matches = {}

        # Iterando sobre as colunas de jogos e somando os valores
        for col in df_matches_teams:
            # Extraindo o nome do time (após 'Team 1_' ou 'Team 2_')
            time = col.split('_')[1]

            # Adicionando o valor de cada time ao total de jogos
            if time in total_matches:
                total_matches[time] += df_matches_teams[col].sum()
            else:
                total_matches[time] = df_matches_teams[col].sum()

        # Transformando o dicionário em um DataFrame
        total_matches_df = pd.DataFrame(list(total_matches.items()), columns=['Teams', 'Total Matches'])

        total_matches_number = total_matches_df["Total Matches"].sum()
        print(f"Total Matches {total_matches_number}")

        return total_matches_df

    def cal_win_loss_ties_per_team(self, total_matches):
        print("Counting wins, losses, and ties per team...")

        # Filtra apenas as colunas que indicam vencedores
        df_winners = self.dt_matches.filter(regex='^Winner_')

        # Contando o número de vitórias para cada país (somando os 1's)
        total_wins = df_winners.sum()

        # Transformando os resultados em um DataFrame para organização
        total_stats_df = total_wins.reset_index()
        total_stats_df.columns = ['Team', 'Total Wins']

        # Removendo o prefixo 'Winner_' do nome das equipes
        total_stats_df['Team'] = total_stats_df['Team'].str.replace('Winner_', '', regex=False)

        total_tied_teams = get_ties_matches()

        # Mesclando os DataFrames
        merged_matches_df = pd.merge(
            total_stats_df,  # DataFrame principal
            total_tied_teams,  # DataFrame com empates
            left_on='Team',  # Coluna no total_stats_df
            right_on='teams',  # Coluna no team_counts
            how='left'  # Tipo de junção (left join para manter todos os times do total_stats_df)
        )

        # Remover a coluna 'teams' duplicada, se necessário
        merged_matches_df.drop(columns=['teams'], inplace=True)

        return merged_matches_df




if __name__ == "__main__":
    get_ties_matches()

