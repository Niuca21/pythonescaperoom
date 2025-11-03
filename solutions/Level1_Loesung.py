def run(eingabe: str) -> int:
    flask_secret_ascii = [ord(
        n) for n in "adminpasssowrd"]

    cookie_values = [ord(n) for n in eingabe]
    sum_cookie = sum(cookie_values)
    sum_secret = sum(flask_secret_ascii)
    auth_value = (sum_cookie + sum_secret) % 1000

    return auth_value
