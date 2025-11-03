# Beispielloesung Level 4

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

def schluesselanwendung_datei(eingabe_datei, ausgabe_datei, schluessel):
	key = ""
	with open(schluessel, "r") as f:
		key = f.readline()
#	counter = 0
	ergebnis = ""
	with open(eingabe_datei, 'r') as in_file:
		with open(ausgabe_datei, 'w') as out_file:
			for line in in_file.read():
#				counter += 1
				tmp = schluesselanwendung(line, key)
				out_file.write(tmp)
#				if (counter >= 20 and counter >= 70):
				ergebnis += tmp
	return ergebnis
