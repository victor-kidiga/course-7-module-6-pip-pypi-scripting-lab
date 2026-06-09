from datetime import datetime


def generate_log(data):
    """Write log entries to a timestamped text file and return the filename."""
    if not isinstance(data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch sample post data from a public API."""
    try:
        import requests
    except ImportError:
        return {}

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=10,
        )
    except requests.RequestException:
        return {}

    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    sample_logs = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_logs)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
