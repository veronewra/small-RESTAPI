# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /weavegrid

COPY . .

RUN pip install -r requirements.txt 
