# **Gene Data App**
This Python script establishes a flask app which fetches Gene data from https://www.genenames.org/download/archive/ using the requests library. The app then 
allows the user to post request the data into a redis database, delete, and make get requests of the data. The app allows for sample jobs to be created that create bar graphs of requested gene data.
The final data will be a bar graph showing the types of genes present on the requested chromosome. To request the types of genes present on all chromosomes, input 0 as the chromosome number.

## **Files Included:**


**genes_api.py** is used to initialize the applicaiton and contains functions to read in the data and return requested data entries or values.


**Dockerfile** contains the information needed to build the container that the code is to be run in


**docker-compose.yaml** automates running and ending the docker and redis containers.


**requirements.txt** holds the dependencies so the Dockerfile has access to them


**worker.py** goes through jobs and creates images with the requested data


**jobs.py** holds methods for the creation and management of jobs and the queue of jobs

**test_genes_api.py** tests the flask routes using pytest to see if basic functionality is happening


**


##  **Input Data:**

The data is from HUGO and comes in json format

## Startup:
**The following lines of code can be used to pull, start, test, and close the application:**

```ruby
#Pull the repository and run the following command:
docker-compose up --build -d

```

**Here are sample get requests from the data**
```ruby
curl -X POST "localhost:5000/data"
#Pulls the data from the host website and loads it into the databse

curl -X GET "localhost:5000/data"
#returns a list of dictionaries of the entire dataset

curl -X DELETE "localhost:5000/data"
#Deletes the current stored dictionary data

curl -X GET "localhost:5000/genes"
#returns a list of all of the hgnc id's in the dataset

curl -X GET "localhost:5000/genes/<hgnc_id>"
#returns a dictionary of all of the data for the inputed hgnc id value
```
**The job system can be managed as so:**
```ruby

curl localhost:5000/jobs  -X POST -d '{"chromosome":1}' -H 'Content-Type: application/json'
#creates a job for the specified chromosome. The chromosome number corresponds to the first integer in the location_sortable field form the original data

curl localhost:5000/jobs
#returns a list of strings holding all current job ID's

curl localhost:5000/jobs/<job_id>
#returns a dictionary holding the specified job ID and the status of that job

curl localhost:5000/jobs -X DELETE
#Deletes all current jobs

curl localhost:5000/download/<job_id> --output output.png
#Downloads the image produced from a completed job

```
**To test the code's basic functionality:**
```ruby
docker ps
#This looks at all active containers
#Copy and paste the container ID into the following command

docker exec -it <container_id> pytest

```


**In order to stop the containers from running run the following command**
```ruby
docker-compose down
```
