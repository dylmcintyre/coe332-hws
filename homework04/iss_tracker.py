import requests
import xmltodict
import math
import logging
import socket
from typing import List



def range_summary(data: List[dict], index: int)->None: 
    
    """
    Print the summary of the location data for a given index in the provided list of dictionaries.

    Args:
        data (List[dict]): A list of dictionaries containing location data.
        index (int): The index of the data entry to summarize.

    Returns:
        None
    """

    try:
        print("location of first entry, (", data[index]['EPOCH'], "):")
        print("{ ", data[index]['X']['#text'], ", ", data[index]['Y']['#text'], ", ", data[index]['Z']['#text'], " }")
    except KeyError:
        logging.debug('The key used in range_summary cannot be found in the inputed dictionary.')
    except TypeError:
        logging.warning('type error in range_summary.')
    except IndexError:
        logging.error('The inputed index is not found within the inputed list of dictionaries.')


def print_full_epoch(data: List[dict], index: int)->None:
    
    """
    Print the full epoch data (position and velocity) for a given index in the provided list of dictionaries.

    Args:
        data (List[dict]): A list of dictionaries containing epoch data.
        index (int): The index of the data entry to print.

    Returns:
        None
    """
    try:
        print(data[index]['EPOCH'], " (", data[index]['X']['#text'], ", ", data[index]['Y']['#text'], ", ", data[index]['Z']['#text'], ") (",data[index]['X_DOT']['#text'], ", ", data[index]['Y_DOT']['#text'], ", ", data[index]['Z_DOT']['#text'], ")") 
    except KeyError:
        logging.warning('The key used in print_full_epoch cannot be found in the inputed dictionary.')
    except TypeError:
        logging.error('type error in print_full_epoch.')
    except IndexError:
        logging.warning('The inputed index is not found within the inputed list of dictionaries.')



def calc_avg_speed(data: List[dict], list_of_velocity_indices: List[str])->float:
    
    """
    Calculate the average speed based on the provided list of velocity components.

    Args:
        data (List[dict]): A list of dictionaries containing velocity data.
        list_of_velocity_indices (List[str]): A list of keys indicating the velocity components.

    Returns:
        float: The average speed calculated from the given velocity components.
    """


    try:
        summy=0
        count=0
        for dic in data:
            running_sum=0
            for comp in list_of_velocity_indices:
                running_sum+= (float(dic[comp]['#text']))**2
            summy+= math.sqrt(running_sum)
            count+=1
        return(summy/count)

    except KeyError:
        logging.warning('The #text key cannot be found in the inputed dictionary.')
    except TypeError:
        logging.warning('type error in calc_avg_speed.')
    except IndexError:
        logging.warning('The inputed indices is not found within the inputed list of dictionaries.')


def main():
    response = requests.get(url="https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml")
    data = xmltodict.parse(response.content)
    data=data['ndm']['oem']['body']['segment']['data']['stateVector']
    range_summary(data, 0)
    range_summary(data,-1)
    print_full_epoch(data, 0)
    print(calc_avg_speed(data, ['X_DOT', 'Y_DOT', 'Z_DOT']))

if __name__ == '__main__':
    main()
