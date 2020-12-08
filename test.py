import requests
import json

Base = "http://127.0.0.1:5000/"

my_list = [['kill', 'feel', 'depress'], 
            ['love', 'big', 'family']]

for i in my_list:
    response = requests.post(Base + "Posts", {"tweet": json.dumps(i)})
    print(response.json())