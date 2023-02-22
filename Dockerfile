FROM python:3
ENV PYTHONUNBUFFERED 1
WORKFIR /app
ADD ./app
RUN pip install -r requirements.txt