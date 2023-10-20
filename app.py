#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask


# In[ ]:


from flask import Flask
from flask import render_template,request
import json
import time
import requests

app = Flask(__name__)


headers = {
    "Authorization" : "Token r8_ZDRyU3lkQgVIhDX7GiaCdc6QShqO8t51u2k0K",
    "Content-Type"  : "application/json"
}

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("question")
        print(q)
    
        body = json.dumps(
            {
                "version" : "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
                "input"   :  
                {
                "prompt"  :  q
                }
            }
        )
        output = requests.post("https://api.replicate.com/v1/predictions", data=body,headers=headers)
        time.sleep(10)
        get_url = output.json()["urls"]["get"]
        get_result = requests.post(get_url,headers=headers).json()["output"]
        
        
        return(render_template("index.html",result=get_result[0]))
    else:
        return(render_template("index.html",result="waiting....."))

if __name__ == "__main__":
    app.run(port=1212)


# In[ ]:





# In[ ]:




