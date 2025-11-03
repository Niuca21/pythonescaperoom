# Beispiellösung Level 2: Veronika
# Lernziele:
# 1. Dateien lesen
#    - Öffnen von Dateien mit open()
#    - Lesen des gesamten Inhalts (read())
#    - Umgang mit Encoding (UTF-8)
#
# 2. Reguläre Ausdrücke (Regex) verwenden
#    - re.findall() kennenlernen
#    - Muster definieren, z. B. "-\d+ UTC" oder "-\d+ UTC."
#    - Optionale Zeichen erkennen (".?")
#
# 3. String-Manipulation
#    - Entfernen unerwünschter Teile (replace())
#    - Sauberes Aufbereiten der gefundenen Werte
#
# 4. Dictionaries für Zählungen
#    - Zählen von Vorkommen einzelner Elemente
#    - Zugriff auf Dictionary-Werte und Standardwerte (dict.get)
#
# 5. Listenoperationen
#    - Entfernen von Duplikaten unter Beibehaltung der Reihenfolge (dict.fromkeys())
#    - Indexierung und Slicing [:3]
#
# 6. String-Formatierung und Zusammenführung
#    - Umwandeln von Zahlen in Strings (str())
#    - Zusammenfügen mit join()
#    - Erzeugen eines Dateinamens wie z.B. "566.jpg"
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
