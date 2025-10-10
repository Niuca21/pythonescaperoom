import random
import string
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

    def create_level2(self):
        task_messages = ["Your encrypted file wird hier benannt, finde das"
                         ]
        hints = ["Look carefully in the file."]
        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.solution_level2, "/static/output1.txt"
            "data": "/static/output.txt"
        }

# Level 1. Aufgabe
    def ascii_cockie(self):
        return "67 111 111 107 105 101 109 111 110 115 116 101 114"

    def solution_level1(self, cockie):
        return "".join(chr(int(n)) for n in cockie.split())

 # Level 3 (Difficult - Veronika)

    placeholders = ["{key1}", "{key2}", "{key3}"]
    utc_list = []
    path = "/static/template.txt"
    output_path = "/static/output_decr.txt"
    name_of_file = "/static/name_of_file.txt"

    # Level 3 solution

    def solution_level2(self, path, output_path, name_of_file):
        # Generate random UTCs
        self.utc_list = [
            f"-{self.random_utc_timestamp()}" for _ in self.placeholders]

    # Replace placeholders in the file
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        for ph, utc in zip(self.placeholders, self.utc_list):
            text = text.replace(ph, utc)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)

        # Count occurrences and replace in output
        counts = {utc: text.count(utc) for utc in self.utc_list}

        for utc, count in counts.items():
            text = text.replace(utc, f"{count}")

        with open(name_of_file, "w", encoding="utf-8") as f:
            f.write(text)

        # Concatenate counts into string like "433"
        name_exe = "".join(str(counts[utc]) for utc in self.utc_list)
        return name_exe

        # Random UTC helper

    @staticmethod
    def random_utc_timestamp(start_year=2000, end_year=2025):
        start = int(time.mktime(time.strptime(
            f"{start_year}-04-12", "%Y-%m-%d")))
        end = int(time.mktime(time.strptime(f"{end_year}-10-31", "%Y-%m-%d")))
        return random.randint(start, end)
