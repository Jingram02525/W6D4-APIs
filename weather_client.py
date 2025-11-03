import argparse, requests
URL = "https://api.open-meteo.com/v1/forecast"
def get_weather(lat: float, lon: float):
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    r = requests.get(URL, params=params, timeout=5)
    r.raise_for_status()
    return r.json()
def print_weather(data: dict):
    cw = data.get("current_weather", {})
    print("Location (approx):", data.get("latitude"), data.get("longitude"))
    print("Temperature:", cw.get("temperature"), "°C")
    print("Wind Speed:", cw.get("windspeed"), "km/h")
    print("Time:", cw.get("time"))
def main():
    p = argparse.ArgumentParser(description="Weather CLI using Open-Meteo")
    p.add_argument("--lat", type=float, default=40.71, help="Latitude (default NYC)")
    p.add_argument("--lon", type=float, default=-74.01, help="Longitude (default NYC)")
    args = p.parse_args()
    try:
        data = get_weather(args.lat, args.lon); print_weather(data)
    except requests.exceptions.RequestException as e:
        print("Error fetching weather:", e)
    except KeyError as e:
        print("Unexpected data shape; check docs. Missing key:", e)
if __name__ == "__main__":
    main()