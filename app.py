# https://python-explorer.tistory.com/13
from flask import Flask
app = Flask(__name__) 

import numpy as np 


@app.route('/') 
def hello_world(): 
 return 'Hello Python Flask' 
 
if __name__ == '__main__': 
 app.run() 
 