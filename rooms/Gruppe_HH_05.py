import random
import string
import time
import re
from EscapeRoom import EscapeRoom
from lib.log_generator import generate_logfile  # Lukasz
import lib.stego as STEGO  # Funktionssammlung Oliver Level 3
import lib.crypt as CRYPT  # Funktionssammlung Oliver Level 4


class Gruppe_HH_05(EscapeRoom):

    def __init__(self, response=None):
        super().__init__(response)
        self.log_data = generate_logfile(40)     # Logfile generieren Lukasz 
        # Logfile speichern für andere Levels  ( Lukasz )
        with open("static/generated_log.txt", "w") as f:
            f.write(self.log_data)
        self.set_metadata("Veronika, Lukasz & Oliver", __name__)
        self.key = CRYPT.schluessel_erstellen(30)  # schluessel erstellen
        self.bild = "static/KEY.jpg"
        # zufälliges Bild ermitteln und umkopieren
        STEGO.random_bild(self.bild)
        STEGO.im_bild_verstecken(self.bild, self.key)
        self.verschluesselt = "static/text.crypt"
        CRYPT.schluesselanwendung_datei(
            "static/originale/test.log", self.verschluesselt, self.key)

        self.add_level(self.create_level1())  # Veronika
        self.add_level(self.create_level2())  # Veronika
        self.add_level(self.create_level3())  # Oliver
        self.add_level(self.create_level4())  # Oliver
        self.add_level(self.create_level5())  # Lukasz
        self.add_level(self.create_level6())  # Lukasz

    ### LEVELS ###
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

    # ---------------------------
    # Level 2 (Schwierig - Veronika)
    # ---------------------------
    def create_level2(self):
        gamename = "Textdatei mit Nebenwirkungen"

        path = "static/template.txt"
        output_path = "static/output.txt"

        self.placeholders = ["{key1}", "{key2}", "{key3}"]

        decrypted_path = self.generate_decrypted_file(
            path, output_path)

        solution = self.count_decrypted_words(
            output_path)
        print("Level 2 Lösung (intern):", solution)

        task_messages = [
            "In dieser Nachricht versteckt sich der Schlüssel zu deinem Bild:",
            f"<a href='{decrypted_path}' target='_blank'>Geheimtext öffnen</a>",
            "Zähle sorgfältig, wie oft jede UTC-Zahl vorkommt, und kombiniere sie zu einer Dateiendung. Do not count the list below."
        ]

        hints = [
            "Jede Zahl (z. B. -1338780358 UTC) zählt. Finde heraus, wie oft sie erscheint.",
            "Setze die Anzahl der Vorkommen in der Reihenfolge ihres ersten Auftretens zusammen.",
            "Beispiel: Wenn du 1, 3, 2 findest → {key1}{key2}{key3}.jpg = 133.jpg"
        ]

        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.count_decrypted_words,
            "data": decrypted_path
        }

    # Level 3

    def create_level3(self):
        task_messages = [
            "  <img src=" + self.bild + " alt='The Key you looking for' height='400'/> ",
            "Hi,",
            "das ist zwar kein CTF, aber ein flag ist trotzdem zu suchen",
        ]
        hints = [
            "schau mal im Bild!",
            "suche nach dem flag= ",
            "Eingabedaten sind der Dateiname des Bildes",
            "mit jedem Bild oder neuanfang bekommst du auch eine andere flag",
            "speichern kann nicht schaden, Bsp. game.key",
            "als encoding wurde 'ISO-8859-1' verwendet",
            "in einem Linux Terminal funktioniert auch der Befehl 'strings [Dateiname]' "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": STEGO.im_bild_finden, "data": self.bild}

    # Level 4
    def create_level4(self):
        task_messages = [
            "Du hast jetzt einen Dateinamen " +
            self.verschluesselt + ", schon mar reingeschaut?",
            "zur kontrolle, zeig mir die Zeichen 20 - 70"
        ]
        hints = [
            "kannst du den Inhalt lesen?",
            "Hattest du die flag gespeichert? Bsp. game.key?",
            "Bitweises XOR schon mal gesehen?",
            "als Rückgabewert die Zeichen 20 - 70 als String zum alsolvieren dieses Level sollten erstmal reichen",
            "Denke drann den Inhalt des Key.File zu nutzen, nicht den Dateinamen",
            "den Key kannst du auch mehrfach hintereinander schreiben, falls er nicht lang genug ist",
            "trotzdem solltest du die komplette Datei bearbeiten und auch wieder speichern. Bsp. ausgabe_encrypt.txt"
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": CRYPT.entschluesseln, "data": self.verschluesselt}

    # Level 5
        
    def create_level5(self):
        gamename = f"Erweiterte Logfile-Analyse"
        log_data = self.log_data
        # log_data = "tmp/ausgabe_encrypt.txt"
        # Wenn mit der ver und wieder Entschlüsselten Datei gearbeitet werden soll.
        # Müßte in Beispiellösung mit der Datei "ausgabe_encrypt.txt" (aus Beispiellösung für Level4)
        # und in der kontrolle mit der Datei "tmp/ausgabe_encrypt.txt" gearbeitet werden

        task_messages = [
            "<b>🧠 Level 5: Erweiterte Logfile-Analyse</b>",
            "Du hast ein umfangreiches Logfile erhalten, das verschiedene Netzwerk- und Systemereignisse enthält.",
            "Deine Aufgabe:",
            "1️⃣ Extrahiere alle Ports und bestimme ihren Status.",
            "2️⃣ Zähle, wie oft ein Login für <i>admin</i> fehlgeschlagen ist.",
            "3️⃣ Liste alle Zeilen auf, die eine <i>Firewall-Regel</i> enthalten.",
            "📚 Lernziele: Reguläre Ausdrücke, Bedingte Logik, Fehlerbehandlung, Kombinierte Analyse, Listen und Dictionaries"
        ]

        hints = [
            "🔍 Nutze <code>re.findall(r\"port (\\d+)\", line)</code>, um Portnummern zu extrahieren.",
            "✍️ Verwende <code>if \"user login failed for user admin\" in line</code>, um gezielt Admin-Fehler zu zählen.",
            "🧱 Verwende <code>if \"firewall rule updated\" in line</code>, um Firewall-Zeilen zu erfassen.",
            "💡 Gib ein Dictionary mit <code>ports</code>, <code>admin_login_failures</code> und <code>firewall_rules</code> zurück."
        ]

        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.check_ports_level5,
            "data": log_data
        }
    # Level 6

    def create_level6(self):
        gamename = "Port-Säuberung & Firewall-Wiederherstellung"

        task_messages = [
            "<b>🧠 Level 6: Port-Säuberung & Firewall-Wiederherstellung</b>",
            "Du hast die Analyse aus Level 5 abgeschlossen. Jetzt musst du aktiv werden:",
            "1️⃣ Schließe alle Ports, die als <i>open</i> markiert sind und deren Grund nicht 'secure/accepted' ist.",
            "2️⃣ Stelle die Firewall-Regeln aus Level 5 wieder auf ihren ursprünglichen Wert zurück (z. B. entferne 'allow').",
            "3️⃣ Wenn mehr als 2 fehlgeschlagene Admin-Logins erkannt wurden, entsperre den Admin-Account und füge eine Warnung hinzu.",
            "📚 Lernziele: Listenmanipulation, Bedingte Logik, Dictionaries, Kombinierte Auswertung"
        ]

        hints = [
            "🔍 Nutze die Daten aus Level 5: ports, firewall_rules, admin_login_failures.",
            "✍️ Verwende Bedingungen wie <code>if entry['status'] == 'open' and entry['reason'] != 'secure/accepted'</code>.",
            "🧱 Gib ein Dictionary zurück mit den Schlüsseln <code>ports</code>, <code>firewall_rules</code>, <code>alert</code> und <code>admin_account</code>."
        ]

    # Nutze die echte Lösung aus Level 5
        data_from_level5 = getattr(self, "level5_result", None)
        if not data_from_level5:
            data_from_level5 = {
                "ports": [],
                "admin_login_failures": 0,
                "firewall_rules": []
            }

        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.check_level6_solution,
            "data": data_from_level5
        }

    ### Hilfsfunktionen ###

    # ---------------------------
    # Level 1 (Easy - Veronika)
    # ---------------------------
    def ascii_cockie(self):
        return "67 111 111 107 105 101 109 111 110 115 116 101 114"

    def solution_level1(self, cockie):
        return "".join(chr(int(n)) for n in cockie.split())

    # ---------------------------
    # Level 2 (Schwierig - Veronika)
    # ---------------------------

    def generate_decrypted_file(self, path, output_path):
        self.utc_list = [
            f"-{self.random_utc_timestamp()}" for _ in self.placeholders]

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        for ph, utc in zip(self.placeholders, self.utc_list):
            text = text.replace(ph, utc)

        desired_counts = [4, 4, 3]
        additional_lines = []
        for utc, count in zip(self.utc_list, desired_counts):
            additional_lines.extend(
                [f"Geheimer Key seit {utc} UTC." for _ in range(count)])
        random.shuffle(additional_lines)
        text += "\n\n" + "\n".join(additional_lines)

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

        with open(output_path, "r", encoding="utf-8") as f:
            text = f.read()
        return "443.jpg"

    ### SOLUTIONS ###
