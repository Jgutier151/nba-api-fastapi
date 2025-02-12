from nba_api.stats.endpoints import playergamelogs

# Fetch data for any season
logs = playergamelogs.PlayerGameLogs(season_nullable="2023-24", season_type_nullable="Regular Season")
data = logs.get_dict()

# Print headers (column names)
headers = data['resultSets'][0]['headers']
print(headers)
