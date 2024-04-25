from jobs import get_job_by_id, update_job_status, q, rd, results
import time
import matplotlib.pyplot as plt
import numpy as np
import json



@q.worker
def do_work(jobid):
    update_job_status(jobid, 'in progress')
    data=rd.get('data')

    try:
        data=json.loads(data)
    except TypeError:
        update_job_status(jobid, 'complete')
        return("Database empty. Job results could not be computed.\n")


    hashmap={}



    current_job= get_job_by_id(jobid)
    if current_job['chromosome']==0:

        for entry in data:
            g_type=entry['locus_group']
            if g_type in hashmap.keys():
                hashmap[g_type]+=1
            else:
                hashmap[g_type]=1

        groups, numbs=zip(*hashmap.items())

        plt.bar(groups,numbs, color = "red")
        plt.savefig('my_bar_graph.png')
        plt.title("Types of genes in whole dataset")
    else:
        for entry in data:
            if int(entry['location_sortable'][0:1])==int(current_job['chromosome']):
                g_type=entry['locus_group']
                if g_type in hashmap.keys():
                    hashmap[g_type]+=1
                else:
                    hashmap[g_type]=1

        groups, numbs=zip(*hashmap.items())

        plt.bar(groups,numbs, color = "red")
        plt.savefig('my_bar_graph.png')
        
        tit_text="Types of Genes on Chromosome: "+str(chromosome)
        plt.title(tit_title)

    try:

        with open('my_bar_graph.png', 'rb') as f:
            img = f.read()
            results.hset(jobid, 'image', img)
    except(FileNotFoundError):
        results.hset(jobid, 'image', "No data was found for that given chromosome, so an image was not created.")

    update_job_status(jobid, 'complete')

do_work()
