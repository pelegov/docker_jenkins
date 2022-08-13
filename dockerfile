FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install flask
RUN pip install requests
RUN pip install json
RUN pip install pymysql
EXPOSE 5000
RUN chmod 644 app.py
CMD ["python3", "rest_app.py", "backend_testing.py", "clean_environment.py"]
