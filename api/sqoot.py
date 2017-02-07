import urllib2
import json
import config

#http://docs.sqoot.com/v2/deals.html for api documentation

api_key = config.sqoot('apiKey_public')

url = 'http://api.sqoot.com/v2/deals/?location=NY&radius=100&per_page=100&api_key=' + str(api_key)
print (url)
    
json_obj = json.load(urllib2.urlopen(url))
    
data = json.load(json_obj)
    
for deals in data['deals']:
    print (deals['deal']['title'])
    print (deals['deal']['short_title'])
    print '$' + str((deals['deal']['price']))
    print ("")
