FROM python:3.9
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .