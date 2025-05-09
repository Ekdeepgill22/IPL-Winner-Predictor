import pandas as pd

def load_data(path='data/Match_Info.csv'):
    # Load the CSV file
    df = pd.read_csv(path)

    # Basic cleanup
    df = df.dropna(subset=['winner'])  # Remove matches with no result

    # Standardize team names
    team_mapping = {
        'Rising Pune Supergiant': 'Rising Pune Supergiants',
        'Delhi Daredevils': 'Delhi Capitals',
        'Deccan Chargers': 'Sunrisers Hyderabad',
        'Kings XI Punjab': 'Punjab Kings',
        "Gujarat Lions": 'Gujarat Titans',
        }
    df['team1'] = df['team1'].replace(team_mapping)
    df['team2'] = df['team2'].replace(team_mapping)
    df['winner'] = df['winner'].replace(team_mapping)

    return df


