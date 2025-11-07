import re
import os
import json

def parse_logfile_extended(log_text):
    if os.path.isfile(log_text):
        with open(log_text, "r", encoding="utf-8") as f:
            log_text = f.read()

    results = []
    admin_fail_count = 0
    firewall_rules = []
    ip_addresses = set()
    open_ports_count = 0
    closed_ports_count = 0

    lines = log_text.strip().split("\n")

    for line in lines:
        line_lower = line.lower().strip()

        # Admin-Login-Fehler zählen
        if "user login failed for user admin" in line_lower:
            admin_fail_count += 1

        # Firewall-Regeln sammeln
        if "firewall rule updated" in line_lower:
            firewall_rules.append(line_lower)

        # IP-Adressen extrahieren
        ips = re.findall(r"\d{1,3}(?:\.\d{1,3}){3}", line)
        ip_addresses.update(ips)

        # Ports analysieren
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

    # Firewall-Ports sortieren

    firewall_ports_sorted = []

    for rule in firewall_rules:
        match = re.search(r"port (\d+)", rule)
        if match:
            firewall_ports_sorted.append(int(match.group(1)))

    firewall_ports_sorted.sort()

    # Rückgabe als JSON-String
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
    }, separators=(',', ':'), sort_keys=True)
#    }, indent=2)

def check_ports_level5(log_data):
    return parse_logfile_extended(log_data)

