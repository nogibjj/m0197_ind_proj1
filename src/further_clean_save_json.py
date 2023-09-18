"""
Use the lib.py functions to clean the data and save it to a new file.

"""
import sys

sys.path.append("/utils")
from ..utils.lib import count_genres, convert_duration_ms_to_duration_m

import pandas as pd

data = pd.read_csv("../datasets/playlist_2010to2022.csv")

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


# function to select only numeric columns and save them as new json file on the ../datasets folder
def save_json(df, filename):
    df = df.select_dtypes(include="number")
    df.to_json(f"../datasets/{filename}.json", orient="records")


save_json(data, "playlist_2010to2022_clean")
