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

def Task3 ():
    places = [
        {'name': 'Cairo Tower', 'lat': 30.0444, 'lon': 31.2358, 'type': 'landmark'},
        {'name': 'Pyramids of Giza', 'lat': 29.9792, 'lon': 31.1344, 'type': 'landmark'},
        {'name': 'Khan El-Khalili', 'lat': 30.0444, 'lon': 31.2358, 'type': 'market'}
        ]
    print ('Task3: Here are some places in Egypt:\n')
    for place in places:
        print(f"{place['name']} is located at {place['lat']}, {place['lon']}. It is a {place['type']}.\n")  # This will print the details of each place
    return 0

Task3()