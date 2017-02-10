#!/bin/bash
echo "Downloading pip source code..\n"
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py

echo "Installing pip..\n"
python get-pip.py

echo "Deleting pip source code..\n"
rm get-pip.py
clear

echo "Installing requests...\n"
pip install requests

echo "Installing beautifulsoup4...\n"
pip install beautifulsoup4

echo "Installing twisted... (necessary dependency for scrapy)."
echo "If any errors occur, Visual Studio has not been installed or configured correctly to build wheel source."
if [[ "$OSTYPE" == "msys" ]]; then
	pip install Twisted[windows_platform]
else 
	pip install Twisted
fi

echo "Installing scrapy...\n"
pip install scrapy

echo "Installing django...\n"
pip install django

echo "Installing rauth...\n"
pip install rauth