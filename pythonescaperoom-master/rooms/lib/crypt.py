#!/usr/bin/python3

import random

# """ Verschlüsselung 
# Symetrische Verschluesselung mittels XOR auf Bit-Basis
#
# Oliver Oberdick Matrikel:548933
# """

# Hilfsfunktion zum erstellen eines Verschluesselungs key in beliebiger laenge
def schluessel_erstellen(laenge):
        ergebnis = ""
        while len(ergebnis) < laenge:
            zahl = random.randint(48, 122)
            if ((zahl >= 48 and zahl <= 57) or (zahl >= 65 and zahl <= 90) or (zahl >= 97 and zahl <= 122)):
				#  Damit der Schluessel nur aus Zahlen, Grossbuchstaben und Kleinbuchstaben besteht
                ergebnis += chr(zahl)
        return ergebnis

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

# Ver oder Entschluesseln eines String mittels XOR (Symetrisch)
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

# erweiterung, damit auch Dateien ver und entschluesselt werden koennen
def schluesselanwendung_datei(eingabe_datei, ausgabe_datei, schluessel):
	counter = 0  # nur zur kontrolle
	ergebnis = ""  # nur zur kontrolle
	with open(eingabe_datei, 'r') as in_file:
		with open(ausgabe_datei, 'w') as out_file:
			for line in in_file.read():
				counter += 1  # nur zur kontrolle
				tmp = schluesselanwendung(line, schluessel)
				out_file.write(tmp)
				if (counter >= 20 and counter >= 70): # nur zur kontrolle
					ergebnis += tmp # nur zur kontrolle
	return ergebnis # nur zur kontrolle im EscapeRoom Spiel

# Angepasste Funktion, damit zum entschluesseln der Schluessel aus einer Daten genutzt werden kann
def entschluesseln(eingabe, ausgabe="tmp/ausgabe_encrypt.txt", schluessel="tmp/game.key"):
	key = ""
	with open(schluessel, "r") as f:
		key = f.readline()
	return schluesselanwendung_datei(eingabe, ausgabe, key)

##
if __name__ == "__main__":

	key1 = schluessel_erstellen(20)
	key2 = schluessel_erstellen(20)

	print(key1)
	print(key2)

	text = "Hallo du da im Radio!"

	print("Original Text")
	print(text)
	print("Verschluesselt mit Key1")
	text_verschluesselt = schluesselanwendung(text, key1)
	print(text_verschluesselt)
	print("Entschluesselt mit Key1")
	text_entschluesselt = schluesselanwendung(text_verschluesselt, key1)
	print(text_entschluesselt)
	print("entschluesselt mit Key2")
	text_entschluesselt = schluesselanwendung(text_verschluesselt, key2)
	print(text_entschluesselt + "  - mit falschem Key")

	print("-------------------------------------")

	schluesselanwendung_datei("test.txt", "test.crypt", key1)

	schluesselanwendung_datei("test.crypt", "test_entcript.txt", key1)

	print("Dateien fertig")
