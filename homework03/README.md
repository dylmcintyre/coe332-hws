# **Meteorite Landing Data Analysis**

This Python script analyzes meteorite landing data stored in a CSV file. It provides summary statistics about the meteorites, calculates distances between meteorites and specified locations, and utilizes a great-circle algorithm to compute geographical distances. For portability reasons, the script can optionally be run in a docker container.


## **Files Included:**


**ml_data_reader.py** is used to read in the csv files and contains functions to calculate and print summary data. 

**gcl_alg.py** is used to calculated distances between points on a globe.

**test_ml_data_reader.py** and **test_gcl_alg.py** are used to test these two scripts for functionality.

**Dockerfile** contains the information needed to build the container that the code is to be run in

**Diagram.png** is a visual diagram displaying the relationship between the files in the program

**Program Flow:**

![Diagram.png](https://github.com/dylmcintyre/coe332-hws/blob/main/homework03/Diagram.png)
This diagram demonstrates the relationship between different files and components of the program. The user runs the docker container and mounts their input data through the command line. The ml_data_reader and gcl_alg files read in and process the data before returning output to the command line while the two test files run error checks on these files using pytest.

##  **Input Data:**

The CSV file should have columns for latitude, longitude, mass, and other relevant information.

## Usage
**The following four lines of code can be used to do the following:**
1) pull the container from docker
2) run the container on your machine
3) test the code for errors
4) execute the code using user inputed data
```ruby

docker pull dylmcintyre/ml_data_reader:1.0

docker run --rm -it -v $PWD/["DATA_FILE_NAME"].csv:/data/["DATA_FILE_NAME"].csv dylmcintyre/ml_data_reader:1.0 /bin/bash 

pytest code

python3 code/ml_data_reader.py data/["DATA_FILE_NAME"].csv
```

Where DATA_FILE_NAME is the name of the csv file containing relavent meteorite landing data

**Alternatively to run the script without creating a docker container (Not Recomended):**

      python3 ml_data_reader.py ["DATA_FILE_NAME"].csv

**Output:**


The output will include summary statistics of the data including the max and min mass of meteorites in grams, the distance between austin and the largest meteorite, and the distance between two sample meteorites.

## **Data:**
Relevent data can be found here: https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data
This data includes meteorite landing information and can be copied into the current directory and passed into the code as described above

