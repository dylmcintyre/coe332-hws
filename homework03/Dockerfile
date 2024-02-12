FROM ubuntu:20.04
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip

RUN pip3 install pytest==8.0.0

COPY ml_data_reader.py /code/ml_data_reader.py
COPY gcl_alg.py /code/gcl_alg.py
COPY test_ml_data_reader.py /code/test_ml_data_reader.py
COPY test_gcl_alg.py /cod/test_gcl_alg.py

RUN chmod +rx /code/ml_data_reader.py

ENV PATH="/code:$PATH"
