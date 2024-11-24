import pandas as pd
from src.generate_match_report import CleanPrepareMatchesData

def generate_match_report():

    print("#### Generating match reports ####")
    try:
        dt_matches = pd.read_csv("../data/CategoricalDataset.csv")

        total_matches = CleanPrepareMatchesData(dt_matches).calc_total_matches()
        total_wins_loss_ties = CleanPrepareMatchesData(dt_matches).cal_win_loss_ties_per_team(total_matches)

        print(total_matches)

    except Exception as e:
        raise f"Eroor to read csv file: {e}"


if __name__ == "__main__":
    get_ties_matches()
