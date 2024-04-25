import requests
import json
import csv
from flask import Flask, request, send_file
import redis
from jobs import add_job, get_job_by_id, update_job_status, get_jids, delete_jdb, results


app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def get_data()->list:


    """
    Route to handle the storage and retrieval of genetic data from a Redis database.
    Supports GET, POST, and DELETE methods.

    - POST: Fetches genetic data from a specified external API, stores it in Redis, and confirms data storage.
    - GET: Retrieves and returns the genetic data stored in Redis. If the database is empty, prompts for a POST request.
    - DELETE: Clears all data stored in the Redis database.
    """

    rd = get_redis_client()
    if request.method=='POST':
    
        data=requests.get("https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json")
        data=data.json()['response']['docs']

        data=json.dumps(data)
        rd.set('data', data)

        return("Data has been posted to redis.\n")

    if request.method=='GET':
        ret_list=[]
        data=rd.get('data')
        try:
            data=json.loads(data)
            return(data)
        except TypeError:
            return("Database empty. Submit a post request before trying to access data.\n")
    if request.method=='DELETE':
        rd.flushdb()
        return("Redis data has been deleted.\n")
def get_redis_client():

    """
    Initializes and returns a Redis client connected to a specified Redis database.
    """
    return redis.Redis(host='redis-db', port=6379, db=0)


@app.route('/jobs', methods=['POST', 'GET', 'DELETE'])
def jobs_id()->list:

    """
    Initializes and returns a Redis client connected to a specified Redis database.
    """
    if request.method=='POST':
        inputs = request.get_json()
        chromosome_number=0
        try:
            chromosome_numer = int(inputs["chromosome"])
        except(TypeError):
            return("Please input an integer for the chromosome number.\n")

        add_job(chromosome_number, status="submitted")
        return("The job has been submitted. Perform a get request to get all active job id's\n")
    if request.method=='GET':
        if len(get_jids())<5:
            return("No current jobs. Use a post request to create new jobs.\n")
        else:
            jid_string=get_jids()[3:-2]
            jid_list=jid_string.split("', b'")
            return(jid_list)

    if request.method=='DELETE':
        delete_jdb()
        return("Jobs Deleted.")

@app.route('/jobs/<jobid>', methods=['GET'])
def get_job_from_id(jobid)->dict:

    """
    Route to manage job submissions and queries about jobs related to genomic data processing.
    Supports POST, GET, and DELETE methods.

    - POST: Submits a new job with a specified chromosome number.
    - GET: Retrieves a list of job IDs. If fewer than 5 jobs are present, prompts to submit more jobs.
    - DELETE: Clears all jobs from the job database.
    """

    try:
        job_dict=get_job_by_id(jobid)
        return(job_dict)
    except:
         return("Specified ID not found in jobs.\n")




@app.route('/download/<jobid>', methods=['GET'])
def download(jobid)->dict:

    """
    Route to retrieve information about a specific job using its job ID.
    Supports only the GET method.

    - GET: Returns details of a job if the specified job ID is found. If not found, returns an error message.
    """

    path = f'/app/{jobid}.png'
    with open(path, 'wb') as f:
        f.write(results.hget(jobid, 'image'))   # 'results' is a client to the results db
    return send_file(path, mimetype='image/png', as_attachment=True)




@app.route('/genes', methods=['GET'])
def get_genes()->list:

    """
    Route to retrieve a list of HGNC IDs from stored genetic data in Redis.
    Supports only the GET method.

    - GET: Returns a list of all HGNC IDs from the stored data. If the database is empty,
            prompts for a POST request to populate data.
    """

    rd = get_redis_client()

    data=rd.get('data')
    try:
        data=json.loads(data)
    except TypeError:
        return("Database empty. Submit a post request before trying to access data.\n")
    ret_list=[]
    for dictionary in data:
        ret_list.append(dictionary['hgnc_id'])

    return(ret_list)

@app.route('/genes/<hgnc_id>', methods=['GET'])
def get_specific_dict(hgnc_id)->dict:

    """
    Route to retrieve specific genetic data by HGNC ID from stored data in Redis.
    Supports only the GET method.

    - GET: Returns the genetic data dictionary for the specified HGNC ID. If the ID is not found,
            returns an error message. If the database is empty, prompts for a POST request to populate data.
    """

    rd = get_redis_client()
    data=rd.get('data')
    try:
        data=json.loads(data)
    except TypeError:
        return("Database empty. Submit a post request before trying to access data.\n")
    ret_list=[]
    for dictionary in data:
        if hgnc_id == dictionary['hgnc_id']:
            return(dictionary)

    return("Specified ID not found in data.\n")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


