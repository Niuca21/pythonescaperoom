
# lib/log_generator.py   ( Lukasz Kotula )

import random

def generate_logfile(num_lines=100):
    port_events = [

        "Secure connection established on port {} at {} from {}",
        "Unauthorized access attempt on port {} from {}",
        "Port {} is filtered",
        "Connection accepted on port {} at {}",
        "Unknown activity on port {} from {}",
        "Firewall rule updated: allow port {} from {}",
        "Exposed service detected on port {} from {}"
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
    # 1. Mindestens 2 
    for _ in range(2):
        port = random.choice(ports)
        ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        log_lines.append(f"Firewall rule updated: allow port {port} from {ip}")

    # 2. Zufällig 2 oder 3 Admin-Login-Fehler
    for _ in range(random.randint(2, 3)):
        log_lines.append("User login failed for user admin")

    # 3. Restliche Zeilen auffüllen
    while len(log_lines) < num_lines:
        if random.random() < 0.6:
            template = random.choice(port_events)
            port = random.choice(ports)
            timestamp = random.choice(times)
            ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
            log_lines.append(template.format(port, timestamp, ip))
        else:
            template = random.choice(system_events)
            if "{}" in template:
                value = random.choice(times if "at" in template else users)
                log_lines.append(template.format(value))
            else:
                log_lines.append(template)

    # Fehlerhafte Einträge für Challenge
        if random.random() < 0.05:
            log_lines.append("ERROR: malformed log entry without port")

    print(f"DEBUG: Logfile generiert mit {num_lines} Zeilen")
    print("DEBUG: Beispiel-Logzeilen:\n", "\n".join(log_lines[:5]))
    return "\n".join(log_lines)
