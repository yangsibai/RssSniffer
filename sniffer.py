# -*- encofing: utf-8 -*-

import sys
import urlparse
import urllib2
import xml.etree.ElementTree as ET

def sniff(url):
    suffixes = ['', 'rss', 'rss.xml', 'feed.xml', 'atom.xml', 'atom2.xml']
    results = []
    for s in suffixes:
        u = urlparse.urljoin(url, s)
        if is_rss(u):
            print u
            results.append(u)
    if len(results) == 0:
        print 'Cannot find a rss feed at %s' % url


def is_rss(url):
    o = urlparse.urlparse(url)
    hdr = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': o.netloc,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36'
    }
    req = urllib2.Request(url, headers=hdr)
    try:
        res = urllib2.urlopen(req)
        if res.getcode() == 200:
            return is_valid_feed(res.read())
    except:
        pass
    return False

def is_valid_feed(content):
    try:
        root = ET.fromstring(content)
        return root.tag == 'rss'
    except:
        pass
    return False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        u = sys.argv[1]
        sniff(u)
    else:
        print 'invalid url, e.g. python sniffer.py http://www.example.com'
