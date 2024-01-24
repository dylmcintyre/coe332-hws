

import json

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

with open('Meteorite_Landings.json', 'r') as f:
     ml_data = json.load(f)

print('average mass (g): ' , compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'))
print('dictionary containing the classes of meteorite and their counts: ', count_class(ml_data['meteorite_landings'], 'recclass'))
print('meteorite with the highest mass (g): ', max_mass(ml_data['meteorite_landings'], 'mass (g)'))
print('meteorite with the lowest mass (g):', min_mass(ml_data['meteorite_landings'], 'mass (g)'))
