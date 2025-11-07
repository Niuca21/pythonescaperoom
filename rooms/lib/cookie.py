# ---------------------------
# Level 1 (Mittel - Veronika)
# ---------------------------

import random
import json
import hashlib
from pathlib import Path


def read_cookie(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_random_cookie(cookie_data) -> str:
    data = cookie_data.get("Gruppe_HH_05.py", {}).get("data", {})
    cookies = data.get("cookies", [data.get("cookie")])
    cookie = random.choice(cookies)
    return cookie


def cookie_ascii(cookie):
    ascii_str = " ".join(str(ord(c)) for c in cookie)
    return ascii_str


def combine_cookie_and_secret(cookie_str: str, flask_secret: list[int]) -> int:
    cookie_values = [ord(n) for n in cookie_str]
    flask_secret_ascii = [ord(n) for n in flask_secret]
    print("Cookie_ascii", cookie_values)
    print("Cookie_ascii", flask_secret_ascii)

    sum_cookie = sum(cookie_values)
    print("Sum cookie values", sum_cookie)
    sum_secret = sum(flask_secret_ascii)
    print("Sum secret values", sum_secret)
    payload = f"{sum_cookie}:{sum_secret}"
    print("Payload", payload)
    auth_hash = hashlib.sha256(payload.encode()).hexdigest()
    print("Auth hash", auth_hash)
    auth_number = auth_hash[:12]

    return auth_number
