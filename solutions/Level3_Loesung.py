# Beispiellösung Level 3: Oliver
#------------------------
#  Lernziele:
#    Dateien lesen & schreiben: einlesen einer Bild-Datei und schreiben einer Text-Datei als zwischenspeicher für einen Endschlüsselungs-Schlüssel
#    durchsuchen von Dateien: Vorgegebenen Suchstring in der Bild-Datei ausfindig machen.
#    Sting nach Muster aufteilen: gefundenen String in separate Teilstrings aufteilen und den relevanten in einer Text-Datei zwischenspeichern.

def run(wo, was="flag="):
    bild = open(wo, encoding="ISO-8859-1", mode="r")
    search = was
    try:
        txt = ""
        byte = bild.read(1)
        while byte != "":
            txt = txt + byte
            byte = bild.read(1)
        pos = txt.find(search) # position des suchstring finden
        pos = pos + len(search) # länge des suchstrings überspringen
        with open("tmp.txt", 'w') as tmp: # Schlüssel für später speichern
            tmp.writelines(txt[pos:])
        return txt[pos:]
    except:
        bild.close()
