# Spielübersicht

# Besonderheiten dieser Spiele-Version
Der Server wurde angepasst, und auf Linux, Mac & im Linux Subsystem auf Windows getestet.
Für die Nutzung auf einer reinen Windows Installation müßten in einigen Dateien, 
jeweils in den genutzten Dateipfaden, der / (Slash) gegen einen \ Backslash ausgetauscht werden.


## Anfang
Du schaltest deinen Computer ein und siehst nur ein seltsames Anmeldefenster als Gast.
Plötzlich startet ein merkwürdiges Spiel, das dir Hinweise gibt, wie du dein Admin-Konto zurückbekommst.

---

## Level 1 – Diese Cookies sind nicht lecker 

**Geschichte**

Du schaltest deinen Computer ein doch etwas stimmt nicht.
Anstatt des gewohnten Desktops erscheint nur ein fremdes Anmeldefenster: „Gastkonto aktiv.“
Jemand muss dein System verändert haben.
Noch bevor du reagieren kannst, öffnet sich automatisch dein Browser.
Ein merkwürdiges Spiel startet — und mitten auf dem Bildschirm erscheint eine Nachricht:
„Willst du dein Admin-Konto zurück? Dann folge den Hinweisen…“


**Lernziele:**

1. **Kodierung und generierte Zeichenketten:** Die Zeichenketen werden dabei im Browser verborgen.
2. **Listen und List Kompression:** Erstellen von Listen über Ausdruckslisten: [ord(n) for n in string]
3. **Grundlegende mathematische Operationen:** Addition von Werten, Bildung von zusammengesetzten Payloads, Aggregieren von Werten (sum())
4. **String-Formatierung:** f-Strings zur dynamischen Erstellung von Strings, Zusammensetzen von Daten für Hashing
5. **Kryptographie-Grundlagen (praktisch):** SHA-256 Hash berechnen mit hashlib, Nutzung des Hashwerts für Authentifizierung, Slicing von Strings, z. B. auth_hash[:12]

**Aufgabe:**  
"Manipuliere deine Strings so das du alle gefundene ASCII-Werte (z. B. '67 111 107' und '45 54') summierst.",
"Verbinde beide Summen durch einen Doppelpunkt (sum_cookie:sum_secret) und berechne daraus den SHA-256-Hash.",
"Die ersten 12 Zeichen dieses Hash-Werts bilden deinen Authentifizierungscode."

**Solution:**
<pre> ```python def run(eingabe):
    flask_secret_ascii = [ord(
        n) for n in "adminpasssowrd"]
 ``` </pre>

---

## Level 2 – Textdatei mit Nebenwirkungen

**Geschichte**

Endlich, du hast dein Admin-Konto zurückerobert.
Doch kaum ist der Triumph da, fällt dein Blick auf eine seltsame Textdatei auf dem Desktop.
Sie scheint dich direkt anzusprechen.
Wirst du sie öffnen?
Vielleicht ist dort gar nichts Bösartiges … doch offenbar hast du keine andere Wahl.


**Lernziele:**
1. **Arbeiten mit Dateien:** Öffnen von Dateien mit open(), Lesen des gesamten Inhalts (read()), Umgang mit Encoding (UTF-8)
2. **String-Manipulation:** Platzhalter werden durch zufällig generierte Zeitstempel ersetzt. Entfernen unerwünschter Teile (replace()). Sauberes Aufbereiten der gefundenen Werte. Umwandeln von Zahlen in . Zusammenfügen mit join(). Erzeugen eines Dateinamens wie z.B. "566.jpg".
1. **Reguläre Ausdrücke (Regex):** Zeitstempel im Skript gezielt finden und verarbeiten. Muster definieren, z. B. "-\d+ UTC" oder "-\d+ UTC."
2. **Listenoperation:** Entfernen von Duplikaten unter Beibehaltung der Reihenfolge (dict.fromkeys()). Indexierung und Slicing beispielsweise [:3]
3. **Datenanalyse & Zähloperationen:** Vorkommen der Zeitstempel zählen, um eine neue Dateiname als Hinweis zu erzeugen. Zugriff auf Dictionary-Werte und Standardwerte (dict.get).

**Aufgabe:**  
"In dieser Nachricht versteckt sich der Schlüssel zu deinem Bild:",
Browser Fenster mit dem Geheimtextnachricht wird gezeigt,
"Berücksichtige jede Zahl (z. B. -1338780358 UTC). Zähle sorgfältig, wie oft jede UTC-Zahl vorkommt, und kombiniere sie zu einer Dateiendung. Verwende den Wert des frühesten Datums zuerst, den des spätesten Datums zuletzt, und kombiniere die Zählungen zu einem Dateinamen (z. B. 443.jpg)."


**Solution:**
<pre> ```python def run(path): return Dateinamen print(run("static/ausgabe.txt")) ``` </pre>

## Level 3 – Strings in Bildern finden (Einfache Steganographie)

