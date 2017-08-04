import socket
import domainName


def get_ip_address(url):

    domain = domainName.get_domain(url)
    ip = socket.gethostbyname(domain)
    return ip

