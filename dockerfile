FROM python:3.7-alpine
WORKDIR /app
COPY getUser.py /app
CMD python3 getUser.py
