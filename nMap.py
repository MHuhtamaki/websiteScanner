from nmap import *


def run_nmap(ip, ports):

    scan_results = "\n"
    string_list = []
    print("Running nmap...")
    nm = nmap.PortScanner()
    nm.scan(ip, ports)
    nm.command_line()

    for host in nm.all_hosts():
        string_list.append('----------------------------------------------------')
        string_list.append('Host : %s (%s)' % (host, nm[host].hostname()))
        string_list.append('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            string_list.append('----------')
            string_list.append('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            for port in lport:
                string_list.append('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    return scan_results.join([string for string in string_list])

