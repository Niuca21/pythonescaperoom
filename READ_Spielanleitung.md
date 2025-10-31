# Spielübersicht

## Anfang
Du schaltest deinen Computer ein und siehst nur ein seltsames Anmeldefenster als Gast.  
Plötzlich startet ein merkwürdiges Spiel, das dir Hinweise gibt, wie du dein Admin-Konto zurückbekommst.

---

## Level 1 – Diese Cookies sind nicht lecker :)

**Geschichte**

Du schaltest deinen Computer ein doch etwas stimmt nicht.
Anstatt des gewohnten Desktops erscheint nur ein fremdes Anmeldefenster: „Gastkonto aktiv.“
Jemand muss dein System verändert haben.
Noch bevor du reagieren kannst, öffnet sich automatisch dein Browser.
Ein merkwürdiges Spiel startet — und mitten auf dem Bildschirm erscheint eine Nachricht:
„Willst du dein Admin-Konto zurück? Dann folge den Hinweisen…“


**Lernziele:**
1. **Session Kontext:** Für die Aufgabenerstellung wurde mithilfe von Python der Session-Kontext im Browser manipuliert, um einen versteckten Hinweis (Hint) zu platzieren.2)
2. **Kodierung und generierte Zeichenketten:** Die Zeichenketen werden dabei im Browser verborgen.
3. **Dekodierung:** Die Aufgabe des Spielers besteht darin, diese Zeichenkette zu finden und zu dekodieren.

**Aufgabe:**  
Finde die versteckte Nachricht(Admin Password) in der ASCII-Zeichenkette.

---

## Level 2 – Textdatei mit Nebenwirkungen

**Geschichte**

Endlich, du hast dein Admin-Konto zurückerobert.
Doch kaum ist der Triumph da, fällt dein Blick auf eine seltsame Textdatei auf dem Desktop.
Sie scheint dich direkt anzusprechen.
Wirst du sie öffnen?
Vielleicht ist dort gar nichts Bösartiges … doch offenbar hast du keine andere Wahl.


**Lernziele:**
1. **Arbeiten mit Dateien:** Eine Textdatei wird erstellt, die Hinweise für den nächsten Level enthält.  
2. **String-Manipulation:** Platzhalter werden durch zufällig generierte Zeitstempel ersetzt.  
3. **Arbeiten mit Zeitstempeln:** Spieler muss die Zeitstempel in normale UTC-Werte übersetzen.  
4. **Reguläre Ausdrücke (Regex):** Zeitstempel im Skript gezielt finden und verarbeiten.  
5. **Datenanalyse & Zähloperationen:** Vorkommen der Zeitstempel zählen, um eine neue Dateiname als Hinweis zu erzeugen.

**Aufgabe:**  
Dekodiere die Zeitstempel, zähle die Werte und finde die neue Datei, die den nächsten Hinweis enthält.

## Level 3 – Strings in Bildern finden

**Geschichte**

Die gefundene Bild-Datei zeigt einen Schlüssel, das könnte eine Bedeutung haben.

**Lernziele:**

1. **Bild-Datei öffenen** gefundenes Bild öffen
2. **suchen von Strings in Bildern** Vorgegebenen String suchen 
3. **Stings nach Muster aufteilen** String in Teilstrings aufteilen
4. **Teilstring in Datei speichern** Teilstring in separater Datei, zur späteren verwendung, speichern.
5. **Name**
6. **Name**

## Level 4 – Bitweise Symetrische Verschlüsselung

**Geschichte**

Was ist jetz mit dem gefundenen Schlüssel zu tun? Warum kann ich den Inhalt dies komische Datei nicht lesen? Könnte sie Verschlüsselt worden sein.

**Lernziele:**

1. **Verketten von Strings** der gefundene Verschlüsselungskey muß für eine Erfolgreiche Entschlüsselung mehrfach hintereinander gesetzt werden, da die Nachricht meist länger als der Schlüssel ist.
2. **Strings umwandeln in Binär und zurück** Damit auf Bit-Ebene Verschlüsselt werden kann müßen die Strings imd Binärfolgen und wieder zurück gewandelt werden
3. **XOR verknüpfung von Binär kodierten Zeichenketten** Verknüpfen der Binären ketten mittels einer "Exklusiv oder" verknüpfung.
4. **Arbeiten mit Funktionen** Aufteilen des Codes in einzelne Funktionen, damit Code nicht Copiert werden muß
5. **Name**
6. **Name**

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


1. **Name**
2. **Name**
3. **Name**
4. **Name**
5. **Name** Lukasz
6. **Name** Lukasz

## Level 6 – Name the game

**Geschichte**

**Lernziele:**

1. **Name**
2. **Name**
3. **Name**
4. **Name**
5. **Name**
6. **Name**
