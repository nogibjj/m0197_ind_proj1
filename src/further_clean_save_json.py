"""
Use the lib.py functions to clean the data and save it to a new file.

"""

from lib import (count_genres, 
                 convert_duration_ms_to_duration_m, 
                 describe_selected_columns)

import pandas as pd

data = pd.read_csv("datasets/playlist_2010to2022.csv")

data = data.drop(
    [
        "playlist_url",
        "track_id",
        "track_name",
        "artist_id",
        "album",
        "artist_popularity",
        "time_signature",
    ],
    axis=1,
)

data["duration_m"] = data["duration_ms"].apply(convert_duration_ms_to_duration_m)
data["artist_genres"] = data["artist_genres"].apply(count_genres)

data = data.drop(["duration_ms"], axis=1)


# function to select only numeric columns and save them as new json file
def save_json(df, filename):
    df = df.select_dtypes(include="number")
    df.to_json(f"datasets/{filename}.json", orient="records")


if __name__ == "__main__":
    save_json(data, "playlist_2010to2022_clean")
    selected_columns=['artist_genres', 'track_popularity', 'duration_m']
    descriptive_stats = describe_selected_columns(data, selected_columns)
    with open("reports/stats.md", "w") as f:
        f.write("\n")
        f.writelines(descriptive_stats.to_markdown())
