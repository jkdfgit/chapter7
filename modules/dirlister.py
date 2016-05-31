# dirlister.py
# Lists all the files in the current directory and returns the list to a string

import os

def run(**args):
    
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return str(files)