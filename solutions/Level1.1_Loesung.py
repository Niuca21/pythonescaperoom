import hashlib

cookie = "Cookie hier hinzufügen"


def run(_):
    flask_secret_ascii = [ord(
        n) for n in "adminpasssowrd"]

    cookie_values = [ord(n) for n in cookie]
    sum_cookie = sum(cookie_values)
    sum_secret = sum(flask_secret_ascii)
    payload = f"{sum_cookie}:{sum_secret}"
    auth_hash = hashlib.sha256(payload.encode()).hexdigest()
    auth_value = auth_hash[:12]

    return auth_value
