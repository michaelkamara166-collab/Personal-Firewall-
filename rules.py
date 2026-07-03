import json

CONFIG_FILE = "config.json"

def load_rules():
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)

def save_rules(rules):
    with open(CONFIG_FILE, "w") as file:
        json.dump(rules, file, indent=4)

def add_ip(ip):
    rules = load_rules()
    if ip not in rules["blocked_ips"]:
        rules["blocked_ips"].append(ip)
        save_rules(rules)

def remove_ip(ip):
    rules = load_rules()
    if ip in rules["blocked_ips"]:
        rules["blocked_ips"].remove(ip)
        save_rules(rules)

def add_port(port):
    rules = load_rules()
    if port not in rules["blocked_ports"]:
        rules["blocked_ports"].append(port)
        save_rules(rules)

def remove_port(port):
    rules = load_rules()
    if port in rules["blocked_ports"]:
        rules["blocked_ports"].remove(port)
        save_rules(rules)
