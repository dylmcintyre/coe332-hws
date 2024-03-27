# **Gene Data App**
This Python script establishes a flask app which fetches Gene data from https://www.genenames.org/download/archive/ using the requests library. The app then 
allows the user to post request the data into a redis database, delete, and make get requests of the data.


## **Files Included:**


**genes_api.py** is used to initialize the applicaiton and contains functions to read in the data and return requested data entries or values.


**Dockerfile** contains the information needed to build the container that the code is to be run in


**docker-compose.yaml** automates running and ending the docker and redis containers.


**requirements.txt** holds the dependencies so the Dockerfile has access to them



##  **Input Data:**

The data is from HUGO and comes in json format

## Startup:
Start by downloading the files to your device.
**The following lines of code can be used to pull, start, test, and close the application:**

```ruby
#Pull the container from Dockerhub and run the application in the background

docker pull dylmcintyre/gene_api:1.0
docker-compose up --build -d

```

**Here are sample get requests from the data**
```ruby
curl -X POST "http://0.0.0.0:5000/data"
#Pulls the data from the host website and loads it into the databse

curl -X GET "http://0.0.0.0:5000/data"
#returns a list of dictionaries of the entire dataset

curl -X DELETE "http://0.0.0.0:5000/data"
#Deletes the current stored dictionary data

curl -X GET "http://0.0.0.0:5000/genes"
#returns a list of all of the hgnc id's in the dataset

curl -X GET "http://0.0.0.0:5000/genes/<hgnc_id>"
#returns a dictionary of all of the data for the inputed hgnc id value
```

**In order to stop the containers from running run the following command**
```ruby
docker-compose down
```
