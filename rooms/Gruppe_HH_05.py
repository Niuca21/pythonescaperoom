import os
import random
import time
import re
from lib import cookie as COOKIE
from lib import text as TEXT

from EscapeRoom import EscapeRoom
from lib.log_generator import generate_logfile  # Lukasz
import lib.stego as STEGO  # Funktionssammlung Oliver Level 3
import lib.crypt as CRYPT  # Funktionssammlung Oliver Level 4


class Gruppe_HH_05(EscapeRoom):

    def __init__(self, response=None):
        super().__init__(response)
        self.set_metadata("Veronika, Lukasz & Oliver", __name__)

        self.log_data = generate_logfile(40)     # Logfile generieren Lukasz
        # Logfile speichern für andere Levels  ( Lukasz )
        with open("static/generated_log.txt", "w") as f:
            f.write(self.log_data)

        self.output_path = "static/output.txt"  # aus Raum 2 umkopiert
        self.solution = TEXT.count_decrypted_words(
            self.output_path)  # aus Raum 2 umkopiert

        self.key = CRYPT.schluessel_erstellen(30)  # schluessel erstellen
        self.bild = (f"static/" + self.solution)  # war "static/KEY.jpg"

        # zufälliges Bild ermitteln und umkopieren
        STEGO.random_bild(self.bild)
        STEGO.im_bild_verstecken(self.bild, self.key)

        self.verschluesselt = "static/text.crypt"
        CRYPT.schluesselanwendung_datei(
            "static/generated_log.txt", self.verschluesselt, self.key)

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
        cookie_data = COOKIE.read_cookie("static/cookie.json")

        cookie_str = COOKIE.get_random_cookie(cookie_data)
        flask_secret = os.getenv("FLASK_SECRET_KEY")
        auth_number = COOKIE.combine_cookie_and_secret(
            cookie_str, flask_secret)

        gamename = f"Diese Cookies sind nicht lecker"
        task_messages = [
            "Hey Buddy, ich habe jetzt die Kontrolle. ",
            "Deine Dateien sind verschluesselt. :)",
            "Finde zwei Werte: den Session-Token (Cookie) und die Schwachstelle in der Datei /.env",
            "Manipuliere deine Strings so das du alle gefundene ASCII-Werte (z. B. '67 111 107' und '45 54') summierst und nachdem Modulo 1000 rechnest.",
        ]

        hints = [
            "Finde den Session-Token (Cookie) im Browser und entdecke die Schwachstelle in der versehentlich gelassenen Datei .env . Öffne die Datei im Browser in einem neuen Tab: http://127.0.0.1:5001/.env"
        ]

        self.response.set_cookie("hint", cookie_str)

        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": lambda x: auth_number,
            "data": cookie_str
        }

    # ---------------------------
    # Level 1 (Easy - Solution)
    # ---------------------------
    # def solution_level1(self, actual_solution) -> str:
    #    return actual_solution
    # ---------------------------
    # Level 2 (Schwierig - Veronika)
    # ---------------------------

    def create_level2(self):
        gamename = "Textdatei mit Nebenwirkungen"

        path = "static/template.txt"
# output_path = "static/output.txt" # nach Zeile 22 verschoben

        placeholders = ["{key1}", "{key2}", "{key3}"]

        decrypted_path = TEXT.generate_decrypted_file(
            path, self.output_path, placeholders)  # self.output_path

# solution = self.count_decrypted_words(   # nach Zeile 23 verschoben
# output_path)  # nach Zeile 24 verschoben
        # print("Level 2 Lösung (intern):", self.solution)  # self.solution

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
            "solution_function": TEXT.count_decrypted_words,
            "data": decrypted_path
        }

    # ---------------------------
    # Level 3 (Oliver)
    # ---------------------------
    def create_level3(self):
        gamename = f"Finde den Schlüssel"
        task_messages = [
            "  <img src=" + self.bild + " alt='The Key you looking for' height='150'/> ",
            "Hi,",
            "Jetzt hast du eine Datei " + self.bild + ", schon eine Idee?",
            "dies ist zwar kein CTF, aber ein flag ist trotzdem zu suchen!",
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
        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": STEGO.im_bild_finden,
            "data": self.bild
        }

    # ---------------------------
    # Level 4 (Oliver)
    # ---------------------------
    def create_level4(self):
        gamename = f"Entschlüssel den Datei-Inhalt"
        task_messages = [
            "Du hast jetzt einen Dateinamen " +
            self.verschluesselt + ", schon mar reingeschaut?",
            f"<a href='{self.verschluesselt}' target='_blank'>" +
            self.verschluesselt + " öffnen</a>",
        ]
        hints = [
            "kannst du den Inhalt lesen?",
            "Hattest du die flag gespeichert? Bsp. game.key?",
            "Bitweises XOR schon mal gesehen?",
            "Denke drann den Inhalt des Key.File zu nutzen, nicht den Dateinamen",
            "den Key kannst du auch mehrfach hintereinander schreiben, falls er nicht lang genug ist",
            "trotzdem solltest du die komplette Datei bearbeiten und auch wieder speichern. Bsp. ausgabe_encrypt.txt"
        ]
        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": CRYPT.entschluesseln,
            "data": self.verschluesselt
        }

    # ---------------------------
    # Level 5 (Lucasz)
    # ---------------------------
    def create_level5(self):
        gamename = f"Erweiterte Logfile-Analyse"
