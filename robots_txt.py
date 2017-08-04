import urllib.request
import io


def get_robots_txt(url):

    print("Requesting the robots.txt -file...")
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    try:
        request = urllib.request.urlopen(path + "robots.txt", data=None)
        data = io.TextIOWrapper(request, encoding='utf-8')
        return data.read()
    except urllib.error.HTTPError as e:
        return repr(e)

