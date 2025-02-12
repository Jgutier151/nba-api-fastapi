import requests

BASE_URL = "https://www.balldontlie.io/api/v1/games?dates[]=2024-12-02"

def fetch_data(endpoint, params=None):
    """
    Fetch data from a given API endpoint.
    """
    url = f"{BASE_URL}/{endpoint}"  # Add endpoint to base URL
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Example: Fetch yesterday's games
params = {"dates[]": "2024-12-02"}  # Replace with desired date
data = fetch_data("games", params=params)  # "games" is the endpoint
print(data)
