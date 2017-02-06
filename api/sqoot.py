import urllib2
import json
import config

def searchBy(location, radius):
    api_key = config.sqoot('public_key')
    url = 'http://api.sqoot.com/v2/deals/?location=' + location + '&radius=' + radius + '&api_key=' + api_key
    
    json.load(urllib2.urlopen(url))
    
    for item in data['deals']:
        print item['title']
        print item['short_title']
