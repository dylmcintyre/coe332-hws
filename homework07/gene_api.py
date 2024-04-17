import requests
import json
import csv
from flask import Flask, request
import redis
from jobs import add_job, get_job_by_id, update_job_status, get_jids


app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def get_data():
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
    return redis.Redis(host='redis-db', port=6379, db=0)


@app.route('/jobs', methods=['POST', 'GET'])
def jobs_id():
    if request.method=='POST':
        inputs = request.get_json()
        job_nums=1
        try:
            job_nums = int(inputs.get('number'))
        except(TypeError):
            return("Please input an integer for number of jobs\n")
        for i in range(job_nums):
            add_job(status="submitted")
        if job_nums==1:
            return("The job has been submitted. Perform a get request to get all active job id's\n")
        else:
            return(str(job_nums)+" new jobs have been submitted. Perform a get request to get all active job id's\n")
    if request.method=='GET':
        if len(get_jids())<5:
            return("No current jobs. Use a post request to create new jobs.\n")
        else:
            jid_string=get_jids()[3:-3]
            jid_list=jid_string.split("', b'")
            return(jid_list)

@app.route('/jobs/<jobid>', methods=['GET'])
def get_job_from_id(jobid):
    try:
        job_dict=get_job_by_id(jobid)
        return(job_dict)
    except:
         return("Specified ID not found in jobs.\n")






@app.route('/genes', methods=['GET'])
def get_genes():
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
def get_specific_dict(hgnc_id):
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


