import requests
from bs4 import BeautifulSoup
import os
import sys
from tabulate import tabulate

# searchType:simple
# bookingPostVerify:RTR_YES
# bundled:off
# deltaOnly:off
# dl:y
# departureTime:AT
# returnTime:AT
# directServiceOnly:off
# dispatchMethod:findFlights
# fareBundle:B5-Coach
# flexMainRTRTravelDate:off
# preferItinId:
# medallionTraveler:0
# displayPreferredOnly:0
# calendarSearch:false
# pricingSearch:true
# directServiceOnly:off
# hiddenFieldsId:
# awardTravel:false
# tripTypeRadio:on
# tripType:ROUND_TRIP
# originCity:JFK
# destinationCity:NRT
# departureDate:02/14/2017
# returnDate:03/20/2017
# flexExactRadio:on
# is_Flex_Search:false
# action:findFlights
# pageName:advanceSearchPage
# datesFlexible:false
# flexDays:3
# cabinFareClass:economyBasic
# cashMilesRadio:on
# is_award_travel:false
# paxCount:1
# :cq_csrf_token:undefined


def main():
    payload = {
        "searchType": "simple",
        # "bookingPostVerify":"RTR_YES",
        "bundled": "off",
        "deltaOnly": "off",
        "dl": "y",
        "departureTime": "AT",
        "returnTime": "AT",
        "directServiceOnly":"off",
        "dispatchMethod": "findFlights",
        "fareBundle": "B5-Coach",
        "flexMainRTRTravelDate": "off",
        "medallionTraveler": 0,
        "displayPreferredOnly": 0,
        "calendarSearch": False,
        "pricingSearch": True,
        "directServiceOnly": "off",
        "awardTravel": False,
        "tripTypeRadio": "on",
        "tripType": "ROUND_TRIP",
        "originCity": "JFK",
        "destinationCity": "HND",
        "departureDate": "02/14/2017",
        "returnDate": "03/10/2017",
        "flexExactRadio": "on",
        "is_Flex_Search": False,
        "action": "findFlights",
        "pageName": "advanceSearchPage",
        "datesFlexible": False,
        "flexDays": 3,
        "cabinFareClass": "economyBasic",
        "cashMilesRadio": "on",
        "is_award_travel":False,
        "paxCount": 1,
        "cq_csrf_token":"undefined"
    }

    r = requests.post("https://www.delta.com/air-shopping/findFlights.action", data=payload)
    print(r.status_code)
    print(r.text)
    print(r.url)
    # print(r.text)
    soup = BeautifulSoup(r.content, 'html.parser')

    for row in soup.findAll('$'):
        if len(row.text) < 6:
            print(len(row))
    #
    # departing = []
    # returning = []
    #
    # for row in soup.findAll('input', {"class": "upsellOutboundRadio"}):
    #     row = row['title'].split(" ")
    #     row.pop(0)
    #     row.pop(0)
    #     row.pop(3)
    #     row.pop(4)
    #     row.pop(5)
    #     row.pop(5)
    #     row.pop(5)
    #     row.pop(5)
    #     row.pop(5)
    #     departing.append(row)
    #
    #
    # for row in soup.findAll('input', {"class": "upsellInboundRadio"}):
    #     row = row['title'].split(" ")
    #     row.pop(0)
    #     row.pop(0)
    #     row.pop(3)
    #     row.pop(4)
    #     row.pop(5)
    #     row.pop(5)
    #     row.pop(5)
    #     row.pop(5)
    #     row.pop(5)
    #     returning.append(row)
    #     # print(row['title'])
    #
    # print(tabulate(departing, ["Flight #", "Price", "Departure time", "Arrival time", "Stops"]))
    # print("\n")
    # print(tabulate(returning, ["Flight #", "Price", "Departure time", "Arrival time", "Stops"]))

    # with open("save_swa_scrape.txt", 'w+', encoding='utf-8') as writefile:
    #     writefile.write(soup.prettify())

main()