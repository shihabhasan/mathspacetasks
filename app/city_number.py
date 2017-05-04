import hashlib

def city_number(city_name):
    if isinstance(city_name, int):
        raise ValueError('Input should not be integer. Please provide the city name correctly ')
    try:
        city_name = city_name.lower().encode('utf-8')
    except ValueError:
        return "Please provide the city name correctly"
    hash_number = int(hashlib.sha256(city_name).hexdigest(), 16) % 10**4
    return hash_number

