import json

def run(data):  # Musterlösung
    ports = data["ports"]
    firewall_rules = data["firewall_rules"]
    admin_failures = data["admin_login_failures"]

    # 1. Ports schließen
    closed_count = 0
    for entry in ports:
        if entry["status"] == "open" and entry["reason"] != "secure/accepted":
            entry["status"] = "closed"
            entry["reason"] = "manually closed"
            closed_count += 1

    # 2. Firewall-Regeln wiederherstellen (Duplikate entfernen)
    restored_firewall_rules = []
    for rule in firewall_rules:
        restored_rule = rule.replace("updated: allow", "restored:")
        if restored_rule not in restored_firewall_rules:
            restored_firewall_rules.append(restored_rule)

    # 3. Alerts für Admin-Account
    alert = None
    admin_account = None
    if admin_failures >= 3:
        alert = "ALERT: Too many admin login failures"
        admin_account = "unlocked"
    if admin_failures > 5:
        alert = "CRITICAL ALERT: Admin account compromised!"

    # 4. Statistik
    stats = {
        "closed_ports_count": closed_count,
        "restored_rules_count": len(restored_firewall_rules)
    }

    # 5. Sortierung für deterministische Ausgabe
    ports.sort(key=lambda x: (x["port"], x["status"], x["reason"]))
    restored_firewall_rules.sort()

    # 6. Ergebnis-Dict
    result_dict = {
        "ports": ports,
        "firewall_rules_restored": restored_firewall_rules,
        "alert": alert,
        "admin_account": admin_account,
        "stats": stats
    }

    # Rückgabe als kompakter JSON-String mit stabiler Sortierung
    return json.dumps(result_dict, separators=(',', ':'), sort_keys=True)
