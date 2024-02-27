# **ISS Data Tracker App**
This Python script establishes a flask app which fetches ISS position data from https://spotthestation.nasa.gov/trajectory_data.cfm using the requests library. The app then returns ISS data to get requests.


## **Files Included:**


**iss_tracker.py** is used to initialize the applicaiton and contains functions to read in the data and return requested data entries or values.

**test_iss_tracker.py** is used to test files in iss_tracker.py

**Dockerfile** contains the information needed to build the container that the code is to be run in


##  **Input Data:**

The data from NASA is imported in xml format and should have timestamps and state vectors values for possition and velocity

## Usage
**The following four lines of code can be used to do the following:**
1) pull the container from docker
2) run the container on your machine
3) test the code for errors
4) Begin running the application that will be used
```ruby

docker pull dylmcintyre/iss_tracker_flask:1.0

docker run --rm -it dylmcintyre/iss_tracker_flask:1.0 /bin/bash

pytest code

python3 iss_tracker.py

```
**Here are sample get requests from the data**
```ruby
GET "http://127.0.0.1:5000/epochs"
#returns a list of dictionaries of all data

GET "http://127.0.0.1:5000/epochs?limit=1&offset=1"
#returns a list of data values starting at the specified offset value and not exceding the specified limit value in length

GET "http://127.0.0.1:5000/epochs/<epoch:int>"
#returns the data at the index specified by <epoch>

GET "http://127.0.0.1:5000/epochs/<epoch:int>/speed"
#returns the calculated speed at the suplied epoch index
```


**Output:**


The outputs will be in the form of lists of dictionaries or lists of str in the case of a speed request.

