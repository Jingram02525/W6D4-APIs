import requests
def demo_success():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    print(f"\nGET {url}")
    r = requests.get(url, timeout=5, headers={"Accept": "application/json"})
    print("Status code:", r.status_code)
    r.raise_for_status()
    data = r.json()
    print("Parsed keys:", list(data.keys()))
    print("Title:", data.get("title"))
def demo_404():
    bad_url = "https://jsonplaceholder.typicode.com/todozzz"
    print(f"\nGET {bad_url}")
    r = requests.get(bad_url, timeout=5)
    print("Status code:", r.status_code)
    if r.status_code != 200:
        print("Friendly message: That endpoint does not exist (404). Check the docs.")
def main():
    print("=== Demo: Basic requests + JSON ===")
    try:
        demo_success(); demo_404()
    except requests.exceptions.RequestException as e:
        print("Network/request error:", e)
    except ValueError as e:
        print("JSON parse error:", e)
if __name__ == "__main__":
    main()