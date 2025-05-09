import pandas as pd
from collections import defaultdict

# Define the set of known Indian IPL venues
INDIAN_VENUES = {
    'MA Chidambaram Stadium, Chepauk, Chennai',
    'Dr DY Patil Sports Academy, Mumbai',
    'Brabourne Stadium, Mumbai',
    'Wankhede Stadium, Mumbai',
    'Eden Gardens, Kolkata',
    'Arun Jaitley Stadium, Delhi',
    'Narendra Modi Stadium, Ahmedabad',
    'Sawai Mansingh Stadium, Jaipur',
    'M Chinnaswamy Stadium, Bengaluru',
    'Rajiv Gandhi International Stadium, Uppal',
    'Punjab Cricket Association IS Bindra Stadium, Mohali',
    'Himachal Pradesh Cricket Association Stadium, Dharamsala',
    'Holkar Cricket Stadium, Indore',
    'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow'
}

def get_team_venues():
    df = pd.read_csv("data/Match_Info.csv")

    team_venues = defaultdict(set)

    for _, row in df.iterrows():
        venue = row["venue"]
        team1 = row["team1"]
        team2 = row["team2"]

        if venue in INDIAN_VENUES:
            team_venues[team1].add(venue)
            team_venues[team2].add(venue)

    # Convert sets to sorted lists for easier JSON use
    return {
        team: sorted(list(venues))
        for team, venues in team_venues.items()
    }

# Optional helper for neutral venue detection
def get_neutral_venues(team1, team2):
    team_venues = get_team_venues()
    venues_team1 = set(team_venues.get(team1, []))
    venues_team2 = set(team_venues.get(team2, []))
    common_venues = venues_team1.union(venues_team2)

    neutral_venues = [
        venue for venue in common_venues
        if venue not in venues_team1 or venue not in venues_team2
    ]
    return sorted(neutral_venues)