**Geschichte**

Die gefundene Bild-Datei zeigt ein Schlüsselsymbol, was könnte daß für eine Bedeutung haben.


**Lernziele:**
1. **Dateien lesen & schreiben** einlesen einer Bild-Datei und schreiben einer Text-Datei als zwischenspeicher für einen Endschlüsselungs-Schlüssel
2. **durchsuchen von Dateien** Vorgegebenen Suchstring in der Bild-Datei ausfindig machen.
3. **Sting nach Muster aufteilen** gefundenen String in separate Teilstrings aufteilen und den relevanten in einer Text-Datei zwischenspeichern.

**Aufgabe:**  
Finden und zwischenspeichern (wird in Level4 benötigt) eines in der Bild-Datei versteckten ver./enschlüsselungsschlüssel.

## Level 4 – Bitweise Symetrische Verschlüsselung

**Geschichte**

Der Inhalt dieser Datei sieht komisch aus! 
Könnte Verschlüsselt worden sein? 
Was hat daß jetzt mit dem gefundenen Schlüssel zu tun?


**Lernziele:**
1. **Verketten von Strings** der gefundene Verschlüsselungskey muß für eine Erfolgreiche Entschlüsselung mehrfach hintereinander gesetzt werden, da die Nachricht meist länger als der Schlüssel ist.
2. **wandlung in Binär-Format** Damit ein String auf Bit-Ebene Entschlüsselt werden kann, müßen die Strings ins Binärformat und wieder zurück gewandelt werden.
3. **Bitweise XOR verknüpfung** Verknüpfen der Binären ketten mittels einer "Exklusiv oder" verknüpfung, zur Symetrischen ver./entschlüsselung mittels eines Schlüssel/Password/Zeichenketten.
4. **Arbeiten mit Funktionen** Aufteilen des Codes in einzelne Funktionen, damit Code nicht Kopiert werden muß, wenn dieser mehrfach verwendet wird. Bsp. bei der Umwandlung von Strings in Binärfolgen für die Nachricht und den ver./entschlüsselungsschlüssel.

**Aufgabe:**  
Entschlüsseln (Einfache Symetrische Verschlüsselung) des Datei-Inhaltes mit dem in Level3 gefundenen Schlüssel. Die Verschlüsselung ist mittels XOR Verknüpfung auf Bit-Ebene realisiert.

## Level 5 – Erweiterte Logfile-Analyse

**Geschichte**

Ein umfangreiches Logfile wurde dir zugespielt – es enthält Hinweise auf verdächtige Aktivitäten im
Netzwerk. Du vermutest, dass jemand versucht hat, sich Zugang zu einem Admin-Account zu verschaffen
und möglicherweise Firewall-Regeln manipuliert hat. Deine Aufgabe ist es, die Spuren zu analysieren.


**Lernziele:**
1. **Arbeiten mit regulären Ausdrücken**  Extrahieren von Portnummern aus Logzeilen.
2. **Bedingte Logik anwenden**  Erkennen von sicherem oder unsicherem Port-Zugriff anhand von Schlüsselwörtern.
3. **Fehleranalyse**  Zählen von fehlgeschlagenen Admin-Logins.
4. **Listen und Dictionaries verwenden**  Strukturierte Rückgabe der Analyseergebnisse für weitere Verarbeitung.

**Aufgaben**  
1. Alle Portnummern mit Status und Grund.
2. Die Anzahl der fehlgeschlagenen Admin-Logins.
3. Alle Zeilen, die eine Änderung an Firewall-Regeln enthalten.


## Level 6 - Port-Säuberung & Firewall-Wiederherstellung

**Geschichte**

Nach der Analyse im vorherigen Level ist klar: Einige Ports sind offen und stellen ein Sicherheitsrisiko dar. Du
musst nun eingreifen und die gefährlichen Ports schließen, um das System zu sichern. Außerdem sollen
manipulierte Firewall-Regeln wiederhergestellt und der Admin-Account entsperrt werden – aber nur, wenn zu
viele Fehlversuche erkannt wurden.


**Lernziele:**
1. **Listenmanipulation**  Ändern von Einträgen in einer Liste basierend auf Bedingungen.
2. **Bedingte Logik**  Entscheidung, ob ein Port geschlossen werden muss oder ob eine Warnung ausgegeben wird.
3. **String-Manipulation**  Wiederherstellung von Firewall-Regeln durch Ersetzen von Textteilen.
4. **Strukturierte Rückgabe**  Zusammenführen aller Ergebnisse in einem Dictionary zur weiteren Verwendung.

**Aufgaben**  
1. Schließe alle Ports, die als „open“ markiert sind und deren Grund nicht „secure/accepted“ ist.
2. Stelle manipulierte Firewall-Regeln wieder her.
3. Entsperre den Admin-Account, wenn mehr als zwei Fehlversuche erkannt wurden.

