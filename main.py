from bs4 import BeautifulSoup

import requests
import locale

def main():
	r = requests.get("https://www.southwest.com")

	request_text = str(r.text.encode('utf-8'))
	with open("southwestindex.html", "w+") as writefile:
		writefile.write(request_text)
	soup = BeautifulSoup(request_text, 'html.parser')
	#print(soup.prettify())
	with open("southwest_routes.html", "w+") as writefile:
		for x in soup.findAll('script'):
				if 'var routes' in str(x):
					writefile.write(str(x))
					writefile.write("\n")

main()