# log_data = self.log_data
        log_data = "tmp/ausgabe_encrypt.txt"
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

    # ---------------------------
    # Level 6 (Lucasz)
    # ---------------------------
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
    # def solution_level1(self, auth_number) -> str:
    #    return auth_number
    #    return "".join(chr(int(n)) for n in cookie.split())

    # ---------------------------
    # Level 3 (Oliver)
    # Die Hilfsfunktionen für Level 3 befinden sich in der Datei rooms/lib/stego.py
    # Importiert mit: import lib.stego as STEGO
    # ---------------------------

    # ---------------------------
    # Level 4 (Oliver)
    # Die Hilfsfunktionen für Level 4 befinden sich in der Datei rooms/lib/crypt.py
    # Importiert mit: import lib.stego as CRYPT
    # ---------------------------

    # ---------------------------
    # Level 5 (Lucasz)
    # ---------------------------

    def check_ports_level5(self, log_data):
        result = self.parse_logfile_extended(log_data)
        self.level5_result = result  # Speichere für Level 6
        return result

    def parse_logfile_extended(self, log_text):
        results = []
        admin_fail_count = 0
        firewall_rules = []
        lines = log_text.strip().split("\n")

        for line in lines:
            line = line.lower().strip()

        # Zusatzaufgabe: Admin-Login-Fehler zählen
            if "user login failed for user admin" in line:
                admin_fail_count += 1

        # Zusatzaufgabe: Firewall-Regeln sammeln
            if "firewall rule updated" in line:
                firewall_rules.append(line)

        # Port-Analyse
            matches = re.findall(r"port (\d+)", line)
            for match in matches:
                port = int(match)
                if "secure" in line or "accepted" in line:
                    status = "open"
                    reason = "secure/accepted"
                elif "attempt" in line or "exposed" in line or "unauthorized" in line:
                    status = "open"
                    reason = "attempt/exposed/unauthorized"
                elif "filtered" in line:
                    status = "closed"
                    reason = "filtered"
                else:
                    status = "closed"
                    reason = "default"

                results.append({
                    "port": port,
                    "status": status,
                    "reason": reason,
                    "raw_line": line
                })

        return {
            "ports": results,
            "admin_login_failures": admin_fail_count,
            "firewall_rules": firewall_rules
        }

    # ---------------------------
    # Level 6 (Lucasz)
    # ---------------------------
    def check_level6_solution(self, data):
        ports = data["ports"]
        firewall_rules = data["firewall_rules"]
        admin_failures = data["admin_login_failures"]

    # 1. Ports schließen
        for entry in ports:
            if entry["status"] == "open" and entry["reason"] != "secure/accepted":
                entry["status"] = "closed"
                entry["reason"] = "manually closed"

    # 2. Firewall-Regeln wiederherstellen (z. B. 'allow' entfernen)
        restored_firewall_rules = []
        for rule in firewall_rules:
            # Beispiel: "Firewall rule updated: allow port 80" -> "Firewall rule restored: port 80"
            restored_rule = rule.replace("updated: allow", "restored:")
            restored_firewall_rules.append(restored_rule)

    # 3. Admin-Account entsperren + Warnung
        alert = None
        admin_account = None
        if admin_failures > 2:
            alert = "ALERT: Too many admin login failures"
            admin_account = "unlocked"

        return {
            "ports": ports,
            "firewall_rules_restored": restored_firewall_rules,
            "alert": alert,
            "admin_account": admin_account
        }
