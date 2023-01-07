#!/usr/bin/python3
# -*- coding: utf-8 -*-

# MSManager installation & setup assistant
# You can launch this installer with the command: msmanager autosetup.
# The program will launch automatically when the application is started for the first time.
# WARNING! The configuration will be overwritten if you run the installer again when the program is installed.

# MSManager is under GPLv3 license, if you use the program or part of the program in one of your projects via a "fork" of GitHub, you must keep this license on your project.

# Imports
import requests
import displays as displays
import json
import os
from os.path import expanduser
home = expanduser("~")

# Fonctions
def download_distribution(distribution):
    if distribution == 'paper':
        download_versions = json.loads(requests.get('https://gist.githubusercontent.com/osipxd/6119732e30059241c2192c4a8d2218d9/raw/ce7efbdaded56779ecc7ce6e5b484d8ee0e55429/paper-versions.json').text)['versions']
        for version in download_versions:
            displays.info('Downloading paper '+version+'...')
            try:
                r = requests.get(download_versions[version], allow_redirects=True)
                open(home+"/.msmanager/predownload/paper/%s.jar"% version, 'wb').write(r.content)
            except:
                displays.fail('Failed to download paper '+version)

# Welcome message
print('Welcome to MSManager installation assistant')
print('You are starting MSManager for the first time on this session or system.')
print('Thank you for using our application, we will take care of installing everything automatically but you may need to answer the following questions.')

# Directory config
displays.info('Configuring directorys... ')
try:
    os.mkdir(home+"/.msmanager")
    os.mkdir(home+"/.msmanager/predownload")
    os.mkdir(home+"/.msmanager/predownload/paper")
    os.mkdir(home+"/.msmanager/predownload/spigot")
    os.mkdir(home+"/.msmanager/predownload/vanilla")
except:
    pass
displays.info('done')

# Formulary
displays.info('Pre-downloading servers will make it easier for you to configure servers in the future. If you want to create a single server, we advise you to answer no.')
displays.warning('Disk space will be required.')
server_download = displays.prompt_auto('Do you want to predownload servers? ', ['yes', 'no'])
if server_download == "yes":
    distribution = displays.prompt_auto('The servers will be installed but please indicate a "distribution" of minecraft servers: ', ['paper', 'spigot', 'vanilla'])
    download_distribution(distribution)