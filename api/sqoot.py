import urllib2
import json
import config

def searchBy(location, radius):
    api_key = config.sqoot('public_key')
    url = 'http://api.sqoot.com/v2/deals/?location=' + location + '&radius=' + radius + '&api_key=' + api_key
    
    json.load(urllib2.urlopen(url))
    
    for deals in data['deals']:
        print (deals['deal']['title'])
        print (deals['deal']['short_title'])
        print '$' + str((deals['deal']['price']))
        print ("")
