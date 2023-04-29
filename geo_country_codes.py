import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

def print_country_code_from_geocoding() -> None:
    api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    address = input('Enter location: ')

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

#print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
#print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
        

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        
    country_code = False    
    address_components = js['results'][0]['address_components']
    for location in address_components:
        if 'country' in location['types']:
            print('Country code:', location['short_name'])
            country_code = True
    if country_code == False:
        print('No country code found.')


# The original examples are a loop, write this to run once
if __name__ == "__main__":
    print_country_code_from_geocoding()
