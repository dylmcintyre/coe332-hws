# **Meteorite Landing Data Analysis**

This Python script analyzes meteorite landing data stored in a CSV file. It provides summary statistics about the meteorites, calculates distances between meteorites and specified locations, and utilizes a great-circle algorithm to compute geographical distances.


## **Files Included:**


**ml_data_reader.py** is used to read in the csv files and contains functions to calculate and print summary data. 

**gcl_alg.py** is used to calculated distances between points on a globe.

**test_ml_data_reader.py** and **test_gcl_alg.py** are used to test these two scripts for functionality.


##  **Input Data:**

The CSV file should have columns for latitude, longitude, mass, and other relevant information.

## Usage
**Pull the container from docker and run the code inside**

docker pull dylmcintyre/ml_data_reader:1.0

To run the container on your machine: 
docker run --rm -it -v $PWD/["DATA_FILE_NAME"].csv:/data/["DATA_FILE_NAME"].csv dylmcintyre/ml_data_reader:1.0 /bin/bash

To run the program with your data: 
python3 code/ml_data_reader.py data/["DATA_FILE_NAME"].csv

To test the code: 
pytest code



**Run the Script:**

      python3 ml_data_reader.py data.csv

Replace data.csv with the name of your CSV file.

**Output:**


The output will include summary statistics of the data including the max and min mass of meteorites in grams, the distance between austin and the largest meteorite, and the distance between two sample meteorites.

## **Data:**
Relevent data can be found here: https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data
This data includes meteorite landing information and can be copied into the current directory and passed into the code as described above

