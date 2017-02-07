import urllib2
import json
import config

def searchBy(location, radius):
    api_key = config.sqoot('apiKey_public')
    url = 'http://api.sqoot.com/v2/deals/?location=' + location + '&radius=' + radius + '&api_key=' + api_key
    
    json_obj = json.load(urllib2.urlopen(url))
    
    data = json.load(json_obj)
    
    for deals in data['deals']:
        print (deals['deal']['title'])
        print (deals['deal']['short_title'])
        print '$' + str((deals['deal']['price']))
        print ("")
