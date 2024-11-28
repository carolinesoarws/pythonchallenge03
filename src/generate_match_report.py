import pandas as pd
import numpy as np
from tabulate import tabulate


def generate_match_report():
    """
    This function processes multiple datasets to generate detailed match reports for the Indian team.
    It includes statistical analyses of team performance, including win, loss,
    and tie percentages, as well as home/away
    performance breakdowns. Additionally, the function calculates average margins of victory
    or defeat, and analyzes India's
    performance against specific teams and grounds.

    The following reports are generated:
    1. **India's overall statistics** (win, loss, tie percentages, home/away performance).
    2. **Matches played by India against other teams**.
    3. **Match statistics** such as average win/loss by runs per year.
    4. **Analysis of most played grounds for India, both home and away**.

    """
    print("##################################")
    print("#### Generating match reports ####")
    print("##################################\n")

    try:
        # Load the match report data for India
        df_matches_report_data = pd.read_csv("../data/match_report_data.csv")

        # Filter the data for India and make a copy for further manipulation
        india_stats = df_matches_report_data[df_matches_report_data['Teams'] == 'India'].copy()

        # Calculate total wins, losses, ties percentages for India
        calc_total_win_loss_tie_india_percentage(india_stats)
        # Calculate total wins, losses, ties  for India Team in home an away matches.
        calc_total_home_away_percentage(india_stats)

        # Load continuous dataset to calculate the next 3 steps
        df_total_matches_team = pd.read_csv("../data/ContinousDataset.csv")

        # Analyze matches played by India against other teams
        calc_total_matches_india_played_per_team(df_total_matches_team)

        # Analyze India's wins and losses against various teams
        calc_total_india_wins_losses(df_total_matches_team)

        # Identify most played home and away grounds for India
        calc_most_played_matches_grounds_india(df_total_matches_team)

        # Load the original dataset to analise and calculate the next function
        df_total_mathes = pd.read_csv("../data/originalDataset.csv")

        # Step 8: Calculate average win/loss by runs per year
        calculate_avg_win_loss_runs(df_total_mathes)

    except Exception as e:
        print(f"Error processing match data: {e}")
        raise


def calc_total_win_loss_tie_india_percentage(df_india_matches: pd.DataFrame):
    """
    This function calculates the total percentage of wins, losses,
    and ties for the Indian team across all their matches.

    Args:
    - df_india_matches (pd.DataFrame): A DataFrame containing
    match statistics for India with columns such as
    'Total Wins', 'Total Losses', and 'Total Tieds'.

    """
    print("#### Total win, loss, percentage for the Team India ####")

    result = {
        "Win Percentage":
            round((df_india_matches['Total Wins'].iloc[0] / df_india_matches['Total Matches'].iloc[0]) * 100),
        "Loss Percentage":
            round((df_india_matches['Total Losses'].iloc[0] / df_india_matches['Total Matches'].iloc[0]) * 100),
        "Tie Percentage":
            round((df_india_matches['Total Tieds'].iloc[0] / df_india_matches['Total Matches'].iloc[0]) * 100)
    }

    # Display the results
    print(f"Wins: {result['Win Percentage']}%")
    print(f"Loss: {result['Loss Percentage']}%")
    print(f"Ties: {result['Tie Percentage']}% \n")


def calc_total_home_away_percentage(df_india_matches: pd.DataFrame):
    """
    This function processes match data to calculate the total percentage of wins, losses, and ties
    for India in both home and away games. It displays these percentages for home and away matches separately.

    Args:
    - df_india_matches (pd.DataFrame): A DataFrame containing statistics for India's matches with columns
      such as 'Home Games', 'Away Games', 'Total Wins', 'Total Losses', and 'Total Tieds'.
    """
    print("#### Total win, loss, percentage in matches Home and Away for the Team India ####")

    result_home_percentage = {
        "Win Percentage": round((df_india_matches['Total Wins'].iloc[0] / df_india_matches['Home Games'].iloc[0]) * 100),
        "Loss Percentage": round((df_india_matches['Total Losses'].iloc[0] / df_india_matches['Home Games'].iloc[0]) * 100),
        "Tie Percentage": round((df_india_matches['Total Tieds'].iloc[0] / df_india_matches['Home Games'].iloc[0]) * 100)
    }

    result_away_percentage = {
        "Win Percentage": round((df_india_matches['Total Wins'].iloc[0] / df_india_matches['Away Games'].iloc[0]) * 100),
        "Loss Percentage": round((df_india_matches['Total Losses'].iloc[0] / df_india_matches['Away Games'].iloc[0]) * 100),
        "Tie Percentage": round((df_india_matches['Total Tieds'].iloc[0] / df_india_matches['Away Games'].iloc[0]) * 100)
    }

    print(f"India's Home Matches Win Percentage: {result_home_percentage['Win Percentage']}%")
    print(f"India's Home Matches Loss Percentage: {result_home_percentage['Loss Percentage']}%")
    print(f"India's Home Matches Tie Percentage: {result_home_percentage['Tie Percentage']}%\n")

    print(f"India's Away Matches Win Percentage: {result_away_percentage['Win Percentage']}%")
    print(f"India's Away Matches Loss Percentage: {result_away_percentage['Loss Percentage']}%")
    print(f"India's Away Matches Tie Percentage: {result_away_percentage['Tie Percentage']}%\n")


