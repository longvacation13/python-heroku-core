# https://python-explorer.tistory.com/13
from flask import Flask
app = Flask(__name__) 

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("config\heroku-pro-firebase-adminsdk-na1xm-9e49a017fd.json")
firebase_admin.initialize_app(cred)


@app.route('/') 
def hello_world(): 
 #print(str(cred))   
#  df = pd.read_csv('2020년 ITEM_ID별 실적(센터)_05월.csv')
 # print(df)
#  plt.figure(figsize=(10,5))
#  plt.scatter(df.index, df['day_ord_cnt'])
#  plt.savefig('result\graph\savefig_default.png')
 return "Hello Python!"
 
if __name__ == '__main__': 
 app.run() 
 