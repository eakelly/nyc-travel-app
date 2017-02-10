#!/bin/bash
printf "Downloading pip source code..\n"
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py

printf "Installing pip..\n"
python get-pip.py

printf "Deleting pip source code..\n"
rm get-pip.py
clear

printf "Installing requests...\n"
pip install requests

printf "Installing beautifulsoup4...\n"
pip install beautifulsoup4

printf "Installing twisted... (necessary dependency for scrapy)."
printf "If any errors occur, Visual Studio has not been installed or configured correctly to build wheel source."
if [[ "$OSTYPE" == "msys" ]]; then
	pip install Twisted[windows_platform]
else 
	pip install Twisted
fi

printf "Installing scrapy...\n"
pip install scrapy

printf "Installing django...\n"
pip install django

printf "Installing rauth...\n"
pip install rauth

printf "Installing tabualte..\n"
pip install tabulate
