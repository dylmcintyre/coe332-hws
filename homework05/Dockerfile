FROM python:3.9
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN pip3 install pytest==8.0.0
Run pip3 install requests

COPY iss_tracker.py /app/app.py

ENTRYPOINT ["python"]
CMD ["app.py"]
