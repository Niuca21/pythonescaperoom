import os
import re
import shutil
import json
from lib import cookie as COOKIE  # Funktionssammlung Veronika Level 1
from lib import text as TEXT  # Funktionssammlung Veronika Level 2
from solutions.Level5_Loesung import run
from EscapeRoom import EscapeRoom
from lib.log_generator import generate_logfile  # Lukasz
from lib.log6_analysis import check_level6_solution # lukasz
from lib.log_analysis import check_ports_level5  # Lukasz
from lib.log_analysis import parse_logfile_extended  # Lukasz
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
        # Level 2
        self.output_path = TEXT.generate_decrypted_file("static/template.txt", "static/output.txt",
                                                        ["{key1}", "{key2}", "{key3}"])  # aus Raum 2 umkopiert
        self.solution = TEXT.count_decrypted_words(
            self.output_path)

        self.key = CRYPT.schluessel_erstellen(30)  # schluessel erstellen
        self.bild = (f"static/" + self.solution)  # war "static/KEY.jpg"

        # zufälliges Bild ermitteln und umkopieren
        STEGO.random_bild(self.bild)
        STEGO.im_bild_verstecken(self.bild, self.key)

        self.verschluesselt = "static/text.crypt"
        CRYPT.schluesselanwendung_datei(
            "static/generated_log.txt", self.verschluesselt, self.key)
        shutil.copy("tmp/ausgabe_encrypt.txt", "static/ausgabe_encrypt.txt")    # Lukasz

        self.add_level(self.create_level1())  # Veronika
        self.add_level(self.create_level2())  # Veronika
        self.add_level(self.create_level3())  # Oliver
        self.add_level(self.create_level4())  # Oliver
        self.add_level(self.create_level5())  # Lukasz
        self.add_level(self.create_level6())  # Lukasz


        print(f"DEBUG: Anzahl Levels im Raum = {len(self.get_levels())}")

    ### LEVELS ###
    # ---------------------------
    # Level 1 (Mittel - Veronika)
    # ---------------------------
    def create_level1(self):
        cookie_data = COOKIE.read_cookie("static/cookie.json")
        cookie_str = COOKIE.get_random_cookie(cookie_data)
        flask_secret = os.getenv("FLASK_SECRET_KEY")
        auth_number = COOKIE.combine_cookie_and_secret(
            cookie_str, flask_secret)

        gamename = f"Diese Cookies sind nicht lecker"
        task_messages = [
            "Hey Buddy — ich habe die Kontrolle übernommen. "
            "Willst du dein Admin-Konto zurück? Folge den Hinweisen, um deinen Authentifizierungscode zu berechnen."
            "Aufgabe: Finde zwei Werte: den Session-Token (aus dem Cookie) und ein Geheimnis in der Datei .env."
            "Verwandle beide Fundstellen in Zahlen: in jedem Fall summierst du die ASCII-Codes der jeweiligen Zeichenfolgen."
            "Bildet für beide Summen jeweils eine Zahl (sum_cookie und sum_secret), verbinde sie mit einem Doppelpunkt → 'sum_cookie:sum_secret'."
            "Berechne den SHA-256-Hash dieses Strings. Die ersten 12 Zeichen des Hex-Digests sind dein Authentifizierungscode."
        ]

        hints = [
            "Finde den Session-Token (Cookie) im Browser und entdecke die Schwachstelle in der versehentlich gelassenen Datei .env .",
            "Öffne die Datei im Browser in einem neuen Tab: http://127.0.0.1:5001/.env",
            "So führst du die Function aus: 'python def run(eingabe):'"
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
    # Level 2 (Schwierig - Veronika)
    # ---------------------------

    def create_level2(self):
        gamename = "Textdatei mit Nebenwirkungen"
        path = "static/template.txt"
        placeholders = ["{key1}", "{key2}", "{key3}"]
        decrypted_path = TEXT.generate_decrypted_file(
            path, self.output_path, placeholders)

        task_messages = [
            "In dieser Nachricht versteckt sich der Schlüssel zu deinem Bild:",
            f"<a href='{decrypted_path}' target='_blank'>Geheimtext öffnen</a>",
            "Zähle sorgfältig, wie oft jede UTC-Zahl vorkommt, und kombiniere sie zu einer Dateiendung.",
            "Verwende den Wert des frühesten Datums zuerst, den des spätesten Datums zuletzt, und kombiniere die Zählungen zu einem Dateinamen (z. B. 443.jpg)."
        ]

        hints = [
            "Jede Zahl endet mit 'UTC'. Entferne ' UTC', bevor du sie weiterverarbeitest.",
            "Beachte: etwa 20 prozent der Zahlen können absichtlich fehlerhaft sein (z.B. '1' → 'I', '0' → 'o'). Korrigiere sie, bevor du zählst.",
            "Zähle, wie oft jeder UTC-Timestamp vorkommt. Ein Dictionary oder collections.Counter ist hilfreich.",
            "Wandle die Zahlen in Integer um und finde das kleinste und das größte Datum.",
            "Die Zählung des frühesten Datums kommt zuerst, die des spätesten Datums zuletzt für den Dateinamen.",
            "Kombiniere die beiden Zahlen zu einem String und hänge '.jpg' an, z.B. '443.jpg'.",
            "Führe die Funktion so aus: `def run(path): return dateiname`."
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
            "Du hast eine Dateinamen bekommen " + self.bild,
            "(Eingabe für das Rätsel), schon eine Idee?",
            "  <img src=" + self.bild + " alt='The Key you looking for' height='150'/> ",
            "dies ist zwar kein CTF, aber ein \"flag=\" gilt es trotzdem zu finden!",
        ]
        hints = [
            "schau mal im Bild!",
            "suche nach dem \"flag=\" ",
            "als encoding wurde 'ISO-8859-1' verwendet",
            "speichern des Teils hinter \"flag=\" kann nicht schaden, Bsp. game.key",
            "mit jedem neuanfang, bekommst du auch ein anderes Bild und eine neue \"flag=\"! ",
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
            "Neben dem Bild war da noch eine andere Datei ",
            self.verschluesselt,
            "(Eingabe für das Rätsel), schon mal reingeschaut?",
            f"<a href='{self.verschluesselt}' target='_blank'>" +
            self.verschluesselt + "</a> öffnen",
        ]
        hints = [
            "Der Inhalt scheint verschlüsselt zu sein",
            "Hattest du den Schlüssel abgespeichert? Bsp. game.key?",
            "Bitweise XOR verknüpfung vom Inhalt der Datei mit dem Schlüssel (\"flag=\") aus vorherigem Rätsel.",
            "den Key kannst du auch mehrfach hintereinander schreiben, falls er nicht lang genug ist!",
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
    # Level 5 (Lukasz)
    # ---------------------------
    def create_level5(self):
        gamename = f"Erweiterte Logfile-Analyse"
        log_data = "tmp/ausgabe_encrypt.txt"
    # Speichere die Analyse für Level 6
        self.level5_result = json.loads(check_ports_level5(log_data))

        log_text = open("tmp/ausgabe_encrypt.txt", "r", encoding="utf-8").read()

        print("=== Deine Lösung ===")
        print(parse_logfile_extended(log_text))

        print("=== Musterlösung ===")
        print(run(log_text))



        task_messages = [
            "<b>🧠 Level 5: Erweiterte Logfile-Analyse</b>",
            "Du hast ein umfangreiches Logfile erhalten, das verschiedene Netzwerk- und Systemereignisse enthält.",
            "Deine Aufgabe:",
            "🔍 Analysiere das Logfile und finde wichtige Informationen:",
            "1️⃣ Extrahiere alle Ports und bestimme ihren Status. (open/closed) sowie den Grund.",
            "2️⃣ Zähle, wie oft ein Login für <i>admin</i> fehlgeschlagen ist.",
            "3️⃣ Liste alle Zeilen auf, die eine <i>Firewall-Regel</i> enthalten.",
            "4️⃣ Extrahiere alle eindeutigen IP-Adressen.",
            "5️⃣ Erstelle eine Statistik: offene und geschlossene Ports zählen, Firewall-Ports sortieren.",
            "📚 Lernziele: Reguläre Ausdrücke, Bedingte Logik, Fehlerbehandlung, Kombinierte Analyse, Listen und Dictionaries"
        ]

        hints = [
            "🔍 Nutze <code>re.findall(r\"port (\\d+)\", line)</code>, um Portnummern zu extrahieren.",
            "✍️ Verwende <code>if \"user login failed for user admin\" in line</code>, um gezielt Admin-Fehler zu zählen.",
            "🧱 Verwende <code>if \"firewall rule updated\" in line</code>, um Firewall-Zeilen zu erfassen.",
            "✅ Gib ein JSON-String zurück mit den Schlüsseln: <code>ports</code>, <code>admin_login_failures</code>, <code>firewall_rules</code>, <code>firewall_ports_sorted</code>, <code>ip_addresses</code>, <code>stats</code>.",
            "<br><b>Öffne das Logfile im Browser:</b> <a href='/static/ausgabe_encrypt.txt' target='_blank'>Logfile anzeigen</a>",
        ]

        print(f"DEBUG: Level 5 geladen mit Datenquelle = {log_data}")

        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": check_ports_level5,
            "data": log_data
        }

    # ---------------------------
    # Level 6 (Lukasz)
    # ---------------------------
    def create_level6(self):
        gamename = "Port-Säuberung & Firewall-Wiederherstellung"

        task_messages = [
            "<b>🧠 Level 6: Port-Säuberung & Firewall-Wiederherstellung</b>",
            "Du hast die Analyse aus Level 5 abgeschlossen. Jetzt musst du aktiv werden:",
            "1️⃣ Schließe alle Ports, die als <i>open</i> markiert sind und deren Grund nicht 'secure/accepted' ist.",
            "2️⃣ Stelle die Firewall-Regeln aus Level 5 wieder auf ihren ursprünglichen Wert zurück (z. B. entferne 'allow').",
            "✅ Entferne doppelte Firewall-Regeln.",
            "3️⃣ Wenn mehr als 2 fehlgeschlagene Admin-Logins erkannt wurden, entsperre den Admin-Account und füge eine Warnung hinzu.",
            "✅ Gib zusätzlich eine Statistik zurück: Anzahl geschlossener Ports und wiederhergestellter Regeln.",
            "📚 Lernziele: Listenmanipulation, Bedingte Logik, Validierung, JSON-Ausgabe."
        ]

        hints = [
            "🔍 Nutze die Daten aus Level 5: <code>ports</code>, <code>firewall_rules</code>, <code>admin_login_failures</code>.",
            "✍️ Verwende Bedingungen wie <code>if entry['status'] == 'open' and entry['reason'] != 'secure/accepted'</code>.",
            "✍️ Verwende rule.replace('updated: allow', 'restored:'), um die Firewall-Regeln wiederherzustellen."
            "🧱 Entferne Duplikate mit <code>if rule not in restored_firewall_rules</code>.",
            "📊 Gib ein JSON-String zurück mit den Schlüsseln: <code>ports</code>, <code>firewall_rules_restored</code>, <code>alert</code>, <code>admin_account</code>, <code>stats</code>."
            "ℹ️ Hinweis: Falls der Vergleich beim ersten Versuch fehlschlägt, sprüfe den Level noch einmal mit derselben Datei."
        ]



   # Daten aus Level 5 holen und JSON in Dict umwandeln
        data_from_level5 = getattr(self, "level5_result", {})

        # Sortierung für deterministische Eingabe
        if "ports" in data_from_level5:
            data_from_level5["ports"].sort(key=lambda x: (x["port"], x["status"], x["reason"]))
        if "firewall_rules" in data_from_level5:
            data_from_level5["firewall_rules"].sort()


        print("DEBUG: Level 6 geladen")
        print("DEBUG: Daten aus Level 5 (nach JSON-Umwandlung):")
        print(json.dumps(data_from_level5, indent=2))

        return {
            "gamename": gamename,
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": check_level6_solution,
            "data": data_from_level5
        }

