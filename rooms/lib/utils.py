# lib/utils.py
def pretty_print(result):
    print("🔐 Admin Login Failures:", result["admin_login_failures"])
    
    print("\n🧱 Firewall Rules:")
    if result["firewall_rules"]:
        for rule in result["firewall_rules"]:
            print(" -", rule)
    else:
        print(" - Keine gefunden")

    print("\n🔌 Port Status:")
    if result["ports"]:
        for port_info in result["ports"]:
            print(f" - Port {port_info['port']}: {port_info['status']} ({port_info['reason']})")
    else:
        print(" - Keine Ports gefunden")
