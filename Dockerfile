FROM revolutionsystems/python:3.7.2-wee-optimized-lto

RUN mkdir /code
WORKDIR /code
COPY . /code

RUN pip install -U pip; pip install -e /code/

ENTRYPOINT ["mkpasswd"]
CMD []

