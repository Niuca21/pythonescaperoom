# Beispiell�sung Level 3

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
        pos = pos + len(search) # l�nge des suchstrings �berspringen
        with open("tmp.txt", 'w') as tmp: # Schl�ssel f�r sp�ter speichern
            tmp.writelines(txt[pos:])
        return txt[pos:]
    except:
        bild.close()
