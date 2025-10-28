
# lib/log_generator.py   ( Lukasz Kotula )

import random

def generate_logfile(num_lines=40):
    port_events = [
        "Secure connection established on port {}",
        "Unauthorized access attempt on port {}",
        "Port {} is filtered",
        "Connection accepted on port {}",
        "Unknown activity on port {}",
        "Firewall rule updated: allow port {}",
        "Exposed service detected on port {}"
    ]

    system_events = [
        "System rebooted at {}",
        "User login failed for user {}",
        "Configuration file changed",
        "Backup completed successfully",
        "Antivirus scan started",
        "User {} logged out",
        "Security policy updated"
    ]

    ports = [22, 80, 443, 8080, 8443, 9999, 3306, 21, 25, 110, 143, 995, 993]
    users = ["admin", "guest", "root", "user1", "service"]
    times = ["00:01", "12:45", "03:33", "18:22", "23:59"]

    log_lines = []

    # 1. Mindestens 2 Firewall-Regeln
    for _ in range(2):
        port = random.choice(ports)
        log_lines.append(f"Firewall rule updated: allow port {port}")

    # 2. Zufällig 2 oder 3 Admin-Login-Fehler
    for _ in range(random.randint(2, 3)):
        log_lines.append("User login failed for user admin")

    # 3. Restliche Zeilen auffüllen
    while len(log_lines) < num_lines:
        if random.random() < 0.6:
            template = random.choice(port_events)
            port = random.choice(ports)
            log_lines.append(template.format(port))
        else:
            template = random.choice(system_events)
            if "{}" in template:
                value = random.choice(times if "at" in template else users)
                log_lines.append(template.format(value))
            else:
                log_lines.append(template)

    return "\n".join(log_lines)
