# Base Image
FROM python:3.11.5-slim

# Specifying WORKDIR location
WORKDIR /Users/bharatkhanna/Library/CloudStorage/OneDrive-Personal/Classes/Batch 04/ML OPS/mojorojo_flask/DOCKER

# Copying Requirements to WORKDIR
COPY requirements.txt ./

# Upgrading Pip and Installing Requirements recursively
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

 # COPY all the files to WORKDIR
 COPY . .

 # Command to run flask app
CMD [ "python3", "-m", "flask", "--app", "predictions.py", "run", "--host=0.0.0.0" ]


