import eventful
import config

api = eventful.API(config.eventful['apiKey'])

# If you need to log in:
# api.login('username', 'password')

events = api.call('/events/search', q='music', l='New York', include='price')
for event in events['events']['event']:
    print "%s at %s - %s" % (event['title'], event['venue_name'], event['description'])
    print "Time: %s" % (event['start_time'])
    print "Price: %s" % (event['price'])
    print " "

events = api.call('/events/search', q='concert', l='New York', include='price')
for event in events['events']['event']:
    print "%s at %s - %s" % (event['title'], event['venue_name'], event['description'])
    print "Time: %s" % (event['start_time'])
    print "Price: %s" % (event['price'])
    print " "
