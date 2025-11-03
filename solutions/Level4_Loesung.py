# Beispiellösung Level 4: Oliver
#------------------------
#  Lernziele:
#    Verketten von Strings: der gefundene Verschlüsselungskey muß für eine Erfolgreiche Entschlüsselung mehrfach hintereinander gesetzt werden, da die Nachricht meist länger als der Schlüssel ist.
#    wandlung in Binär-Format: Damit ein String auf Bit-Ebene Entschlüsselt werden kann, müßen die Strings ins Binärformat und wieder zurück gewandelt werden.
#    Bitweise XOR verknüpfung: Verknüpfen der Binären ketten mittels einer "Exklusiv oder" verknüpfung, zur Symetrischen ver./entschlüsselung mittels eines Schlüssel/Password/Zeichenketten.
#    Arbeiten mit Funktionen: Aufteilen des Codes in einzelne Funktionen, damit Code nicht Kopiert werden muß, wenn dieser mehrfach verwendet wird. Bsp. bei der Umwandlung von Strings in Binärfolgen für die Nachricht und den ver./entschlüsselungsschlüssel.

def run(eingabe):
	return schluesselanwendung_datei(eingabe, "ausgabe_encrypt.txt", "tmp.txt")

def string_to_binaer(nachricht):
	ergebnis = ""
	for c in nachricht:
		ergebnis += ''.join(format(ord(c), '08b'))
	return ergebnis

def binaer_to_string(nachricht):
	ergebnis = ""	
	for i in range(0, len(nachricht), 8):
		ergebnis += chr(int(nachricht[i: i+8], 2))
	return ergebnis

# Symmetrische Verschlüsselung
# Bitweises verschlüsseln und entschlüsseln
def schluesselanwendung(was, womit):
	ergebnis = ""
	schluessel = ""
	while len(schluessel) < len(was):
		schluessel += womit
	binaer_schluessel = string_to_binaer(schluessel)
	binaer_nachricht = string_to_binaer(was)
	for i in range(len(binaer_nachricht)):
		ergebnis += str(int(binaer_nachricht[i]) ^ int(binaer_schluessel[i]))
	return binaer_to_string(ergebnis)

# Anwendung der verschlüsselung & entschlüsselung auf den Inhalt einer Datei
def schluesselanwendung_datei(eingabe_datei, ausgabe_datei, schluessel):
	key = ""
	with open(schluessel, "r") as f:
		key = f.readline()
	ergebnis = ""
	with open(eingabe_datei, 'r') as in_file:
		with open(ausgabe_datei, 'w') as out_file:
			for line in in_file.read():
				tmp = schluesselanwendung(line, key)
				out_file.write(tmp)
				ergebnis += tmp
	return ergebnis
