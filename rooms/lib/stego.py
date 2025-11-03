#!/usr/bin/python3

import random
import os

# """ Steganographie
# verstecken und auslesen von Nachrichten in einem Bild.
#
# Oliver Oberdick
# """

# Hilfsfunktion nur fuer den EscapeRoom, damit unterschiedliche Bilder genutzt werden
def random_bild(ziel_bild):
	nummer = random.randint(1, 9)
	dst = ziel_bild
	src = "static/originale/Bild_Schluessel_" + str(nummer) + ".jpg"
	if os.name == 'nt':  # pruefen ob Windows
		kopierbefehl = f'copy "{src}" "{dst}"'
	else:
		kopierbefehl = f'cp "{src}" "{dst}"'
	os.system(kopierbefehl)

# Funktion zum Vorbereiten der Level
def im_bild_verstecken(bild_datei, schluessel):
    bild = open(bild_datei, encoding="ISO-8859-1", mode="a+")
    bild.write("flag=" + schluessel)
    bild.close()

# Kontrollfunktion
def im_bild_finden(bild_datei, was="flag="):
    bild = open(bild_datei, encoding="ISO-8859-1", mode="r")
    search = was
    try:
        txt = ""
        byte = bild.read(1)
        while byte != "":
            txt = txt + byte
            byte = bild.read(1)
        pos = txt.find(search) # position des suchstring finden
        pos = pos + len(search) # laenge des suchstrings ueberspringen
        with open("tmp/game.key", 'w') as tmp: # gefundenen Schluessl zwischenspeichern
            tmp.writelines(txt[pos:])
        bild.close()
        return txt[pos:]
    except:
        bild.close()

##
if __name__ == "__main__":
    pass
