import requests


#  def for getting access token and token_signature
def get_tokens(url, email, password):
    url_login = f"{url}/users/public/v1/auth/signin"
    headers_login = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en,es;q=0.9,ru;q=0.8,ru-RU;q=0.7,en-US;q=0.6,de;q=0.5",
        "Connection": "keep-alive",
        "Content-Type": "application/json"
    }
    payload = {
        "data": {
            "email": f"{email}",
            "password": f"{password}"
        }
    }

    response = requests.post(url_login, headers=headers_login, json=payload)
    if response.status_code == 200:
        data = response.json().get("data")
        access_token = data.get("accessToken")
        token_signature = response.cookies.get("token_signature")
        return [access_token, token_signature]
    else:
        return f"Error: {response.status_code} - {response.json()}"
