import re
import os
import json

def run(log_text):
    print("DEBUG: run() gestartet mit log_text =", log_text)
    if os.path.isfile(log_text):
        with open(log_text, "r", encoding="utf-8") as f:
            log_text = f.read()
    print("DEBUG: Dateiinhalt (erste 200 Zeichen):")
    print(log_text[:200])
    results = []
    admin_fail_count = 0
    firewall_rules = []
    ip_addresses = set()
    open_ports_count = 0
    closed_ports_count = 0

    lines = log_text.strip().split("\n")

    # Debug-Ausgabe zur Prüfung des Logfile-Inhalts
    print("DEBUG: Pfad oder Inhalt der Logdatei:")
    print(log_text[:200])

    print("DEBUG: Erste 5 Zeilen der Logdatei:")
    for i, line in enumerate(lines[:5]):
        print(f"Zeile {i+1}: {repr(line)}")

    for line in lines:
        line_lower = line.lower().strip()

        if "user login failed for user admin" in line_lower:
            admin_fail_count += 1

        if "firewall rule updated" in line_lower:
            firewall_rules.append(line_lower)

        ips = re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", line)
        ip_addresses.update(ips)

        matches = re.findall(r"port (\d+)", line_lower)
        for match in matches:
            port = int(match)
            if "secure" in line_lower or "accepted" in line_lower:
                status = "open"
                reason = "secure/accepted"
                open_ports_count += 1
            elif "attempt" in line_lower or "exposed" in line_lower or "unauthorized" in line_lower:
                status = "open"
                reason = "attempt/exposed/unauthorized"
                open_ports_count += 1
            elif "filtered" in line_lower:
                status = "closed"
                reason = "filtered"
                closed_ports_count += 1
            else:
                status = "closed"
                reason = "default"
                closed_ports_count += 1

            results.append({
                "port": port,
                "status": status,
                "reason": reason,
                "raw_line": line
            })

    firewall_ports_sorted = sorted([int(re.search(r"port (\d+)", rule).group(1)) for rule in firewall_rules])

    # Debug-Ausgaben hier:
    print("DEBUG: Datei analysiert =", log_text[:50], "...")
    print(f"DEBUG: Anzahl Zeilen = {len(lines)}")
    print(f"DEBUG: Admin-Fehler = {admin_fail_count}")
    print(f"DEBUG: Firewall-Regeln = {firewall_rules}")
    print(f"DEBUG: IP-Adressen = {list(ip_addresses)}")
    print(f"DEBUG: Ports gefunden = {len(results)}")
    print("DEBUG: Vollständiges Ergebnis:\n", json.dumps({
        "ports": results,
        "admin_login_failures": admin_fail_count,
        "firewall_rules": firewall_rules,
        "ip_addresses": list(ip_addresses),
        "stats": {
            "open_ports_count": open_ports_count,
            "closed_ports_count": closed_ports_count
        }
    }, indent=2))


    return json.dumps({
        "ports": results,
        "admin_login_failures": admin_fail_count,
        "firewall_rules": firewall_rules,
        "firewall_ports_sorted": firewall_ports_sorted,
        "ip_addresses": list(ip_addresses),
        "stats": {
            "open_ports_count": open_ports_count,
            "closed_ports_count": closed_ports_count
        }
    }, indent=2, sort_keys=True)


#    return {
#        "ports": results,
#        "admin_login_failures": admin_fail_count,
#        "firewall_rules": firewall_rules,
#        "firewall_ports_sorted": firewall_ports_sorted,
#        "ip_addresses": list(ip_addresses),
#        "stats": {
#            "open_ports_count": open_ports_count,
#            "closed_ports_count": closed_ports_count
#        }
#    }

