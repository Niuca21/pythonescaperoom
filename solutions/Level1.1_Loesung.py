# Beispiellösung Level 1: Veronika
# Lernziele:
# 1. Strings in Python verstehen
#    - Zugriff auf einzelne Zeichen
#    - Iteration über Strings (for n in string)
#
# 2. ASCII-Werte berechnen
#    - Funktion ord() kennenlernen
#    - Umwandlung von Zeichen in Ganzzahlen
#
#
# 3. Grundlegende mathematische Operationen
#    - Addition von Werten
#    - Bildung von zusammengesetzten Payloads
#
# 4. String-Formatierung
#    - f-Strings zur dynamischen Erstellung von Strings
#    - Zusammensetzen von Daten für Hashing
#
# 5. Kryptographie-Grundlagen (praktisch)
#    - SHA-256 Hash berechnen mit hashlib
#    - Nutzung des Hashwerts für Authentifizierung
#    - Slicing von Strings, z. B. auth_hash[:12]
import hashlib

cookie = "Telly Monster"


def run(_):
    flask_secret_ascii = [ord(
        n) for n in "adminpasssowrd"]

    cookie_values = [ord(n) for n in cookie]
    sum_cookie = sum(cookie_values)
    sum_secret = sum(flask_secret_ascii)
    payload = f"{sum_cookie}:{sum_secret}"
    auth_hash = hashlib.sha256(payload.encode()).hexdigest()
    auth_value = auth_hash[:12]

    return auth_value
