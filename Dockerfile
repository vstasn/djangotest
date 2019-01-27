FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /djangotest
WORKDIR /djangotest
COPY requirements.txt /djangotest/
RUN pip install -r requirements.txt
COPY . /djangotest/
