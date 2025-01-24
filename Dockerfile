#Copilot: copy fdoor.py to create a dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY fdoor.py .

EXPOSE 8080

CMD ["python", "fdoor.py"]