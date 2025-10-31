# Beispielloesung Level 6

<<<<<<< HEAD
def run(data):
        ports = data["ports"]
        firewall_rules = data["firewall_rules"]
        admin_failures = data["admin_login_failures"]

    # Ports schließen
        for entry in ports:
            if entry["status"] == "open" and entry["reason"] != "secure/accepted":
                entry["status"] = "closed"
                entry["reason"] = "manually closed"

    # Firewall-Regeln wiederherstellen
        restored_firewall_rules = []
        for rule in firewall_rules:
            restored_rule = rule.replace("updated: allow", "restored:")
            restored_firewall_rules.append(restored_rule)

    # Admin entsperren
        alert = None
        admin_account = None
        if admin_failures > 2:
            alert = "ALERT: Too many admin login failures"
            admin_account = "unlocked"

        return {
            "ports": ports,
            "firewall_rules_restored": restored_firewall_rules,
            "alert": alert,
            "admin_account": admin_account
        }
=======
def run(port_list):
    cleaned = []
    for entry in port_list:
        if entry["status"] == "open" and entry["reason"] != "secure/accepted":
            entry["status"] = "closed"
            entry["reason"] = "manually closed"
        cleaned.append(entry)
    return cleaned
>>>>>>> 79700d30aebc1b2b6354c3cd4d0664734979dcfa
