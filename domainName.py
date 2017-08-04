from tld import get_tld


def get_domain(url):

    domain = get_tld(url)
    return domain
