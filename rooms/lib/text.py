# ---------------------------
# Level 2 (Schwierig - Veronika)
# ---------------------------

import re
import random
import time


def generate_decrypted_file(path, output_path, placeholders: list[str]) -> str:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    total = len(placeholders)
    corrupt_count = max(1, int(total * 0.3))
    corrupt_placeholders = set(random.sample(range(total), corrupt_count))

    for i, ph in enumerate(placeholders):
        ts = f"-{random_utc_timestamp()}"
        if i in corrupt_placeholders:
            ts = ts.replace("0", "o").replace("1", "I").replace("0", "O")
        text = text.replace(ph, ts)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    return output_path


def random_utc_timestamp(start_year=2000, end_year=2025):
    start = int(time.mktime(time.strptime(
        f"{start_year}-04-12", "%Y-%m-%d")))
    end = int(time.mktime(time.strptime(f"{end_year}-10-31", "%Y-%m-%d")))
    return random.randint(start, end)


def count_decrypted_words(output_path: str) -> str:
    with open(output_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("I", "1").replace("o", "0").replace("O", "0")
    matches = re.findall(r"-\d+\sUTC", text)
    clean_matches = [m.replace(" UTC", "") for m in matches]

    counts = {}
    for key in clean_matches:
        counts[key] = counts.get(key, 0) + 1

    placeholders_ordered = list(dict.fromkeys(clean_matches))[
        :3]
    solution_numbers = [str(counts[k]) for k in placeholders_ordered]
    solution = "".join(solution_numbers) + ".jpg"
    return solution

    # counts = {}
    # for key in clean_matches:
    #    counts[key] = counts.get(key, 0) + 1
    # unique_keys = list(dict.fromkeys(clean_matches))[:3]
    # solution_numbers = [str(counts[k]) for k in unique_keys]

    # solution = "".join(solution_numbers) + ".jpg"
    # print("Decrypted file analysis result:", solution)

    # return solution
