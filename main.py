from bs4 import BeautifulSoup

import requests
import locale

def main():
	r = requests.get("https://www.southwest.com")
	with open("southwestindex.html", "w+") as writefile:
		writefile.write(r.text)
	soup = BeautifulSoup(r.text, 'html.parser')
	#print(soup.prettify())
	with open("southwest_routes.html", "w+") as writefile:
		for x in soup.findAll('script'):
				if 'var routes' in str(x):
					writefile.write(str(x))
					writefile.write("\n")

main()
