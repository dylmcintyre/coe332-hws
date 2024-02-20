# **ISS Data Tracker**
This Python script fetches ISS position data from https://spotthestation.nasa.gov/trajectory_data.cfm using the requests library. The file then stores this data and prints summary information about its values.


## **Files Included:**


**iss_tracker.py** is used to read in the csv files and contains functions to calculate and print summary data. 

**test_iss_tracker.py** is used to calculated distances between points on a globe.


**Dockerfile** contains the information needed to build the container that the code is to be run in


##  **Input Data:**

The data from NASA is imported in xml format and should have timestamps and state vectors values for possition and velocity

## Usage
**The following four lines of code can be used to do the following:**
1) pull the container from docker
2) run the container on your machine
3) test the code for errors
4) execute the code using user inputed data
```ruby

docker pull dylmcintyre/iss_tracker:1.0

docker run --rm -it dylmcintyre/iss_tracker:1.0 /bin/bash

pytest code

python3 code/iss_tracker.py
```


**Output:**


The output will include possition values for the first and last entry. It will also output values for all state vectors in the first epoch. Finally, it will output a float which is the average of all epoch's speed in km.

