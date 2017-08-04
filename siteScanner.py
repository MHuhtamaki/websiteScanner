import general
import domainName
import ipAddress
import nMap
import robots_txt
import whois
import sys

ROOT_DIR = 'Websites'
general.create_directory(ROOT_DIR)
args = sys.argv


def run_site_scan(url, port_range):

    # Get an ip-address of a given domain.
    ip = ipAddress.get_ip_address(url)

    nmap_scan_results = nMap.run_nmap(ip, port_range)
    robots_txt_file = robots_txt.get_robots_txt(url)
    whois_info = whois.get_whois(url)

    save_results(nmap_scan_results, robots_txt_file, whois_info, url)


def save_results(nmap_scan_results, robots_txt_file, whois_info, url):

    website_dir = ROOT_DIR + '/' + domainName.get_domain(url) + '/'

    # Directory for the website info
    general.create_directory(website_dir)

    # Generate files from the website data.
    general.write_file(website_dir + "nMap_scan.txt", nmap_scan_results)
    general.write_file(website_dir + "robots_txt_file.txt", robots_txt_file)
    general.write_file(website_dir + "whois_info.txt", whois_info)

    print("\n"+"Scan complete!!")
    print("\n"+"Results in: " + ROOT_DIR + "/" + domainName.get_domain(url))

run_site_scan(args[1], args[2])
