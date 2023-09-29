import time
import requests
import access

# /accounts/private/v1/admin/requests/csv/import
# specify api and creds
api_url = ""
email = ""
password = ""

duration = 3600  # 1 hour in seconds
interval = 60  # 60 seconds

start_time = time.time()
end_time = start_time + duration
count = 0
while time.time() < end_time:
    tokens = access.get_tokens(api_url, email, password)
    url = f"{api_url}/accounts/private/v1/admin/requests/csv/import"
    headers = {
        "Authorization": f"Bearer {tokens[0]}",
        "Cookie": f"token_signature={tokens[1]}"
    }
    count += 1
    files = {
        # put file in the same folder and specify the name.extension(text/csv)
        "file": ("imp2.txt", open("imp2.txt", "rb"), "text/csv"),
    }
    try:
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            print(response.text, count)
        else:
            print(f"Error: {response.status_code} - {response.json()} and count = {count}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    time.sleep(interval)
