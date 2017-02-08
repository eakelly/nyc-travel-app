import requests
from bs4 import BeautifulSoup
import os
import sys

# returnAirport:
# twoWayTrip:true
# fareType:DOLLARS
# originAirport:LGA
# destinationAirport:SFO
# outboundDateString:02/08/2017
# returnDateString:02/11/2017
# adultPassengerCount:1
# seniorPassengerCount:0
# promoCode:
# submitButton:true


def main():
    payload = {
        "returnAirport": "",
        "twoWayTrip": True,
        "fareTrip": "DOLLARS",
        "originAirport": "LGA",
        "destinationAirport": "SJC",
        "outboundDateString": "02/19/2017",
        "returnDateString": "03/10/2017",
        "adultPassengerCount": "1",
        "seniorPassengerCount": "0",
        "promoCode": "",
        "submitButton": True
    }

    r = requests.post("https://www.southwest.com/flight/search-flight.html?preserveBugFareType=TRUE", data=payload)

    soup = BeautifulSoup(r.content, 'html.parser')

    # for row in soup.findAll('$'):
    #     if len(row.text) < 6:
    #         print(len(row))

    departing = []
    returning = []

    for row in soup.findAll('input', {"class": "upsellOutboundRadio"}):
        # print(row)
        departing.append(row['title'])
        print(row['title'])

    for row in soup.findAll('input', {"class": "upsellInboundRadio"}):
        returning.append(row['title'])
        print(row['title'])

    with open("save_swa_scrape.txt", 'w+', encoding='utf-8') as writefile:
        writefile.write(soup.prettify())