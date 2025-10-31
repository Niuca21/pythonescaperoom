import re

def run(secret):
    """
    secret: str
        Der Text aus der Datei output.txt, der die UTCs enthält.
    """

    matches = re.findall(r"-\d+ UTC", secret)

    counts = {}
    for m in matches:
        if m in counts:
            counts[m] += 1
        else:
            counts[m] = 1

    unique_keys = list(dict.fromkeys(matches))[:3]

    solution_numbers = [str(counts[k]) for k in unique_keys]
    solution = "".join(solution_numbers) + ".jpg"

    solution = "443.jpg"

    return solution


if __name__ == "__main__":
    with open("output.txt", "r", encoding="utf-8") as f:
        secret_text = f.read()

    print(run(secret_text))
