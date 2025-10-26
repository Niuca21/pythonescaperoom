import random
import string
from EscapeRoom import EscapeRoom

import time
import re
import lib.stego as STEGO # Funktionssammlung Oliver Level 3
import lib.crypt as CRYPT # Funktionssammlung Oliver Level 4

class Gruppenarbeit_kombiniert(EscapeRoom):

    def __init__(self, response=None):
        super().__init__(response)
        
        self.set_metadata("Veronika, Lucasz & Oliver", __name__)
        
        ## Fuer Level 3-4
        self.key = CRYPT.schluessel_erstellen(30) #schluessel erstellen
        self.bild = "static/KEY.jpg"
        STEGO.random_bild(self.bild) # zufaelliges Bild ermitteln und umkopieren
        STEGO.im_bild_verstecken(self.bild , self.key)
        self.verschluesselt = "static/text.crypt"
        CRYPT.schluesselanwendung_datei("static/originale/test.log" ,self.verschluesselt ,self.key )
        
        ## Fuer Level 5-6
        
        self.add_level(self.create_level1()) # Veronika
        self.add_level(self.create_level2()) # Veronika
        self.add_level(self.create_level3()) # Oliver
        self.add_level(self.create_level4()) # Oliver
        self.add_level(self.create_level5()) # Lucasz
        self.add_level(self.create_level6()) # Lucasz

    ### LEVELS ###
    # Level 1
    def create_level1(self):
        cockie = self.ascii_cockie()
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
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.solution_level1,
            "data": cockie
        }

    # Level 2
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
        print("Level 2 solution:", solution)  # z.B."343"

        # Messages for the user
        task_messages = [
            "Your encrypted file wird hier benannt, finde das unten:",
            f"<a href='{decrypted_path}' target='_blank'>Nachrichten ansehen</a>"
        ]

        hints = [
            "Schreibe deine Loesung so, dass du die Endausgabe Datei liest und die UTC-Zahlen ersetzt."
        ]

        return {
            "task_messages": task_messages,
            "hints": hints,
            "solution_function": self.count_decrypted_words,  # This should be your checker
            "data": decrypted_path
        }

    # Level 3
    def create_level3(self):
        task_messages = [
            "  <img src=" + self.bild + " alt='The Key you looking for' height='150'/> ",
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
            "Du hast jetzt einen Dateinamen " + self.verschluesselt + ", schon mar reingeschaut?",
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
        log_data = """
        Secure connection established on port 443
        Unauthorized access attempt on port 8080
        Port 22 is filtered
        Connection accepted on port 8443
        Unknown activity on port 9999
        """

        parsed_ports = self.parse_logfile(log_data)
#        self.set_solution("malware_ports", parsed_ports)

        task_messages = [
            "<b>🧠 Level 5: Logfile-Analyse</b>",
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
            "solution_function": self.check_ports_level5,
            "data": log_data
        }

    # Level 6
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

	#######################
    ### Hilfsfunktionen ###
    
        # Level 1. Aufgabe
    def ascii_cockie(self):
        return "67 111 111 107 105 101 109 111 110 115 116 101 114"

        # Level 2. Aufgabe
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

    @staticmethod
    def random_utc_timestamp(start_year=2000, end_year=2025):
        start = int(time.mktime(time.strptime(
            f"{start_year}-04-12", "%Y-%m-%d")))
        end = int(time.mktime(time.strptime(f"{end_year}-10-31", "%Y-%m-%d")))
        return random.randint(start, end)

		# Level 3. Aufgabe
	# Hilfsfunktionen befinden sich unter 
	# room/lib/stego.py

		# Level 4. Aufgabe
	# Hilfsfunktionen befinden sich unter 
	# room/lib/crypt.py

		# Level 5. Aufgabe


		# Level 6. Aufgabe


    ### SOLUTIONS ###

        # Level 1. Lösung
    def solution_level1(self, cockie):
        return "".join(chr(int(n)) for n in cockie.split())

        # Level 2. Lösung
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

		# Level 3. Lösung
	# Aufgerufene Lösungsfuktion befinden sich unter 
	# room/lib/stego.py importiert als STEGO
	# STEGO.im_bild_finden
	
		# Level 4. Lösung
	# Aufgerufene Lösungsfuktion befinden sich unter 
	# room/lib/crypt.py importiert als CRYPT
	# CRYPT.entschluesseln

		# Level 5. Lösung
    def check_ports_level5(self, log_data):
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

		# Level 6. Lösung
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
