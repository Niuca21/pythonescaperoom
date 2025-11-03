import random
import json
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

    sum_cookie = sum(cookie_values)
    sum_secret = sum(flask_secret_ascii)
    total = sum_cookie + sum_secret
    auth_number = total % 1000

    return auth_number
