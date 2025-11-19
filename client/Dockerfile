FROM python:3.13-slim
WORKDIR /app
RUN pip install requests
COPY client.py .
CMD [ "python", "client.py" ]
