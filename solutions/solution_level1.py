secret = "67 111 111 107 105 101 109 111 110 115 116 101 114"


def run(secret):
    return "".join(chr(int(n)) for n in secret.split())
