def Task1 ():
    my_list = ['Cairo', 'Alexandria', 'Giza', 'Luxor', 'Aswan']
    print(f"Task1: {my_list[2]}\n")  # This will print 'Giza' since list indexing starts at 0
    return 0

Task1()

def Task2 ():
    my_dict = {'name': 'Cairo Tower', 'lat': 30.0444, 'lon': 31.2358, 'type': 'landmark'}
    print(f"Task2: {my_dict['name']} is located at {my_dict['lat']}, {my_dict['lon']}. It is a {my_dict['type']}.\n")  # This will print the details of the landmark
    return 0

Task2()

places = [
        {'name': 'Cairo Tower', 'lat': 30.0444, 'lon': 31.2358, 'type': 'landmark'},
        {'name': 'Pyramids of Giza', 'lat': 29.9792, 'lon': 31.1344, 'type': 'landmark'},
        {'name': 'Khan El-Khalili', 'lat': 30.0444, 'type': 'market'},
        {'name': 'Luxor Temple', 'lat': None, 'lon': None, 'type': 'temple'}
        ]

def Task3 ():
    print ('Task3: Here are some places in Egypt:\n')
    for place in places:
        lat = place.get('lat')
        lon = place.get('lon')
        if lat is None or lon is None:
            print(f"{place['name']} does not have valid coordinates.\n")  # This will print a message if the coordinates are None
        else:
            print(f"{place['name']} is located at {place['lat']}, {place['lon']}. It is a {place['type']}.\n")  # This will print the details of each place
    return 0

Task3()

def Task4 ():
    print ('Task4: Verifying coordinates of places:\n')
    for place in places:
        lat = place.get('lat')
        lon = place.get('lon')
        if lat is None or lon is None:
            verified = False
            print(f"{place['name']}, {verified} \n")  # This will print a message if the coordinates are None            
        else:
            verified = True
            print(f"{place['name']}, {verified} \n")  # This will print the details of each place
    return 0

Task4()

class KeynotFoundError(Exception):
    pass

def Task5 ():
    print ('Task5: Checking for missing keys in places:\n')
    for place in places:
        try:
            if 'name' not in place or 'lat' not in place or 'lon' not in place or 'type' not in place:
                raise KeynotFoundError(f"Missing key in {place}")
            else:
                print(f"{place['name']} has all required keys.\n")  # This will print the details of each place
        except KeynotFoundError as e:
            print(f'{e}\n')  # This will print an error message if a key is missing
    return 0

Task5()

data = {
        'elements': [
            {'name': 'empire state building', 'location': {'lat': 40.7488, 'lon': -73.9854}, 'type': 'landmark'},
            {'name': 'statue of liberty', 'location': {'lat': 40.6892, 'lon': -74.0445}, 'type': 'landmark'},
            {'name': 'central park', 'location': {'lat': 40.7850, 'lon': -73.9682}, 'type': 'park'}
        ]
}
def Task6 ():
    print ('Task6: parsing nested data structures:\n')
    for element in data['elements']:
        name = element.get('name')
        location = element.get('location', {})
        lat = location.get('lat')
        lon = location.get('lon')
        type_ = element.get('type')
        print(f"{name} is located at {lat}, {lon}. It is a {type_}.\n")  # This will print the details of each element
    return 0

Task6()