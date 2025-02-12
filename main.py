from fastapi import FastAPI, HTTPException
from nba_api.stats.endpoints import playergamelogs

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NBA API Server is Running!"}

@app.get("/playergamelogs")
def get_player_game_logs(player_id: int, season: str = "2023-24", season_type: str = "Regular Season"):
    try:
        # Use the correct argument name `player_id_nullable`
        logs = playergamelogs.PlayerGameLogs(
            player_id_nullable=str(player_id),
            season_nullable=season,
            season_type_nullable=season_type
        )

        data = logs.get_dict()

        # Extract headers and rows
        headers = data['resultSets'][0]['headers']
        rows = data['resultSets'][0]['rowSet']

        # Filter for requested player_id (this may not be necessary anymore)
        filtered_rows = [row for row in rows if row[headers.index("PLAYER_ID")] == player_id]

        return {
            "headers": headers,
            "data": filtered_rows
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
