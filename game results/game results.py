import requests
import pandas as pd

# API Base URL
BASE_URL = "https://www.balldontlie.io/api/v1"

# Function to fetch data from an endpoint
def fetch_data(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Fetch last night's games
def fetch_yesterdays_games():
    from datetime import datetime, timedelta
    yesterday = datetime.now() - timedelta(1)
    date_str = yesterday.strftime('%Y-%m-%d')
    params = {"dates[]2024-12-02": date_str}

    data = fetch_data("games", params)
    if data and data.get("data"):
        return pd.DataFrame(data["data"])
    return pd.DataFrame()

# Fetch player stats for a specific game
def fetch_game_stats(game_id):
    params = {"game_ids[]": game_id}
    data = fetch_data("stats", params)
    if data and data.get("data"):
        return pd.DataFrame(data["data"])
    return pd.DataFrame()

# Main function
def main():
    print("Fetching last night's games...")
    games_df = fetch_yesterdays_games()
    if not games_df.empty:
        print("Games data fetched:")
        print(games_df.head())

        # Example: Fetch stats for the first game
        first_game_id = games_df.iloc[0]["id"]
        print(f"Fetching stats for game ID {first_game_id}...")
        game_stats_df = fetch_game_stats(first_game_id)
        if not game_stats_df.empty:
            print("Game stats fetched:")
            print(game_stats_df.head())
    
        # Save data to CSV
        games_df.to_csv("nba_games_yesterday.csv", index=False)
        game_stats_df.to_csv(f"nba_game_{first_game_id}_stats.csv", index=False)
        print("Data saved to CSV files.")
    else:
        print("No games found for yesterday.")

if __name__ == "__main__":
    main()
