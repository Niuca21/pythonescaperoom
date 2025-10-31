import random
import string
import time
import re
from EscapeRoom import EscapeRoom


class VerloreneRechner(EscapeRoom):

    def __init__(self, response):
        super().__init__(response)
        self.set_metadata("Nika", __name__)
        self.add_level(self.create_level1())
        self.add_level(self.create_level2())

    # ---------------------------
    # Level 1 (Easy - Veronika)
    # ---------------------------
    def create_level1(self):
        cockie = self.ascii_cockie()
        gamename = f"Diese Cockies sind nicht lecker"
        task_messages = [
            "Hey Buddy, ich habe jetzt die Kontrolle. ",
            "Deine Dateien sind verschluesselt. ",
            "Wenn du dein Passwort wiederhaben willst, folge den Anweisungen.",
            "Hier ist mein Wallet: Diese Cockies sind nicht lecker!"
        ]

        hints = [
            "Schaue die Webseite an und danach stelle fest, sind die Cockies lecker und was die Gangster mit ASCII zu tun haben."
        ]

        self.response.set_cookie("hint", cockie)

        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.solution_level1,
            "data": cockie
        }

    def ascii_cockie(self):
        return "67 111 111 107 105 101 109 111 110 115 116 101 114"

    def solution_level1(self, cockie):
        return "".join(chr(int(n)) for n in cockie.split())

    # ---------------------------
    # Level 2 (Textdatei mit Nebenwirkungen)
    # ---------------------------
    def create_level2(self):
        gamename = "Textdatei mit Nebenwirkungen"

        # Dateipfade
        template_path = "static/template.txt"
        output_path = "static/output.txt"

        # Platzhalter definieren
        self.placeholders = ["{key1}", "{key2}", "{key3}"]

        # Datei erzeugen (Platzhalter durch UTCs ersetzen + zusätzliche Zeilen für Lösung 443)
        decrypted_path = self.generate_decrypted_file(
            template_path, output_path)

        # Lösung intern testen
        solution = self.count_decrypted_words(
            output_path)  # Intern für Escape Room
        print("Level 2 Lösung (intern):", solution)

        # Nachrichten für Schüler
        task_messages = [
            "In dieser Nachricht versteckt sich der Schlüssel zu deinem Bild:",
            f"<a href='{decrypted_path}' target='_blank'>Geheimtext öffnen</a>",
            "Zähle sorgfältig, wie oft jede UTC-Zahl vorkommt, und kombiniere sie zu einer Dateiendung."
        ]

        # Hinweise für Schüler
        hints = [
            "Jede Zahl (z. B. -1338780358 UTC) zählt. Finde heraus, wie oft sie erscheint.",
            "Setze die Anzahl der Vorkommen in der Reihenfolge ihres ersten Auftretens zusammen.",
            "Beispiel: Wenn du 4, 4, 3 findest → {key1}{key2}{key3}.jpg = 443.jpg"
        ]

        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.count_decrypted_words,  # Prüffunktion
            "data": decrypted_path
        }

    # ---------------------------
    # Level 2. Datei erzeugen
    # ---------------------------
    def generate_decrypted_file(self, template_path, output_path):
        # Zufällige UTCs erzeugen
        self.utc_list = [
            f"-{self.random_utc_timestamp()}" for _ in self.placeholders]

        # Template einlesen
        with open(template_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Platzhalter ersetzen
        for ph, utc in zip(self.placeholders, self.utc_list):
            text = text.replace(ph, utc)

        # Zusätzliche Zeilen erzeugen, damit die Lösung 443 ergibt
        desired_counts = [4, 4, 3]  # key1, key2, key3
        additional_lines = []
        for utc, count in zip(self.utc_list, desired_counts):
            additional_lines.extend(
                [f"Geheimer Key seit {utc} UTC." for _ in range(count)])
        random.shuffle(additional_lines)
        text += "\n\n" + "\n".join(additional_lines)

        # Datei speichern
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        return output_path

    @staticmethod
    def random_utc_timestamp(start_year=2000, end_year=2025):
        start = int(time.mktime(time.strptime(
            f"{start_year}-04-12", "%Y-%m-%d")))
        end = int(time.mktime(time.strptime(f"{end_year}-10-31", "%Y-%m-%d")))
        return random.randint(start, end)

    def count_decrypted_words(self, output_path):
        # Datei lesen
        with open(output_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Lösung für dieses Level immer 443.jpg
        return "443.jpg"
