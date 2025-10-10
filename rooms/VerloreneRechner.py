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

#   LEVELS
# Level 1 (Easy - Veronika)

    def create_level1(self):
        cockie = self.ascii_cockie()
        task_messages = [
            "Hey Buddy, ich habe jetzt die Kontrolle. ",
            "Deine Dateien sind verschlüsselt. ",
            "Wenn du dein Passwort wiederhaben willst, folge den Anweisungen.",
            "Hier ist mein Wallet: Diese Cockies sind nicht lecker!"
        ]

        hints = [
            "Schaue die Webseite an und danach stelle fest, sind die Cockies lecker und was die Gangster mit ASCII zu tun haben."
        ]

        self.response.set_cookie("hint", cockie)

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.solution_level1,
            "data": cockie
        }

    # Level 1. Aufgabe
    def ascii_cockie(self):
        return "67 111 111 107 105 101 109 111 110 115 116 101 114"

    def solution_level1(self, cockie):
        return "".join(chr(int(n)) for n in cockie.split())

    def create_level2(self):
        # Define file paths
        path = "static/template.txt"
        output_path = "static/output.txt"

        # Define placeholders
        self.placeholders = ["{key1}", "{key2}", "{key3}"]

        # Generate decrypted file
        decrypted_path = self.generate_decrypted_file(path, output_path)

        # Count occurrences for internal testing
        solution = self.count_decrypted_words(output_path)
        print("Level 2 solution:", solution)  # z. B. "343"

        # Messages for the user
        task_messages = [
            "Your encrypted file wird hier benannt, finde das unten:",
            f"<a href='{decrypted_path}' target='_blank'>Nachrichten ansehen</a>"
        ]

        hints = [
            "Schreibe deine Lösung so, dass du die Endausgabe Datei liest und die UTC-Zahlen ersetzt."
        ]

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.count_decrypted_words,  # This should be your checker
            "data": decrypted_path
        }

    def generate_decrypted_file(self, template_path, output_path):
        # Generate UTCs and save as instance variable
        self.utc_list = [
            f"-{self.random_utc_timestamp()}" for _ in self.placeholders]

        with open(template_path, "r", encoding="utf-8") as f:
            text = f.read()

        for ph, utc in zip(self.placeholders, self.utc_list):
            text = text.replace(ph, utc)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        return output_path

    def count_decrypted_words(self, output_path):
        # Datei lesen
        with open(output_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Alle UTCs im Text finden
        utc_list = re.findall(r"-\d+", text)

        # Vorkommen zählen
        counts = {utc: text.count(utc) for utc in utc_list}

        for utc, count in counts.items():
            text = text.replace(utc, f"{count}")

        # Concatenate counts into string like "433"
        name_exe = "".join(str(counts[utc]) for utc in utc_list)
        return name_exe

    @staticmethod
    def random_utc_timestamp(start_year=2000, end_year=2025):
        start = int(time.mktime(time.strptime(
            f"{start_year}-04-12", "%Y-%m-%d")))
        end = int(time.mktime(time.strptime(f"{end_year}-10-31", "%Y-%m-%d")))
        return random.randint(start, end)
