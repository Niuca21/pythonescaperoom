import random
import string
from EscapeRoom import EscapeRoom


class VerloreneRechner(EscapeRoom):

    def __init__(self, response):
        super().__init__(response)
        self.set_metadata("Nika", __name__)
        self.add_level(self.create_level1())

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
