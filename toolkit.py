import argparse
from modules import port_scanner, brute_force, subdomain_enum, web_scanner

def main():
    parser = argparse.ArgumentParser(description="Pentest Toolkit")
    parser.add_argument("-m", "--module", required=True, help="port_scan, brute_force, subdomain_enum, web_scan")
    parser.add_argument("-t", "--target", required=True, help="Target URL/IP")
    args = parser.parse_args()

    modules = {
        "port_scan": port_scanner.scan_ports,
        "brute_force": brute_force.attack,
        "subdomain_enum": subdomain_enum.find_subdomains,
        "web_scan": web_scanner.scan_vulnerabilities
    }
    
    modules.get(args.module, lambda x: print("Invalid module"))(args.target)

if __name__ == "__main__":
    main()
