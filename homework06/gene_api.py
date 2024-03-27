import requests
import json
import csv
from flask import Flask, request
import redis



app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def get_data():
    rd = get_redis_client()
    if request.method=='POST':
    
        data=requests.get("https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json")
        data=data.json()['response']['docs']

#        for i in range(len(data)):        
#            for key in data[i].keys():
#                data[i][key]=str(data[i][key])
            
#            rd.hset(str(i), mapping=data[i])
        data=json.dumps(data)
        rd.set('data', data)

        return("data has been posted to redis.\n")

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


@app.route('/genes', methods=['GET'])
def get_genes():
    rd = get_redis_client()

    data=rd.get('data')
    try:
        data=json.loads(data)
    except TypeError:
        return("Database empty. Submit a post request before trying to access data.\n")
    ret_list=[]
    for dict in data:
        ret_list.append(dict['hgnc_id'])

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
    for dict in data:
        if hgnc_id == dict['hgnc_id']:
            return(dict)

    return("Specified ID not found in data.\n")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


