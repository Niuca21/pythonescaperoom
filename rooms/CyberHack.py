import random
import string
import re
from EscapeRoom import EscapeRoom

class CyberHack(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("CyberHackRoom", __name__)
##        self.add_level(self.level_1)
##       self.add_level(self.level_2)
##        self.add_level(self.level_3)
        self.add_level(self.create_level4())  # Korrekt eingebunden!
##        self.add_level(self.level_5)
##        self.add_level(self.level_6)

    def create_level4(self):
        log_data = """
        Secure connection established on port 443
        Unauthorized access attempt on port 8080
        Port 22 is filtered
        Connection accepted on port 8443
        Unknown activity on port 9999
        """

        parsed_ports = self.parse_logfile(log_data)
        self.set_solution("malware_ports", parsed_ports)

        task_messages = [
            "<b>🧠 Level 4: Logfile-Analyse</b>",
            "Du hast ein Logfile erhalten, das verdächtige Netzwerkaktivitäten enthält.",
            "Deine Aufgabe: Extrahiere alle Ports aus dem Logfile und bestimme ihren Status.",
            "💡 Achte auf Schlüsselwörter wie <i>secure</i>, <i>attempt</i>, <i>filtered</i>.",
            "📚 Lernziele: Textanalyse, Reguläre Ausdrücke, Listen und Dictionaries"
        ]

        hints = [
            "🔍 Nutze <code>re.findall(r\"port (\\d+)\", line)</code>, um Portnummern zu extrahieren.",
            "✍️ Verwende <code>line.lower().strip()</code>, um die Zeile zu normalisieren.",
            "💡 Prüfe mit <code>if</code>, ob bestimmte Schlüsselwörter enthalten sind."
        ]

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.check_ports_level4,
            "data": log_data
        }

    def check_ports_level4(self, log_data):
        return self.parse_logfile(log_data)

    def parse_logfile(self, log_text):
        results = []
        lines = log_text.strip().split("\n")

        for line in lines:
            line = line.lower().strip()
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

        return results
