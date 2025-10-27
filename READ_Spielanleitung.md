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

## Level 3 – Strings in Bildern finden (Einfache Steganographie)

**Geschichte**

Die gefundene Bild-Datei zeigt ein Schlüsselsymbol, was könnte daß für eine Bedeutung haben.

**Lernziele:**
1. **Dateien lesen & schreiben** einlesen einer Bild-Datei und schreiben einer Text-Datei als zwischenspeicher für einen Endschlüsselungs-Schlüssel
2. **durchsuchen von Dateiinhalten** Vorgegebenen Suchstring in der Bild-Datei ausfindig machen.
3. **Sting nach Muster aufteilen** gefundenen String in separate Teilstrings aufteilen und den relevanten in einer Text-Datei zwischenspeichern.

**Aufgabe:**

Finden und zwischenspeichern (wird in Level4 benötigt) eines in der Bild-Datei versteckten ver./enschlüsselungsschlüssel.

## Level 4 – Bitweise Symetrische Verschlüsselung

**Geschichte**
Warum kann ich den Inhalt dieser komische Datei nicht lesen? 
Könnte sie Verschlüsselt worden sein? 
Was hat daß jetzt mit dem gefundenen Schlüssel zu tun?

**Lernziele:**
1. **Verketten von Strings** der gefundene Verschlüsselungskey muß für eine Erfolgreiche Entschlüsselung mehrfach hintereinander gesetzt werden, da die Nachricht meist länger als der Schlüssel ist.
2. **wandlung in Binär-Format** Damit ein String auf Bit-Ebene Entschlüsselt werden kann, müßen die Strings ins Binärformat und wieder zurück gewandelt werden.
3. **Bitweise XOR verknüpfung** Verknüpfen der Binären ketten mittels einer "Exklusiv oder" verknüpfung, zur Symetrischen ver./entschlüsselung mittels eines Schlüssel/Password/Zeichenketten.
4. **Arbeiten mit Funktionen** Aufteilen des Codes in einzelne Funktionen, damit Code nicht Kopiert werden muß, wenn dieser mehrfach verwendet wird. Bsp. bei der Umwandlung von Strings in Binärfolgen für die Nachricht und den ver./entschlüsselungsschlüssel.

**Aufgabe:**
Entschlüsseln (Einfache Symetrische Verschlüsselung) des Datei-Inhaltes mit dem in Level3 gefundenen Schlüssel. Die Verschlüsselung ist mittels XOR Verknüpfung auf Bit-Ebene realisiert.

## Level 5 – Name the game

**Geschichte**

**Lernziele:**

1. **Name**
2. **Name**
3. **Name**
4. **Name**
5. **Name**
6. **Name**

**Aufgabe:**

## Level 6 – Name the game

**Geschichte**

**Lernziele:**

1. **Name**
2. **Name**
3. **Name**
4. **Name**
5. **Name**
6. **Name**

**Aufgabe:**
