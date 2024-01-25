
import argparse

import xmltodict

def compute_average_mass(a_list_of_dicts, a_key_string):
    total_mass = 0.
    for i in range(len(a_list_of_dicts)):
        total_mass += float(a_list_of_dicts[i][a_key_string])
    return (total_mass / len(a_list_of_dicts))

def count_class(a_list_of_dicts, a_key_string) -> dict():
    out_dict={}
    for i in range(len(a_list_of_dicts)):
        if a_list_of_dicts[i][a_key_string] in out_dict.keys():
            out_dict[a_list_of_dicts[i][a_key_string]]+=1
        else:
            out_dict[a_list_of_dicts[i][a_key_string]]=1
    return(out_dict)

def max_mass(a_list_of_dicts, a_key_string):
    max_mass=0.
    for i in range(len(a_list_of_dicts)):
        if float(a_list_of_dicts[i][a_key_string])>max_mass:
            max_mass=float(a_list_of_dicts[i][a_key_string])
            name_max=a_list_of_dicts[i]['name']
    return(name_max, max_mass)

def min_mass(a_list_of_dicts, a_key_string):
    min_mass=float(a_list_of_dicts[0][a_key_string])
    name_min=a_list_of_dicts[0]['name']
    for i in range(1, len(a_list_of_dicts)):
        if float(a_list_of_dicts[i][a_key_string])<min_mass:
            min_mass=float(a_list_of_dicts[i][a_key_string])
            name_min=a_list_of_dicts[i]['name']
    return(name_min, min_mass)

parser = argparse.ArgumentParser(description='Input name of file for input:')
parser.add_argument('filename', action='store', type=str, help='Please input the name of the json file')

args = parser.parse_args()

filename=args.filename


with open('Meteorite_Landings.xml', 'r') as f:
    ml_data = xmltodict.parse(f.read())
    ml_data=ml_data['data']


print('Summary Statistics:\n') 

print('average mass (g): ' , compute_average_mass(ml_data['meteorite_landings'], 'mass_g'))
print('dictionary containing the classes of meteorite and their counts: ', count_class(ml_data['meteorite_landings'], 'recclass'))
print('meteorite with the highest mass (g): ', max_mass(ml_data['meteorite_landings'], 'mass_g'))
print('meteorite with the lowest mass (g):', min_mass(ml_data['meteorite_landings'], 'mass_g'))
