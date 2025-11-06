import json

def check_level6_solution(data):
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

    # 3. Admin-Account entsperren + Warnung
    alert = None
    admin_account = None
    print("DEBUG: Admin-Failures =", admin_failures)  # NEU
    if admin_failures >=3:
        alert = "ALERT: Too many admin login failures"
        admin_account = "unlocked"
    if admin_failures >5:
        alert = "CRITICAL ALERT: Admin account compromised!"


    print("DEBUG: alert =", alert)  # NEU
    print("DEBUG: admin_account =", admin_account)  # NEU


    # Statistik
    stats = {
        "closed_ports_count": closed_count,
        "restored_rules_count": len(restored_firewall_rules)
    }

    # Debug-Ausgaben
    print("DEBUG: Level 6 Lösung gestartet")
    print(json.dumps({
        "ports": ports,
        "firewall_rules_restored": restored_firewall_rules,
        "alert": alert,
        "admin_account": admin_account,
        "stats": stats
    }, indent=2))

    # Rückgabe als JSON-String
    result_dict = {
        "ports": ports,
        "firewall_rules_restored": restored_firewall_rules,
        "alert": alert,
        "admin_account": admin_account,
        "stats": stats
    }

    return json.dumps(result_dict, indent=2)




