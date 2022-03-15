FROM python:3.10-slim

COPY ./requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

# Running tests
RUN coverage run -m unittest discover && coverage report -m

CMD python3 /app/app.py
