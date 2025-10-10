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
        # Simuliere ein Logfile aus Level 3
        possible_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]
        selected_ports = random.sample(possible_ports, 5)
        log_lines = []
        for port in selected_ports:
            if random.random() < 0.7:
                log_lines.append(f"[INFO] Connection attempt on port {port}")
            else:
                log_lines.append(f"[INFO] Port {port} is secure")
        log_data = "\n".join(log_lines)

        # Speichere das Logfile als Ergebnis von Level 3
        self.set_solution("level_3_output", log_data)

        # Analysiere das Logfile
        expected_ports = self.parse_logfile(log_data)

        # Speichere die erwarteten Ports für Level 5
        self.set_solution("malware_ports", expected_ports)

        # Spieler soll diese Ports extrahieren
        player_result = self.run_player_code(secret)

        if player_result == expected_ports:
            return "✅ Malware korrekt analysiert. Weiter zu Level 5."
        else:
            return f"❌ Analysefehler. Erwartet: {expected_ports}, erhalten: {player_result}"

    def parse_logfile(self, log_text):
        ports = {}
        lines = log_text.strip().split("\n")
        for line in lines:
            match = re.search(r"port (\d+)", line)
            if match:
                port = int(match.group(1))
                if "secure" in line or "closed" in line:
                    ports[port] = "closed"
                else:
                    ports[port] = "open"
        return ports
        return "Level 4 Platzhalter"

    def level_5(self, secret):
        return "Level 5 Platzhalter"

    def level_6(self, secret):
        return "Level 6 Platzhalter"
