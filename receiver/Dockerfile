#pull base images
FROM python:3.11

#add files
ADD main.py . 

RUN pip install beautifulsoup4
RUN pip install pika
RUN pip install requests


CMD [ "python", "./main.py" ]
