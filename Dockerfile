# ? Selecting the docker image
FROM python:3.10-slim

# ? Defining the workdir directory in the container
WORKDIR /app 
# ? Copy dependencies and install them inside the container
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt 
# ? Copy source code
COPY . . 
# ? Exposing 5000 port of the cointainer
EXPOSE 5000
# ? Running the application 
CMD ["python", "app/main.py"]