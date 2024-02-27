import requests
import xmltodict
import math
import logging
import socket
from typing import List
from flask import Flask, request
from math import sqrt



app=Flask(__name__)

def get_data():
    response = requests.get(url="https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml")
    data = xmltodict.parse(response.content)
    data=data['ndm']['oem']['body']['segment']['data']['stateVector']
    return(data)


@app.route('/epochs', methods=['GET'])
def data_with_limit():
    limit=request.args.get('limit', len(get_data()))
    offset=request.args.get('offset', 0)

    try:
        limit=int(limit)
    except(ValueError):
        return 'Error limit must be a positive int \n'
    try:
        offset=int(offset)
    except(ValueError):
        return 'Error: offset must be a positive int \n'

    return_data=[]
    data=get_data()
    for index in range(offset,offset+limit):
        try:
            return_data.append(data[index])
        except(IndexError):
            logging.warning('End of data reached before inputed limit was reached. Returned data is less than limit.')
            break

    return (return_data)

@app.route('/epochs/<int:epoch>', methods=['GET'])
def single_state_vectors(epoch):
    
    try:
        epoch=int(epoch)
    except:
        return("epoch should be a positive integer")
    try:
        epoch_data=get_data()[epoch]
    except(IndexError):
        return("requested epoch index is out of range.")
    
    return_data=[epoch_data['EPOCH'], epoch_data['X']['#text'], epoch_data['Y']['#text'], epoch_data['Z']['#text'], epoch_data['X_DOT']['#text'], epoch_data['Y_DOT']['#text'], epoch_data['Z_DOT']['#text']]
    return(return_data)

@app.route('/epochs/<int:epoch>/speed', methods=['GET'])
def epoch_speed(epoch):
    try:
        epoch=int(epoch)
    except:
        return("epoch should be a positive integer")
    try:
        epoch_data=get_data()[epoch]
    except(IndexError):
        return("requested epoch index is out of range.")
    try:
        speed=sqrt(float(epoch_data['X_DOT']['#text'])**2+float(epoch_data['Y_DOT']['#text'])**2+float(epoch_data['Z_DOT']['#text'])**2)
    except(ValueError):
        return('Error: Non-int values in velocity data.')
    return(str(speed)+'\n')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
