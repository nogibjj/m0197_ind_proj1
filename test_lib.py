"""
Test goes here

"""

from utils.lib import (
    count_genres,
    describe_selected_columns,
    convert_duration_ms_to_duration_m,
)

import unittest
import pandas as pd


class TestCountGenres(unittest.TestCase):
    """
    Test functions in lib.py
    """

    def test_count_genres_empty_list(self):
        genres_list = []
        expected_count = 0
        actual_count = count_genres(genres_list)
        self.assertEqual(expected_count, actual_count)

    def test_count_genres_single_genre(self):
        genres_list = ["Rock"]
        expected_count = 1
        actual_count = count_genres(genres_list)
        self.assertEqual(expected_count, actual_count)

    def test_count_genres_multiple_genres(self):
        genres_list = ["Rock", "Pop", "Country"]
        expected_count = 3
        actual_count = count_genres(genres_list)
        self.assertEqual(expected_count, actual_count)


class TestDescribeSelectedColumns(unittest.TestCase):
    def test_describe_selected_columns_empty_dataframe(self):
        df = pd.DataFrame()
        columns = ["artist", "genres"]
        with self.assertRaises(ValueError):
            describe_selected_columns(df, columns)

    def test_describe_selected_columns_nonexistent_column(self):
        df = pd.DataFrame({"artist": ["Bob", "Mary", "Joe"]})
        columns = ["artist", "genres"]
        with self.assertRaises(ValueError):
            describe_selected_columns(df, columns)

    def test_describe_selected_columns_returns_correct_descriptive_stats(self):
        df = pd.DataFrame({"age": [25, 30, 35]})

        columns = ["age"]

        expected_descriptive_stats = pd.DataFrame(
            {
                "count": [3.0],
                "mean": [30.0],
                "std": [5.0],
                "min": [25.0],
                "25%": [27.5],
                "50%": [30.0],
                "75%": [32.5],
                "max": [35.0],
            }
        )

        actual_descriptive_stats = describe_selected_columns(df, columns).T
        expected_descriptive_stats = expected_descriptive_stats.reset_index(
            drop=True, inplace=True
        )
        actual_descriptive_stats = actual_descriptive_stats.reset_index(
            drop=True, inplace=True
        )

        self.assertEqual(expected_descriptive_stats, actual_descriptive_stats)


class TestConvertDurationMsToDurationM(unittest.TestCase):
    def test_convert_duration_ms_to_duration_m_positive_ms(self):
        duration_ms = 60000
        expected_duration_m = 1
        actual_duration_m = convert_duration_ms_to_duration_m(duration_ms)
        self.assertEqual(expected_duration_m, actual_duration_m)

    def test_convert_duration_ms_to_duration_m_negative_ms(self):
        duration_ms = -60000
        expected_duration_m = -1
        actual_duration_m = convert_duration_ms_to_duration_m(duration_ms)
        self.assertEqual(expected_duration_m, actual_duration_m)


if __name__ == "__main__":
    unittest.main()
