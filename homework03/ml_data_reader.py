

import csv
import logging
import argparse
from gcl_alg import gcl_alg
import socket
from typing import List


def max_mass(a_list_of_dicts: List[dict], a_key_string: str) -> list:
    """
    Finds the maximum value associated with a specified key in a list of dictionaries.

    Args:
        a_list_of_dicts (list): A list of dictionaries containing the data.
        a_key_string (str): The key to search for the maximum value.

    Returns:
        tuple: A tuple containing the index associated with the maximum value and the maximum value itself.
    """


    max_mass=0.0
    index_max=0
    for i in range(len(a_list_of_dicts)):
        try:
            current=float(a_list_of_dicts[i][a_key_string])
            if current>max_mass:
                max_mass=current
                index_max=i
        except TypeError:
            logging.warning(f'encountered non-float type ,{type(a_list_of_dicts[i][a_key_string])}, in max_mass')
        except ValueError:
            logging.warning(f'encontered non-float value "{a_list_of_dicts[i][a_key_string]}" in max_mass')
    if max_mass==None or max_mass==0.0:
        raise ValueError('List passed in does not have valid, possitive number values')
    return(index_max, max_mass)

def min_mass(a_list_of_dicts: List[dict], a_key_string: str) -> list:
    """
    Finds the minimum value associated with a specified key in a list of dictionaries.

    Args:
        a_list_of_dicts (list): A list of dictionaries containing the data.
        a_key_string (str): The key to search for the minimum value.

    Returns:
        tuple: A tuple containing the index associated with the minimum value and the minimum value itself.
    """

    min_mass=float(a_list_of_dicts[0][a_key_string])
    index_min=0
    for i in range(1, len(a_list_of_dicts)):
        try:
            current=float(a_list_of_dicts[i][a_key_string])
            if current<min_mass and current>0.1:
                min_mass=current
                index_min=i
        except TypeError:
            logging.warning('encountered non-float value in min_mass')
        except ValueError:
            logging.warning(f'encontered non-float value "{a_list_of_dicts[i][a_key_string]}" in min_mass')
    return(index_min, min_mass)

def dist_between_two_ml(a_list_of_dicts: List[dict], index1: int, index2: int, key_string1: str, key_string2: str) -> float:
    """
    Calculates the distance between two geographical coordinates specified by their indices in a list of dictionaries.

    Args:
        a_list_of_dicts (list): A list of dictionaries containing the data.
        index1 (int): The index of the first geographical coordinate.
        index2 (int): The index of the second geographical coordinate.
        key_string1 (str): The key for latitude in the dictionaries.
        key_string2 (str): The key for longitude in the dictionaries.

    Returns:
        float or None: The distance between the two coordinates, or None if calculation fails.
    """
    try:
        lat1=float(a_list_of_dicts[index1][key_string1])
        lon1=float(a_list_of_dicts[index1][key_string2])
        lat2=float(a_list_of_dicts[index2][key_string1])
        lon2=float(a_list_of_dicts[index2][key_string2])
        ret_val=(gcl_alg(lat1,lon1,lat2,lon2))
        return(ret_val)
    except TypeError:
        logging.warning((f'encontered non-float type in dictionary of dist_between_two_ml'))
        return(0)
    except ValueError:
        logging.warning(f'encontered non-float value in dictionary of dist_between_two_ml')
        return(0)

def dist_between_location_and_ml(a_list_of_dicts: List[dict], index: int, key_string1: str, key_string2: str, loc_lat: float, loc_lon: float) -> float:
    """
    Calculates the distance between a specified location and a geographical coordinate in a list of dictionaries.

    Args:
        a_list_of_dicts (list): A list of dictionaries containing the data.
        index (int): The index of the geographical coordinate.
        key_string1 (str): The key for latitude in the dictionaries.
        key_string2 (str): The key for longitude in the dictionaries.
        loc_lat (float): The latitude of the specified location.
        loc_lon (float): The longitude of the specified location.

    Returns:
        float or None: The distance between the location and the coordinate, or None if calculation fails.
    """
    try:
        lat1=float(a_list_of_dicts[index][key_string1])
        lon1=float(a_list_of_dicts[index][key_string2])
        lat2=loc_lat
        lon2=loc_lon
    except TypeError:
        logging.warning('encountered non-float value in min/max longitude/latitude')
    except ValueError:
        logging.warning('encontered non-float value in min/max longitude/latitude')
    try:
        ret_val=(gcl_alg(lat1,lon1,lat2,lon2))
    except:
        logging.error('call to great circle algorithm failed.')
        ret_val=None
    return(ret_val)

def main():

    """
    Parses command-line arguments to get the filename of a CSV file containing meteorite landing data.
    Loads the data from the CSV file into a dictionary.
    Computes summary statistics including maximum and minimum mass of meteorites.
    Calculates distances between meteorites and specified locations.
    Prints the summary statistics and distances.

    Args:
        None

    Returns:
        None
    """

    parser = argparse.ArgumentParser(description='Input name of file for input:')
    parser.add_argument('filename', action='store', type=str, help='Please input the name of the csv file')

    args = parser.parse_args()

    filename=args.filename



    ml_data = {}
    ml_data['meteorite_landings'] = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ml_data['meteorite_landings'].append(dict(row))

    print('Summary Statistics:\n')
    max_tuple=(max_mass(ml_data['meteorite_landings'], 'mass (g)'))
    min_tuple=(min_mass(ml_data['meteorite_landings'], 'mass (g)'))
    print('Meteor with Max Mass:')
    print(ml_data['meteorite_landings'][max_tuple[0]]['name'], ', ',max_tuple[1])
    print('Meteor with Min Mass:')
    print(ml_data['meteorite_landings'][min_tuple[0]]['name'], ', ',min_tuple[1])

    
    print('distance between meteorite, ', ml_data['meteorite_landings'][max_tuple[0]]['name'], ', and Austin in km is:')
            
    print(dist_between_location_and_ml(ml_data['meteorite_landings'],max_tuple[0], 'reclat', 'reclong', 30.2672, 97.7431))
    
    print('distance between meteorites, ', ml_data['meteorite_landings'][min_tuple[0]]['name'], ', and, ', ml_data['meteorite_landings'][0]['name'], ', in km is:')
    print(dist_between_two_ml(ml_data['meteorite_landings'],0,1, 'reclat', 'reclong'))
if __name__ == '__main__':
    main()
