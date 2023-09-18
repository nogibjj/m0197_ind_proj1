"""
A python script with all the common functions used in the project. 

Functions:

"""
import pandas as pd


def count_genres(genres_list):
    """Counts the number of genres the artist plays.

    Args:
        genres_list (list): List of genres.

    Returns:
        int: The number of genres in the list.
    """
    return len(genres_list)


def describe_selected_columns(df, columns):
    """Displays descriptive statistics for selected columns in a DataFrame.

    Args:
        df: A Pandas DataFrame.
        columns: A list of column names.

    Returns:
        A Pandas DataFrame containing the descriptive statistics for the selected columns.
    """

    if not all(column in df.columns for column in columns):
        raise ValueError("Some of the columns do not exist in the DataFrame.")

    descriptive_stats = round(df[columns].describe(), 2)

    return descriptive_stats


def convert_duration_ms_to_duration_m(duration_ms):
    """Converts duration in milliseconds to duration in minutes.

    Args:
        duration_ms: A duration in milliseconds.

    Returns:
        A duration in minutes.
    """

    duration_m = duration_ms / 60000
    return duration_m
