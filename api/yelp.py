import requests
import config

##########################
#### GLOBAL VARIABLES ####
##########################

base_url = 'https://api.yelp.com/v3/businesses/'
data = {'grant_type': 'client_credentials',
        'client_id': config.yelp['client_id'],
        'client_secret': config.yelp['client_secret']}

###########################


def get_search_parameters(location):
    # Parameters: term, location, latitude, longitude, radius, categories,
    # locale, limit, offset, sort_by, price, open_now, open_at, attributes

    params = {'term': 'restaurant',
              'location': str(location),
              'radius': '1000',
              'limit': '5'}

    return params


def main():
    #Location: address, neighborhood, city, state, zip, latitude, longitude
    location = 11228

    #get access token for authentication
    token = requests.post('https://api.yelp.com/oauth2/token', data=data)
    access_token = token.json()['access_token']

    #get parameters for request
    url = base_url + 'search'
    params = get_search_parameters(location)
    headers = {'Authorization': 'bearer %s' % access_token}

    request_list = requests.get(url=url, params=params, headers=headers)
    business_list = request_list.json()

    #request business information individually using business id
    for business in business_list['businesses']:
        print (business['name'])

        url = base_url + business['id']
        request_information = requests.get(url=url,headers=headers)
        business_information = request_information.json()

        print (business_information['hours'])

main()