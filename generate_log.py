from lib.generate_log import fetch_data, generate_log


if __name__ == "__main__":
    sample_logs = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_logs)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
