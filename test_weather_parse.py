# test_weather_parse.py
import unittest
from weather_parse import extract_current, summarize_current

SAMPLE = {
    "latitude": 40.71,
    "longitude": -74.01,
    "current_weather": {
        "temperature": 21.3,
        "windspeed": 9.5,
        "time": "2025-11-14T12:00"
    }
}

MISSING = {"current_weather": {}}
EMPTY = {}

class TestWeatherParse(unittest.TestCase):
    def test_extract_current_happy(self):
        temp, wind = extract_current(SAMPLE)
        self.assertEqual(temp, 21.3)
        self.assertEqual(wind, 9.5)

    def test_extract_current_missing_keys(self):
        temp, wind = extract_current(MISSING)
        self.assertIsNone(temp)
        self.assertIsNone(wind)

    def test_extract_current_empty(self):
        temp, wind = extract_current(EMPTY)
        self.assertIsNone(temp)
        self.assertIsNone(wind)

    def test_summarize_current_happy(self):
        self.assertEqual(
            summarize_current(SAMPLE),
            "Temp: 21.3 °C | Wind: 9.5 km/h"
        )

    def test_summarize_current_missing(self):
        self.assertEqual(summarize_current(MISSING), "Data unavailable")
        self.assertEqual(summarize_current(EMPTY), "Data unavailable")

if __name__ == "__main__":
    unittest.main(verbosity=2)
