import pytest
import requests

response1 = requests.get('http://localhost:5000/data')
a_representative_entry = response1.json()[0]

response2 = requests.get('http://localhost:5000/genes')

response3 = requests.get('http://localhost:5000/genes/'+response2.json()[0])

response4 = requests.get('http://localhost:5000/jobs')

def test_data_route():
    assert response1.status_code == 200
    assert isinstance(response1.json(), list) == True

def test_genes_route():
    assert response2.status_code == 200
    assert isinstance(response2.json(), list) == True

def test_specific_gene_route():
    assert response3.status_code == 200
    assert isinstance(response2.json(), list) == True

def test_jobs_route():
    assert response4.status_code == 200
    assert isinstance(response2.json(), list) == True