def calc_total_matches_india_played_per_team(df_total_matches_team: pd.DataFrame):
    """
    This function filters the dataset to consider matches where India was either 'Team 1' or 'Team 2',
    and then counts the number of matches played against each opponent. The result is displayed as a table
    showing each opponent and the total number of matches India has played against them.

    Args:
    - df_total_matches_team (pd.DataFrame): DataFrame containing the match data with columns such as 'Team 1',
      'Team 2', and 'Winner'.
    """
    print("#### Total matches India played with other teams ####")

    # Filter matches where India is either Team 1 or Team 2
    india_as_team1 = df_total_matches_team[df_total_matches_team['Team 1'] == 'India']
    india_as_team2 = df_total_matches_team[df_total_matches_team['Team 2'] == 'India']
    india_as_winner = df_total_matches_team[df_total_matches_team['Winner'] == 'India']

    # Concatenate the data to combine all relevant matches (India as Team 1, Team 2, or Winner)
    india_matches_df = pd.concat(
        [india_as_team1, india_as_team2, india_as_winner]).drop_duplicates().reset_index(drop=True)

    # Filter to keep only matches where India is involved (either as Team 1 or Team 2)
    india_matches = india_matches_df[
        (india_matches_df['Team 1'] == 'India') | (india_matches_df['Team 2'] == 'India')
    ]

    # Create a new column to represent the opponent team
    india_matches['Opponent'] = india_matches.apply(
        lambda row: row['Team 2'] if row['Team 1'] == 'India' else row['Team 1'], axis=1
    )

    # Count the number of matches played against each opponent
    matches_count = india_matches['Opponent'].value_counts().reset_index()
    matches_count.columns = ['Opponent', 'Matches Played']

    # Print the result showing the number of matches against each opponent
    print("\n--- Number of matches India has played against different teams ---")
    print(matches_count.to_string(index=False))


def calc_total_india_wins_losses(df_total_matches_team: pd.DataFrame):
    """
    This function processes the match data to determine how many games India won and lost
    against each opponent, excluding ties. It then aggregates the results by opponent and
    displays the number of wins and losses against each team.

    Args:
    - df_total_matches_team (pd.DataFrame): DataFrame containing match data with columns such as 'Team 1',
      'Team 2', 'Winner', and others.

    """
    print("#### Total matches India Won or Lost against other teams ####")

    # Filter matches where India is either Team 1 or Team 2
    india_matches = df_total_matches_team[
        (df_total_matches_team['Team 1'] == 'India') | (df_total_matches_team['Team 2'] == 'India')
    ].copy()

    # Add columns to indicate if India won or lost (excluding ties)
    india_matches['India Won'] = india_matches.apply(
        lambda row: 1 if (
            (row['Team 1'] == 'India' and row['Winner'] == 'India') or
            (row['Team 2'] == 'India' and row['Winner'] == 'India')
        ) else 0, axis=1
    )

    india_matches['India Lost'] = india_matches.apply(
        lambda row: 1 if (
            (row['Team 1'] == 'India' and row['Winner'] != 'India' and row['Winner'] != 'Tie') or
            (row['Team 2'] == 'India' and row['Winner'] != 'India' and row['Winner'] != 'Tie')
        ) else 0, axis=1
    )

    # Determine the opponent based on the position of 'India'
    india_matches['Opponent'] = india_matches.apply(
        lambda row: row['Team 2'] if row['Team 1'] == 'India' else row['Team 1'], axis=1
    )

    # Group by opponent and aggregate the number of wins and losses
    india_stats = india_matches.groupby('Opponent').agg(
        {'India Won': 'sum', 'India Lost': 'sum'}
    ).reset_index()

    # Display the results
    print("\n--- India Matches Win/Loss Summary ---")
    print(india_stats)


