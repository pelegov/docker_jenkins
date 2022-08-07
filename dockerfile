FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install flask
EXPOSE 5000
RUN chmod 644 app.py
CMD ["python3", "rest_app.py"]
