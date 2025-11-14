# weather_parse.py
"""
Tiny helpers for parsing Open-Meteo style JSON.
These are pure functions (no requests), safe for offline tests.
"""

def extract_current(weather_json: dict):
    """
    Return (temperature_c, wind_kmh) from an Open-Meteo-like response.
    If fields are missing, return (None, None).
    """
    cw = weather_json.get("current_weather", {})
    return cw.get("temperature"), cw.get("windspeed")


def summarize_current(weather_json: dict) -> str:
    """
    Return a short human-readable summary like:
    'Temp: 21.3 °C | Wind: 9.5 km/h'
    Falls back to 'Data unavailable' if keys are missing.
    """
    temp, wind = extract_current(weather_json)
    if temp is None or wind is None:
        return "Data unavailable"
    return f"Temp: {temp} °C | Wind: {wind} km/h"
