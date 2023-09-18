"""
testing functions in further_clean_save_json.py script

"""

from further_clean_save_json import save_json

import unittest
import pandas as pd
import json


class SaveJsonTest(unittest.TestCase):
    def test_save_json_with_numeric_columns(self):
        df = pd.DataFrame(
            {"numeric_column": [1, 2, 3], "non_numeric_column": ["a", "b", "c"]}
        )

        save_json(df, "test")

        with open("datasets/test.json", "r") as f:
            json_data = json.load(f)

        for row in json_data:
            for key, value in row.items():
                self.assertTrue(isinstance(value, (int, float)))


if __name__ == "__main__":
    unittest.main()
