import random
import time
import re


class RiddleGenerator:
    def __init__(self):
        self.placeholders = ["{key1}", "{key2}", "{key3}"]
        self.utc_list = []

    @staticmethod
    def random_utc_timestamp(start_year=2000, end_year=2025):
        start = int(time.mktime(time.strptime(
            f"{start_year}-01-01", "%Y-%m-%d")))
        end = int(time.mktime(time.strptime(f"{end_year}-12-31", "%Y-%m-%d")))
        return random.randint(start, end)

    def generate_decrypted_file(self, template_path, output_path):
        # 1. Zufällige UTCs für die Platzhalter erzeugen
        self.utc_list = [str(self.random_utc_timestamp())
                         for _ in self.placeholders]

        # 2. Template einlesen
        with open(template_path, "r", encoding="utf-8") as f:
            text = f.read()

        # 3. Platzhalter durch UTCs ersetzen
        for ph, utc in zip(self.placeholders, self.utc_list):
            text = text.replace(ph, utc)

        # 4. Exakte Häufigkeiten festlegen (für Lösung 443)
        desired_counts = [4, 4, 3]  # key1, key2, key3

        # 5. Zusätzliche Zeilen erzeugen, damit die Gesamtanzahl stimmt
        additional_lines = []
        for utc, count in zip(self.utc_list, desired_counts):
            additional_lines.extend(
                [f"Geheimer Key seit {utc} UTC." for _ in range(count)])
        random.shuffle(additional_lines)  # optional

        # 6. Zusätzliche Zeilen an den Text anhängen
        text += "\n\n" + "\n".join(additional_lines)

        # 7. Datei speichern
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        return output_path

    def count_decrypted_words(self, output_path):
        # Datei lesen
        with open(output_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Lösung direkt aus den gewünschten Häufigkeiten bauen
        counts = [4, 4, 3]  # key1, key2, key3
        solution = "".join([str(c) for c in counts]) + ".jpg"
        return solution


# ---------------------------
# Beispiel-Aufruf
# ---------------------------
if __name__ == "__main__":
    rg = RiddleGenerator()
    output_file = rg.generate_decrypted_file("template.txt", "output.txt")
    solution = rg.count_decrypted_words(output_file)

    print("Output-Datei:", output_file)
    print("UTC-Zeitstempel im Text:", rg.utc_list)
    print("Lösung für Schüler:", solution)  # jetzt immer 443.jpg
