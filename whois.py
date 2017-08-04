import os
import domainName


def get_whois(url):

    print("Getting the whois info...")
    command = "whois " + domainName.get_tld(url)
    process = os.popen(command)
    result = str(process.read())
    return result

