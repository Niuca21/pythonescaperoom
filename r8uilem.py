
import re

def solve(log_text):
    results = []
    lines = log_text.strip().split("
")

    for line in lines:
        line = line.lower().strip()
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

    return results
