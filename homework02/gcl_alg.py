import math
import logging
def gcl_alg(lat1, lon1, lat2, lon2):
    """
    Calculates the great-circle distance between two points on the Earth's surface using the Haversine formula.

    Args:
        lat1 (float): Latitude of the first point in degrees.
        lon1 (float): Longitude of the first point in degrees.
        lat2 (float): Latitude of the second point in degrees.
        lon2 (float): Longitude of the second point in degrees.

    Returns:
        float: The distance between the two points in kilometers.

    Raises:
        TypeError: If any of the input arguments are not of type float.
        ValueError: If any of the input arguments are invalid for conversion to radians.
    """
    try:
        
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
    except TypeError:
        logging.error('Non float value found in input for gcl_alg')
        raise(TypeError)
        return(None)
    except ValueError:
        logging.error('Invalid data input into gcl_alg')
        raise(TypeError)
        return(None)

    # Calculate the differences between the latitudes and longitudes
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    # Radius of the Earth in kilometers
    R = 6371.0

    # Calculate the distance
    distance = R * c
    if distance<0.05:
        logging.debug('Very small distance found. Inputed points to gcl_alg may be identical')
    return distance

