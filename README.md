# Coding challenge

## 📋 Project Description

This code is the solution for the BCG coding challenge 

---

## 🛠️ Technologies Used

- **Python**: 3.12  
- **Pandas**: For data manipulation and analysis.  
- **NumPy**: For numerical computing and working with arrays.

---

## 📦 Installation

Follow these steps to set up the environment and run the project:

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/coding-challenge.git
cd coding-challenge
```

### 2. Create a Virtual Environment (optional but recommended):

- For **Linux/Mac**:
  ```bash
  python3.12 -m venv venv
  source venv/bin/activate
  ```

- For **Windows**:
  ```bash
  python3.12 -m venv venv
  .\venv\Scripts\activate
  ```

### 3. Install Dependencies:

Make sure **pip** is up to date:
```bash
pip install --upgrade pip
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Service

1. After setting up the environment and installing dependencies, run the main script to start the service.

```bash
python src/generate_match_report.py
```
---

## 📄 Project Structure

```bash
.
├── README.md               # Project tech refinament/documentation
├── README-TECH.md          # Project documentation
├── requirements.txt        # Project dependencies
└── data/                   # Folder with sample data (if applicable)
    └── CategorialDataset.csv
    └── ContinousDataset.csv 
    └── LabelledDataset.csv 
    └── match_report_data.csv 
    └── originalDataset.csv 
└── src/                   # Folder with sample data (if applicable)
    └── clean_prepare_data.py
    └── generate_match_report.py
    └── generate_match_report_data.py

```

## Case Study Context:

All the 4 datasets below represent the same data in different structures.
To answer the questions, you can leverage any of the forms that you are most comfortable. 

Sample list of questions below:
1. What is India’s total Win/Loss/Tie percentage?
2. What is India’s Win/Loss/Tie percentage in away and home matches?
3. How many matches has India played against different ICC teams?
4. How many matches India has won or lost against different teams?
5. Which are the home and away grounds where India has played most number of matches?
6. What has been the average Indian win or loss by Runs per year?



## Refiniment 

### Cleaning and Normalizing the data
#### **1. Load the Dataset**
   - Import the required libraries.
   - Load the data into a Pandas DataFrame for processing.

#### **2. Clean the Data**
   - Identify and handle missing values.
   - Normalize column names (e.g., remove prefixes like `Winner_` or `Team 1_`).
   - Ensure consistent data types for calculations (e.g., convert binary values to integers).

#### **3. Calculate Total Matches**
   - **Count Matches per Team**: 
     - Sum the matches for each team in columns like `Team 1_xx` and `Team 2_xx`.
   - **Summarize the Count per Team**:
     - Aggregate the counts to create a summary of total matches played by each team.

#### **4. Calculate Wins, Losses, and Ties**
   - **Wins**: Sum the binary `1` values in the `Winner_xx` columns for each team.
   - **Losses**: Subtract the total wins from the total matches for each team.
   - **Ties**: Calculate the remaining matches that are neither wins nor losses:
     \[
     \text{Ties} = \text{Total Matches} - (\text{Wins} + \text{Losses})
     \]

#### **5. Calculate Total Home Games Played**
   - Identify home games by summing occurrences of teams in `Team 1_xx` columns.
   - Aggregate the results for each team.

#### **6. Calculate Total Away Games Played**
   - Identify away games by summing occurrences of teams in `Team 2_xx` columns.
   - Aggregate the results for each team.



## What is India’s total Win/Loss/Tie percentage?

Steps:
1. **Data Preparation:**
    - Filter matches where the team is "India".
    - Count the total number of matches played (Total Matches), wins (Wins), losses (Losses), and ties (Ties).
2. **Processing:**
    - Calculate the percentages:
        - Win Percentage = (Wins / Total Matches) × 100
        - Loss Percentage = (Losses / Total Matches) × 100
        - Tie Percentage = (Ties / Total Matches) × 100
3. **Output:**
    - Display the total matches, wins, losses, ties, and their respective percentages.

## What is India’s Win/Loss/Tie percentage in away and home matches?

Steps:
1. **Data Preparation:**
    - Filter matches by location:
    - Home matches (Location == 'Home')
    - Away matches (Location == 'Away').
2. **Processing:**
    - For both Home and Away:
        - Count the total matches, wins, losses, and ties.
    - Calculate percentages using the formulas:
        -  Win Percentage = (Wins / Total Matches) × 100
        -  Loss Percentage = (Losses / Total Matches) × 100
        -  Tie Percentage = (Ties / Total Matches) × 100.
3. **Output:**
    - Display the statistics separately for home and away matches.

## How many matches has India played against different ICC teams?
Steps:
1. **Data Preparation:**
    - Filter matches where Team or Opponent is "India".
2. **Processing:**
Group the matches by Opponent and count the total matches played against each team.
3. **Output:**
    - Provide a list or table showing the opponent teams and the number of matches played against each.

## How many matches has India won or lost against different teams?
Steps:
1. **Data Preparation:**
    - Filter matches where Team == 'India'.
    - Include the result (Win or Loss) and the opponent team.
2. **Processing:**
    - Group by Opponent and calculate:
    - Total wins against each team.
    - Total losses against each team.
3. **Output:**
    - Provide a table showing opponent teams, matches won, and matches lost.

## Which are the home and away grounds where India has played the most matches?
Steps:
1. **Data Preparation:**
    - Filter matches where Team == 'India'.
    - Separate matches by Home and Away.
2. **Processing:**
    - Group by Ground for home and away matches separately.
    - Count the total matches played at each ground.
    - Identify the grounds with the maximum matches.
3. **Output:**
    - Display the most frequent home and away grounds and the number of matches played at each.

## What has been the average Indian win or loss by runs per year?
Steps:
1. **Data Preparation:**
    - Filter matches where Team == 'India'.
    - Extract the year from the match date.
    - Identify results (Win or Loss) and the margin of runs.
2. **Processing:**
    - Group by year and calculate:
    - Average runs for wins: mean(Margin of Runs) for Win.
Average runs for losses: mean(Margin of Runs) for Loss.
3. **Output:**
    - Provide a table or graph showing yearly averages for wins and losses by runs.



 # Calculando Total Losses
        total_stats_df['Total Losses'] = total_matches['Total Matches'] - total_stats_df['Total Wins']

        print("Soma de Wins e Losses:", total_stats_df['Total Losses'].sum())
        print("Total de Matches:", total_matches['Total Matches'].sum())


---

## 📧 Contact

- **Author**: [Carol Soares]  
- **Email**: [karol.siva@hotmail.com]  
- **GitHub**: [carolinesoarws](https://github.com/carolinesoarws?tab=repositories)

---