import random
import string
from EscapeRoom import EscapeRoom

class CyberHackRoom(EscapeRoom):
    def __init__(self):
        super().__init__()
        self.set_metadata("CyberHackRoom", __name__)
        self.add_level(self.level_1)
        self.add_level(self.level_2)
        self.add_level(self.level_3)
        self.add_level(self.level_4)
        self.add_level(self.level_5)
        self.add_level(self.level_6)

    def level_1(self, secret):
        return "Level 1 Platzhalter"

    def level_2(self, secret):
        return "Level 2 Platzhalter"

    def level_3(self, secret):
        return "Level 3 Platzhalter"

    def level_4(self, secret):
        return "Level 4 Platzhalter"

    def level_5(self, secret):
    # Hole das Logfile aus Level 3
    log_data = self.get_solution("level_3_output")

    # Berechne die Musterlösung dynamisch aus dem Logfile
    expected_ports = self.parse_logfile(log_data)

    # Speichere die erwarteten Ports für Level 5
    self.set_solution("malware_ports", expected_ports)

    # Spieler soll diese Ports extrahieren
    player_result = self.run_player_code(secret)

    if player_result == expected_ports:
        return "✅ Malware korrekt analysiert. Weiter zu Level 5."
    else:
        return f"❌ Analysefehler. Erwartet: {expected_ports}, erhalten: {player_result}"


    def parse_logfile(log_text):
        ports = []
        lines = log_text.strip().split("\n")

        for line in lines:
          line = line.lower().strip()  # Normalisierung

          matches = re.findall(r"port (\d+)", line)
        for match in matches:
            port = int(match)

            # Status-Erkennung anhand erweiterter Schlüsselwörter
            if "secure" in line or "accepted" in line:
                status = "open"
                reason = "secure/accepted"
            elif "attempt" in line or "exposed" in line or "unauthorized" in line:
                status = "open"
                reason = "attempt/exposed/unauthorized"
            elif "filtered" in line:
                status = "unbekannt"
                reason = "filtered"
            else:
                status = "closed"
                reason = "default"

            results.append({
                "port": port,
                "status": status,
                "reason": reason,
                "raw_line": line  # optional: für spätere Analyse
            })


        return ports
        return "Level 4 Platzhalter"

    def level_6(self, secret):
    # Hole die Portliste aus Level 5
    port_list = self.get_solution("malware_ports")

    # Spieler-Code ausführen
    player_result = self.run_player_code(secret)

    # Erwartete Lösung: alle gefährlichen offenen Ports geschlossen
    expected_result = []
    for entry in port_list:
        updated = entry.copy()
        if updated["status"] == "open" and updated["reason"] == "attempt/exposed/unauthorized":
            updated["status"] = "closed"
        expected_result.append(updated)

    if player_result == expected_result:
        return "✅ Alle gefährlichen Ports wurden erfolgreich geschlossen. Weiter zu Level 6!"
    else:
        return f"❌ Nicht alle gefährlichen Ports wurden korrekt geschlossen.\nErwartet: {expected_result}\nErhalten: {player_result}"

    def level_6(self, secret):
        return "Level 6 Platzhalter"
