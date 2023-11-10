# Team T06 - IT496 CP3 
# This is the main file that is used to run the application

# importing libraries
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import numpy as np
import pickle  
import pandas as pd


# Initialize app using FastAPI
app = FastAPI()

# IP Address and Port Number to run the app
IpAddr = '127.0.0.1'
Port = 8000

# function that returns the content
# of given html file, pass the relative path
def getHtmlFileContents(path):
    # read the file contents and return
    with open(path) as htmlFile:
        fileContents = htmlFile.read()
    return fileContents

#default route
@app.get('/')
def index():
    return HTMLResponse(content=getHtmlFileContents('./Frontend/index.html'), media_type='text/html')

# Run the API with Uvicorn
if __name__ == '__main__':
   uvicorn.run(app, host=IpAddr, port=Port)


# To run the server, enter the following command in terminal  
# python -m uvicorn server:app --reload