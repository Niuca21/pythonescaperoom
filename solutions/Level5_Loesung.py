# Beispiellösung Level 5: Lucasz

import re

def run(log_text):
    results = []
    admin_fail_count = 0
    firewall_rules = []
    lines = log_text.strip().split("\n")

    for line in lines:
        line = line.lower().strip()

        if "user login failed for user admin" in line:
            admin_fail_count += 1

        if "firewall rule updated" in line:
            firewall_rules.append(line)

        matches = re.findall(r"port (\d+)", line)
        for match in matches:
            port = int(match)
            if "secure" in line or "accepted" in line:
                status = "open"
                reason = "secure/accepted"
            elif "attempt" in line or "exposed" in line or "unauthorized" in line:
                status = "open"
                reason = "attempt/exposed/unauthorized"
            elif "filtered" in line:
                status = "closed"
                reason = "filtered"
            else:
                status = "closed"
                reason = "default"

            results.append({
                "port": port,
                "status": status,
                "reason": reason,
                "raw_line": line
            })

    return {
        "ports": results,
        "admin_login_failures": admin_fail_count,
        "firewall_rules": firewall_rules
    }
