
<h1 align='center'>Ransom0</h1>

<p align="center">
    This is a fork of
    <a href="https://github.com/HugoLB0/Ransom0">HugoLB0's Ransom0</a> working
    on terminal based machines. This was part of a university project.
</p>
 
<p align="center">
  Ransom0 is an open source ransomware made with Python, designed to find and encrypt user data. 
  <img src="https://hugolb0.000webhostapp.com/ransom0_main.png">
</p>





## Program Structure:
In order for the program to work from anywhere in the world, the server uses PyNgrok to tunnel it and make the server reacheable from evrywhere.

The project is composed of two main **parts/programs**: **the server and the ransomware**

the **server** is organised in **two parts**:
- **SQL database:** create a SQL database with a CLIENT table where user datas such as key, digits, time are stored in there
- **HTTP server:** basic http server to handle POST requests made from the ransomware.

the **ransomware** is organised  in **four parts**:
 - **Find Files:** find files by extensions and store the path into **path.txt**
 - **Encrypt Files:** encrypt files in **path.txt**, generate **digits id**, **send key and id**
 - **Decrypt:** ask for money, wait for the key, and decrypt file if key is correct
-  **Send data:** send data to our http server

## How to run
You need to have python3 installed and configured

 - Download the repository via git or zip
 - Install requirements: `pip install -r requirements.txt`

1.Run the server: `python3 server.py`
Before running the ransomware, you'll need to modify a few things in ransom.py:

 1. Put the url you've got when you started the server: ![enter image description here](https://hugolb0.000webhostapp.com/ransom0_url.png)

 

 2. I recommend running it in a testing directory, otherwise all of your files will be encrypted: ![enter image description here](https://hugolb0.000webhostapp.com/ransom0_directory.png)

2. Run it: `python3 ransom0.py`

## To do:
 - [x] Add logs
 - [x] Add filter to exclude system files
 - [x] Message in a GUI windows (Tkinter)
 - [x] !! Add a databases or server instead of mail (SQL) 
 - [ ] !! Add a Web Interface ( Frontend: VueJs ? Backend: Django?) 
 - [ ] !! Bypass permission / Privileges Escalation (WinPwnage)
 - [ ] Hide logs
 - [ ] Automatically  show the message on startup
 - [ ] Generate executable for all OS (pyinstaller)


## Testing
This Program have been test on:

 - **Windows 10**
 - **Mac OS Catalina 10.15.6 (19G73)**
 - **Mac OS Big Sur 11.2.1 (20D74)**

## Any donation are welcome
Donations are welcome, it'll really help me to continue to maintain this project :)
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/big/1Bw82zC5FnVtw93ZrcALQTeZBXgtVWH75n)](https://en.cryptobadges.io/badge/big/1Bw82zC5FnVtw93ZrcALQTeZBXgtVWH75n)

[![Donate with Ethereum](https://en.cryptobadges.io/badge/big/0x71b163e2fc5b2c10cd8cf0a2cc8917db6db57326)](https://en.cryptobadges.io/badge/big/0x71b163e2fc5b2c10cd8cf0a2cc8917db6db57326)


## DISCLAIMER 
**THIS PROJECT IS FOR EDUCATION PURPOSE ONLY, DO NOT RUN IT WITHOUT PERMISSION!**
**I AM NOT RESPONSIBLE FOR ANY DAMAGED CAUSED BY THE ILLEGAL USAGE OF THIS PROGRAM**

## Stargazers
 [![Stargazers repo roster for @USERNAME/REPO_NAME](https://reporoster.com/stars/HugoLB0/Ransom0)](https://github.com/HugoLB0/Ransom0/stargazers)
