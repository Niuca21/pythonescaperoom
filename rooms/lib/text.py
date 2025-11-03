# ---------------------------
# Level 2 (Schwierig - Veronika)
# ---------------------------

import re
import random
import time


def generate_decrypted_file(path, output_path, placeholders: list[str]) -> str:
    utc_list = [
        f"-{random_utc_timestamp()}" for _ in placeholders]

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    for ph, utc in zip(placeholders, utc_list):
        text = text.replace(ph, utc)

    desired_counts = [4, 4, 3]
    additional_lines = []
    for utc, count in zip(utc_list, desired_counts):
        additional_lines.extend(
            [f"Geheimer Key seit {utc} UTC." for _ in range(count)])
    random.shuffle(additional_lines)
    text += "\n\n" + "\n".join(additional_lines)

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

    matches = re.findall(r"-\d+\sUTC", text)

    clean_matches = [m.replace(" UTC", "") for m in matches]

    counts = {}
    for key in clean_matches:
        counts[key] = counts.get(key, 0) + 1
    unique_keys = list(dict.fromkeys(clean_matches))[:3]
    solution_numbers = [str(counts[k]) for k in unique_keys]

    solution = "".join(solution_numbers) + ".jpg"
    print("Decrypted file analysis result:", solution)

    return solution