def calc_most_played_matches_grounds_india(df_total_matches_team: pd.DataFrame):
    """
    This function analyzes the total match data to determine which home and away grounds India
    has played the most matches. It categorizes the matches based on the venue (home or away),
    then calculates the frequency of matches played on each ground. The most frequently played
    grounds are then displayed.

    Args:
    - df_total_matches_team (pd.DataFrame): DataFrame containing match data with columns such as 'Team 1',
      'Team 2', 'Venue_Team1', 'Venue_Team2', and 'Ground'.

    """
    print("#### Home and Away Grounds where India has played the most matches ####")

    #  Filter matches involving India
    india_matches = df_total_matches_team[
        (df_total_matches_team['Team 1'] == 'India') | (df_total_matches_team['Team 2'] == 'India')
    ].copy()

    # Separate Home and Away matches for India
    india_matches['Location'] = india_matches.apply(
        lambda row: 'Home' if (row['Team 1'] == 'India' and row['Venue_Team1'] == 'Home') or
                              (row['Team 2'] == 'India' and row['Venue_Team2'] == 'Home')
        else 'Away', axis=1
    )

    # Group by 'Ground' for Home and Away matches separately
    home_matches = india_matches[india_matches['Location'] == 'Home']
    away_matches = india_matches[india_matches['Location'] == 'Away']

    home_ground_counts = home_matches['Ground'].value_counts()
    away_ground_counts = away_matches['Ground'].value_counts()

    # Identify the most frequent grounds
    most_home_ground = home_ground_counts.idxmax()
    most_home_matches = home_ground_counts.max()

    most_away_ground = away_ground_counts.idxmax()
    most_away_matches = away_ground_counts.max()

    #  Display the results
    print(f"Most frequent home ground: {most_home_ground} with {most_home_matches} matches.")
    print(f"Most frequent away ground: {most_away_ground} with {most_away_matches} matches.")


def calculate_avg_win_loss_runs(df_matches: pd.DataFrame):
    """
    This function processes match data involving India to compute the average run margin for wins
    and losses in each year. The results are then displayed in a formatted table showing the average
    run margin for both wins and losses by year.

    Args:
    - df_matches (pd.DataFrame): DataFrame containing match data with columns such as 'Team 1', 'Team 2',
      'Winner', 'Margin', and 'Match Date'.

    """
    print("#### Average Indian Win or Loss by Runs per Year ####")

    # Filter matches where India is involved
    india_matches = df_matches[
        (df_matches['Team 1'] == 'India') | (df_matches['Team 2'] == 'India')
    ].copy()

    # Parse the match date to extract the year
    def extract_year(date_str):
        try:
            date = pd.to_datetime(date_str, format='%b %d, %Y', errors='coerce')
            if not pd.isna(date):
                return date.year
        except Exception:
            if ',' in date_str:
                return int(date_str.split(',')[-1].strip())
            return np.nan

    india_matches['Year'] = india_matches['Match Date'].apply(extract_year).astype('Int64')
    india_matches = india_matches.dropna(subset=['Year'])

    # Determine Win or Loss and filter matches with run margins
    india_matches['Result'] = india_matches.apply(
        lambda row: 'Win' if row['Winner'] == 'India' else
                    'Loss' if row['Winner'] != 'India' and row['Winner'] != 'Tie' else np.nan, axis=1
    )
    india_matches = india_matches.dropna(subset=['Result'])
    india_matches['Margin Runs'] = india_matches['Margin'].apply(
        lambda x: int(x.split(' ')[0]) if 'runs' in str(x).lower() else np.nan
    ).astype('Int64')
    india_matches = india_matches.dropna(subset=['Margin Runs'])

    # Group by year and result, then calculate the averages
    yearly_avg = india_matches.groupby(['Year', 'Result'])['Margin Runs'].mean().unstack(fill_value=0)

    # Round to integers or floats
    yearly_avg = yearly_avg.round(0).astype(int)

    # Output the result as a formatted table
    formatted_table = tabulate(yearly_avg.reset_index(), headers="keys", tablefmt="grid")
    print(formatted_table)


if __name__ == "__main__":
    generate_match_report()
