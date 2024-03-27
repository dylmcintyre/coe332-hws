FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

#RUN pip3 install pytest==8.0.0
#RUN pip3 install requests
#RUN pip3 install xmltodict

COPY gene_api.py /app/app.py

ENTRYPOINT ["python3"]
CMD ["app.py"]
