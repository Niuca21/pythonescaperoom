# Beispiellösung Level 2: Veronika
import re


def run(path: str) -> str:

    with open(path, "r", encoding="utf-8") as f:
        secret = f.read()

    matches = re.findall(r"-\d+\sUTC\.?", secret)
    print(matches)
    clean_matches = [m.replace(" UTC", "").replace(".", "") for m in matches]

    counts = {}
    for key in clean_matches:
        counts[key] = counts.get(key, 0) + 1

    unique_keys = list(dict.fromkeys(clean_matches))[:3]
    solution_numbers = [str(counts[k]) for k in unique_keys]
    solution = "".join(solution_numbers) + ".jpg"
    print(solution)
    return solution
