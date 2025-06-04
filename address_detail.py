from geopy.geocoders import Nominatim

def get_coords_from_address(address_string):
    geolocator = Nominatim(user_agent="my_geocoder")
    try:
        location = geolocator.geocode(address_string)
        if location:
            print(f"Coordinates for '{address_string}':\
                    Latitude = {location.latitude}, \
                    Longitude = {location.longitude}")
            return location.address
        else:
            return f"Address details not found for '{address_string}'."
    except Exception as e:
        return f"An error occurred: {e}"

place_name = input("Enter a name to find address: ")
address_details = get_coords_from_address(place_name)
print(f"Address details: {address_details}")