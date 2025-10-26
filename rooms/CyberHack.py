import random
import string
import re
from EscapeRoom import EscapeRoom
from lib.log_generator import generate_logfile

class CyberHack(EscapeRoom):
    def __init__(self, response=None):
        super().__init__(response)
        self.log_data = generate_logfile(40)     # Logfile generieren 
        # Logfile speichern für andere Levels  ( Lukasz )
        with open("static/generated_log.txt", "w") as f:
            f.write(self.log_data)
        self.set_metadata("CyberHackRoom", __name__)
##        self.add_level(self.level_1)
##       self.add_level(self.level_2)
##        self.add_level(self.level_3)
        self.add_level(self.create_level4())  # Korrekt eingebunden!
        self.add_level(self.create_level6())
##        self.add_level(self.level_5)
##        self.add_level(self.level_6)


    def create_level5(self):
        log_data = self.log_data

        task_messages = [
            "<b>🧠 Level 5: Erweiterte Logfile-Analyse</b>",
            "Du hast ein umfangreiches Logfile erhalten.",
            "Deine Aufgabe: Extrahiere alle Ports und bestimme ihren Status.",
            "Zusätzlich: Zähle, wie oft ein Login für <i>admin</i> fehlgeschlagen ist.",
            "📚 Lernziele: Reguläre Ausdrücke, Bedingte Logik, Fehlerbehandlung, Kombinierte Analyse"
        ]

        hints = [
            "🔍 Nutze <code>re.findall(r\"port (\\d+)\", line)</code> für Ports.",
            "✍️ Verwende <code>if \"user login failed for user admin\" in line</code> für die Zusatzaufgabe.",
            "💡 Kombiniere Listen und Zähler in einem Dictionary."
        ]

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.check_ports_level5,
            "data": log_data
        }



    def check_ports_level5(self, log_data):
        return self.parse_logfile_extended(log_data)

    def parse_logfile_extended(self, log_text):
        results = []
        admin_fail_count = 0
        lines = log_text.strip().split("\n")

        for line in lines:
            line = line.lower().strip()

        # Zusatzaufgabe: Admin-Login-Fehler zählen
            if "user login failed for user admin" in line:
                admin_fail_count += 1

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
            "admin_login_failures": admin_fail_count
        }



    def create_level6(self):
        task_messages = [
            "<b>🧠 Level 6: Port-Säuberung</b>",
            "Du hast nun eine Liste von Ports mit Status und Gründen aus der vorherigen Analyse.",
            "Deine Aufgabe: Schließe alle Ports, die als <i>open</i> markiert sind und deren Grund <b>nicht</b> 'secure/accepted' ist.",
            "💡 Ändere den Status auf 'closed' und den Grund auf 'manually closed'.",
            "📚 Lernziele: Listenmanipulation, Bedingte Logik, Dictionaries"
        ]

        hints = [
            "🔍 Iteriere über die Liste mit einer Schleife.",
            "✍️ Verwende eine Bedingung wie <code>if entry['status'] == 'open' and entry['reason'] != 'secure/accepted'</code>.",
            "💡 Du kannst die Einträge direkt verändern oder eine neue Liste erstellen."
        ]

        # Beispielhafte Daten aus Level 5 (könnten auch dynamisch übergeben werden)
        example_data = [
            {"port": 443, "status": "open", "reason": "secure/accepted", "raw_line": "secure connection established on port 443"},
            {"port": 8080, "status": "open", "reason": "attempt/exposed/unauthorized", "raw_line": "unauthorized access attempt on port 8080"},
            {"port": 22, "status": "closed", "reason": "filtered", "raw_line": "port 22 is filtered"},
            {"port": 8443, "status": "open", "reason": "secure/accepted", "raw_line": "connection accepted on port 8443"},
            {"port": 9999, "status": "closed", "reason": "default", "raw_line": "unknown activity on port 9999"}
        ]

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.check_ports_level6,
            "data": example_data
        }

    def check_ports_level6(self, port_list):
        return self.clean_ports(port_list)

    def clean_ports(self, port_list):
        cleaned = []
        for entry in port_list:
            if entry["status"] == "open" and entry["reason"] != "secure/accepted":
                entry["status"] = "closed"
                entry["reason"] = "manually closed"
            cleaned.append(entry)
        return cleaned
