import requests
import secrets
import codecs
import json


def get_coordinates_from_zip(zip_code):
    r = requests.get(f'http://dev.virtualearth.net/REST/v1/Locations/US/-/{zip_code}/-/-?o=json&inclnb=1&key={secrets.api_key}')
    if r.status_code == 200:
        decoded_data = json.loads(codecs.decode(r.text.encode(), 'utf-8-sig'))
        resources = decoded_data['resourceSets'][0]['resources'][0]
        return {
            "msg": "success",
            "zip info": resources['address'],
            "coordinates": resources['point']['coordinates']
        }
    return {
        "msg": "return of zip code failed.  Status code " + str(r.status_code)
    }


def get_miles_from_zips(origin_point, dest_point):
    distance_obj = {
        "waypoints": [{
            "latitude": origin_point[0],
            "longitude": origin_point[1]
        }, {
            "latitude": dest_point[0],
            "longitude": dest_point[1]
        }]
    }
    url = f'https://dev.virtualearth.net/REST/v1/Routes/Truck?key={secrets.api_key}'
    x = requests.post(url, json=distance_obj)
    results = json.loads(codecs.decode(x.text.encode(), 'utf-8-sig'))
    return results


if __name__ == '__main__':
    origin = get_coordinates_from_zip(60515)
    destination = get_coordinates_from_zip(60661)
    print(get_miles_from_zips(origin['coordinates'], destination['coordinates']))
