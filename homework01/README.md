Homework 01: a program to read in Meteorite Landing data of various file types and output summary information of that data

Each file in this project reads in a data file and reports summary statistics of that data. 
Each file outputs:

-The average mass of every meteorite in the data

-A dictionary that holds the count of meteorites for each class type. The key values are the classes of meteorite and the values are the count of that class

-A tuple of the name of the meteorite with the highest mass and the mass of that meteorite in grams

-a tuple of the name of the meteorite with the lowest mass and the mass of that meteorite in grams


Execution:
To execute each file, input the following command into the command line:

    python3 ml_"filetype"_reader.py Meteorite_Landings."filetype"
    
so for a csv file, the command would be:

    python3 ml_csv_reader.py Meteorite_Landings.csv

Files:

-ml_json_reader.py
    Reads in a json file
    
-ml_csv_reader.py
    Reads in a csv file
    
-ml_xml_reader.py
    Reads in a xml file
    
-ml_yaml_reader.py
    Reads in a yaml file
