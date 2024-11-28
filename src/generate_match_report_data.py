import pandas as pd
from src.clean_prepare_data import CleanPrepareMatchesData


def generate_match_report_data():

    try:
        # Loading data and functions
        dt_matches = pd.read_csv("../data/CategoricalDataset.csv")
        dt_matches_home_away = pd.read_csv("../data/ContinousDataset.csv")
        clean_prepared_data = CleanPrepareMatchesData(dt_matches)

        # Calculating total matches per team
        total_matches = clean_prepared_data.calc_total_matches()

        # Calculating total Wins, Loss and Ties
        total_wins_loss_ties = clean_prepared_data.cal_win_loss_ties_per_team(total_matches)

        # Calculating total home away matches per times
        total_home_away_matches = clean_prepared_data.\
            cal_total_matches_home_away_played(total_matches, dt_matches_home_away)

        # merging all calcutations
        merged_df = total_matches.merge(total_wins_loss_ties, on='Teams', how='inner') \
            .merge(total_home_away_matches, on='Teams', how='inner')

        print(merged_df.head(5))

        merged_df.to_csv('../data/match_report_data.csv', index=False)

    except Exception as e:
        print(f"Error generating matches report: {e}")
        raise


if __name__ == "__main__":
    generate_match_report_data()
