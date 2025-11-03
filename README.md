# W6D4 — APIs Workshop (GitHub Codespaces)

## Launch
1) GitHub → Code → Create codespace on main
2) Container auto-installs `requests` + `rich`

## Run
- Menu: `python run_menu.py`
- Demo: `python api_demo.py`
- Weather (NYC): `python weather_client.py`
- Weather (custom): `python weather_client.py --lat 34.05 --lon -118.24`

## Notes
- Check `response.status_code` or call `response.raise_for_status()`
- Parse JSON with `.json()` and inspect `data.keys()`
- Catch `requests.exceptions.RequestException` for network/HTTP issues

## Public APIs for Breakout 1
- Dog CEO: https://dog.ceo/api/breeds/image/random
- Bored API: https://www.boredapi.com/api/activity
- Cat Fact: https://catfact.ninja/fact

Open-Meteo: https://open-meteo.com/
