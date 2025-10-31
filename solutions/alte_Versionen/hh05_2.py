# Beispielloesung Level 2

def run(wo, was="flag="):
    bild = open(wo, encoding="ISO-8859-1", mode="r")
    search = was
    try:
        txt = ""
        byte = bild.read(1)
        while byte != "":
            txt = txt + byte
            byte = bild.read(1)
        pos = txt.find(search)
        pos = pos + len(search)
        with open("tmp.txt", 'w') as tmp: # gefundenen Schlüssel zwischenspeichern
            tmp.writelines(txt[pos:])
        return txt[pos:]
    except:
        bild.close()
