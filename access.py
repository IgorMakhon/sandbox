import requests


def get_tokens():
    url_login = "https://api-mob1.ebanq-qa.com/users/public/v1/auth/signin"
    headers_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en,es;q=0.9,ru;q=0.8,ru-RU;q=0.7,en-US;q=0.6,de;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "<https://mob1.ebanq-qa.com>",
        "Referer": "<https://mob1.ebanq-qa.com/>",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    payload = {
        "data": {
            "email": "igad",
            "password": "Password1!"
        }
    }

    response = requests.post(url_login, headers=headers_login, json=payload)
    if response.status_code == 200:
        data = response.json().get("data")
        access_token = data.get("accessToken")
        token_signature = response.cookies.get("token_signature")
        return [access_token, token_signature]
    else:
        print(f"Error: {response.status_code} - {response.json()}")
