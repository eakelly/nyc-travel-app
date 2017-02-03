#!/bin/bash

curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
echo "pip finished downloading!"
python get-pip.py
echo "pip finished installing!"
pip install requests
echo "requests finished installing!"
pip install beautifulsoup4
echo "beautifulsoup4 finished installing!"
if [[ "$OSTYPE" == "msys" ]]; then
	pip install Twisted[windows_platform]
	echo "Twisted (for Windows) finished installing!"
else 
	pip install Twisted
	echo "Twisted finished installing!"
fi
pip install scrapy
echo "scrapy finished installing!"
pip install django
echo "django finished installing!"
