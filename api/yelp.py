import rauth
import time
import config

def get_params(location):
    # See the Yelp API for more details
    params = {}
    params["term"] = "restaurant"
    params["location"] = str(location)
    params["radius_filter"] = "2000"
    params["limit"] = "10"

    return params


def get_results(params):
    # Obtain these from Yelp's manage access page
    consumer_key = config.yelp['consumer_key']
    consumer_secret = config.yelp['consumer_secret']
    token = config.yelp['token']
    token_secret = config.yelp['token_secret']

    session = rauth.OAuth1Session(
        consumer_key=consumer_key
        , consumer_secret=consumer_secret
        , access_token=token
        , access_token_secret=token_secret)

    request = session.get("http://api.yelp.com/v2/search", params=params)

    data = request.json()
    session.close()

    return data

def main():
    location = "Hunter College"

    params = get_params(location)
    data = get_results(params)
    time.sleep(1.0)
    for business in data['businesses']:
        print ("%s, Rating: %s" % (business['name'],business['rating']))


main()
