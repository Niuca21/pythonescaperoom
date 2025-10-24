def run(port_list):
    cleaned = []
    for entry in port_list:
        if entry["status"] == "open" and entry["reason"] != "secure/accepted":
            entry["status"] = "closed"
            entry["reason"] = "manually closed"
        cleaned.append(entry)
    return cleaned
``