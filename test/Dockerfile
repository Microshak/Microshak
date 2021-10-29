FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

#docker build -f Dockerfile -t coiny:latest .
EXPOSE 88
CMD ["python", "./app/main.py"]