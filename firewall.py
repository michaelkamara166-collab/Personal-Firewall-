import ipaddress
from rules import load_rules, add_ip, remove_ip, add_port, remove_port
from logger import log_event

rules = load_rules()

blocked_ips = rules["blocked_ips"]
blocked_ports = rules["blocked_ports"]


def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def check_connection(ip, port):

    if ip in blocked_ips:
        print("\n❌ Connection Blocked!")
        print(f"Reason: IP Address {ip} is blocked.")
        log_event(f"Blocked IP: {ip} Port: {port}")
        return

    if port in blocked_ports:
        print("\n❌ Connection Blocked!")
        print(f"Reason: Port {port} is blocked.")
        log_event(f"Blocked Port: {port} from IP {ip}")
        return

    print("\n✅ Connection Allowed.")
    log_event(f"Allowed Connection: {ip}:{port}")


def view_rules():
    rules = load_rules()

    print("\nBlocked IP Addresses")
    for ip in rules["blocked_ips"]:
        print(ip)

    print("\nBlocked Ports")
    for port in rules["blocked_ports"]:
        print(port)


while True:

    print("\n========== PERSONAL FIREWALL ==========")
    print("1. Test Connection")
    print("2. View Rules")
    print("3. Add Blocked IP")
    print("4. Remove Blocked IP")
    print("5. Add Blocked Port")
    print("6. Remove Blocked Port")
    print("7. Exit")

    choice = input("\nSelect option: ")

    if choice == "1":

        ip = input("Enter IP Address: ")

        if not validate_ip(ip):
            print("Invalid IP Address.")
            continue

        try:
            port = int(input("Enter Port Number: "))
        except ValueError:
            print("Invalid Port.")
            continue

        check_connection(ip, port)


    elif choice == "2":
        view_rules()


    elif choice == "3":
        ip = input("Enter IP to block: ")

        if validate_ip(ip):
            add_ip(ip)
            print("IP added successfully.")
        else:
            print("Invalid IP.")


    elif choice == "4":
        ip = input("Enter IP to remove: ")
        remove_ip(ip)
        print("IP removed successfully.")


    elif choice == "5":
        try:
            port = int(input("Enter Port: "))
            add_port(port)
            print("Port blocked.")
        except ValueError:
            print("Invalid Port.")


    elif choice == "6":
        try:
            port = int(input("Enter Port: "))
            remove_port(port)
            print("Port removed.")
        except ValueError:
            print("Invalid Port.")


    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid Option.")
