from flask import Flask, request,jsonify
import numpy as np
import pandas as pd 
app = Flask(__name__)
def Split(test_list): 
    ev_li = test_list[::2] 
    od_li=test_list[1::2] 
    return(list(np.array(od_li)-np.array(ev_li)))

def appearance(intervals):
    d_v=intervals.values()
    d_k=intervals.keys()
    d_new={"lesson":[],"pupil":[],"tutor":[]}
    d_new_sum={"lesson":[],"pupil":[],"tutor":[]}
    for i in np.arange(len(d_v)):
        input_=list(d_v)[i]
        value=Split(input_)
        d_new[list(d_k)[i]].append(value) 
        d_new_sum[list(d_k)[i]].append(sum(value))    
    return d_new,d_new_sum

d={ 
  'lesson': [1594663200, 1594666800], 
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472], 
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473] }
all_,sum_=appearance(d)


@app.route('/')
def pred():
  return str(sum_)


if __name__ == "__main__":
   app.run(port=8889, debug=True)

