import random
import string
from EscapeRoom import EscapeRoom

import lib.stego as STEGO # Funktionssammlung Oliver Level 2
import lib.crypt as CRYPT # Funktionssammlung Oliver Level 4

class Gruppe_HH_05(EscapeRoom):

    def __init__(self):
        super().__init__()
        self.set_metadata("Veronika, Lucasz & Oliver", __name__)
        self.key = CRYPT.schluessel_erstellen(30) #schluessel erstellen
        self.bild = "static/KEY.jpg"
        STEGO.random_bild(self.bild) # zufälliges Bild ermitteln und umkopieren
        STEGO.im_bild_verstecken(self.bild , self.key)
        self.verschluesselt = "static/text.crypt"
        CRYPT.schluesselanwendung_datei("static/originale/test.log" ,self.verschluesselt ,self.key )
        
        self.add_level(self.create_level1()) # Veronika
        self.add_level(self.create_level2()) # Oliver
        self.add_level(self.create_level3()) # Veronika
        self.add_level(self.create_level4()) # Oliver
        self.add_level(self.create_level5()) # Lucasz
        self.add_level(self.create_level6()) # Lucasz

    ### LEVELS ###
    # Level 1
    def create_level1(self):
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
            "speichern kann nicht schaden, Vorschlag game.key",
            "als encoding wurde 'ISO-8859-1' verwendet",
            "in einem Linux Terminal funktioniert auch der Befehl 'strings [Dateiname]' "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": STEGO.im_bild_finden, "data": self.bild}

    # Level 2
    def create_level2(self):
        task_messages = [
            "  <img src=" + self.bild + " alt='The Key you looking for' height='150'/> ",
            "Hi,",
			"das ist zwar kein CTF, aber ein flag ist trotzdem zu suchen"
        ]
        hints = [
            "schau mal im Bild!",
            "suche nach dem flag= ",
            "Eingabedaten: Dateiname des Bildes",
            "mit jedem Bild oder neuanfang bekommst du auch eine andere flag",
            "speichern kann nicht schaden, Bsp. game.key",
            "als encoding wurde 'ISO-8859-1' verwendet",
            "in einem Linux Terminal funktioniert auch der Befehl 'strings [Dateiname]' "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": STEGO.im_bild_finden, "data": self.bild}

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
        task_messages = [
            "  <img src=" + self.bild + " alt='The Key you looking for' height='200'/> ",
            "Hi,",
			"das ist zwar kein CTF, aber ein flag ist trotzdem zu suchen"
        ]
        hints = [
            "schau mal im Bild!",
            "suche nach dem flag= ",
            "Eingabedaten sind der Dateiname des Bildes",
            "mit jedem Bild oder neuanfang bekommst du auch eine andere flag",
            "speichern kann nicht schaden, Vorschlag game.key",
            "als encoding wurde 'ISO-8859-1' verwendet",
            "in einem Linux Terminal funktioniert auch der Befehl 'strings [Dateiname]' "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": STEGO.im_bild_finden, "data": self.bild}

    # Level 6
    def create_level6(self):
        task_messages = [
            "  <img src=" + self.bild + " alt='The Key you looking for' height='200'/> ",
            "Hi,",
			"das ist zwar kein CTF, aber ein flag ist trotzdem zu suchen"
        ]
        hints = [
            "schau mal im Bild!",
            "suche nach dem flag= ",
            "Eingabedaten sind der Dateiname des Bildes",
            "mit jedem Bild oder neuanfang bekommst du auch eine andere flag",
            "speichern kann nicht schaden, Vorschlag game.key",
            "als encoding wurde 'ISO-8859-1' verwendet",
            "in einem Linux Terminal funktioniert auch der Befehl 'strings [Dateiname]' "
        ]
        return {"task_messages": task_messages, "hints": hints, "solution_function": STEGO.im_bild_finden, "data": self.bild}

    ### Hilfsfunktionen ###
    


    ### SOLUTIONS ###

