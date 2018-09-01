# Pilody
Pilody was a small media center connected to Youtube concept written in python with a REST API to control it designed 
to work on Raspberry pi.  

## Installation
* Install python3 and pip3
* Clone the repository
* Install the "requirements.txt" dependencies
* Execute the application
```bash
$ sudo apt install python3 python3-pip
$ git clone https://github.com/zessirb/pilody.git
$ cd pilody && pip3 install -r requirements.txt
$ FLASK_APP=flaskapp python -m flask run --host=0.0.0.0
```

## Using the REST API
After starting the application, a Swagger-UI is served at the url `localhost:5000/docs`. 
You might have a CORS issue, then you won't have the choice but to change the swagger.json URL from the swagger UI 
to match the direct URL of your application. From this URL, you can use various endpoints to pilot the media center.
