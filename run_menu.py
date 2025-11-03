import subprocess, sys, json, os
TARGETS = [
    ("Demo: JSONPlaceholder (GET)", ["python", "api_demo.py"]),
    ("Weather: NYC default", ["python", "weather_client.py"]),
    ("Weather: custom (LA)", ["python", "weather_client.py", "--lat", "34.05", "--lon", "-118.24"]),
]
STATE = ".last_run_w6d4"
def load_last():
    try:
        with open(STATE, "r") as f:
            return json.load(f)
    except Exception:
        return {}
def save_last(idx):
    with open(STATE, "w") as f:
        json.dump({"last": idx}, f)
def main():
    env_sel = os.environ.get("RUN_TARGET")
    last = load_last().get("last")
    if env_sel is not None:
        try:
            idx = int(env_sel)
            title, cmd = TARGETS[idx]
            print(f"▶ Running via RUN_TARGET={idx}: {title}")
            save_last(idx); sys.exit(subprocess.call(cmd))
        except Exception as e:
            print("Invalid RUN_TARGET:", e)
    print("\n=== W6D4 — APIs Workshop Runner ===")
    for i, (title, _) in enumerate(TARGETS):
        mark = " (last)" if last == i else ""
        print(f"[{i}] {title}{mark}")
    choice = input("Choose number (Enter = re-run last): ").strip()
    if choice == "":
        if last is None:
            print("No previous selection. Please choose a number."); return 0
        idx = last
    else:
        try:
            idx = int(choice)
        except ValueError:
            print("Please enter a valid number."); return 1
    if not (0 <= idx < len(TARGETS)):
        print("Out of range."); return 1
    title, cmd = TARGETS[idx]
    print(f"▶ Running: {title} — {' '.join(cmd)}")
    save_last(idx)
    return subprocess.call(cmd)
if __name__ == "__main__":
    sys.exit(main())