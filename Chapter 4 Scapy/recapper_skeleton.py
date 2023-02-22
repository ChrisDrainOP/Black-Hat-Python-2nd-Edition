from scapy.all import TCP, rdpcap
import collections
import os
import re
import sys
import zlib

OUTDIR='~/Pictures'
PCAPS='~/Pictures/PCAP Downloads'

Response = collections.namedtuple('Response', ['header','payload'])

def get_header(payload):
    pass

def extract_content(Response, content_name='image'):
    pass

class Recapper:
    def __init__(self, fname):
        pass

    def get_responses(self):
        pass
    
    def write(self, content_name):
        pass

if __name__ == 'main':
    pfile = os.path.join(PCAPS, 'pcap.pcap')
    recapper = Recapper(pfile)
    recapper.get_responses()
    recapper.write('image')