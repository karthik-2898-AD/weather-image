FROM python:3.9-slim
WORKDIR /app
COPY weather_server.py .
COPY templates ./templates
RUN pip install flask requests
EXPOSE 8083
CMD ["python","weather_server.py"]

