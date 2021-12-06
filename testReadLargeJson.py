import json as js
dataPath = "../yelp_academic_dataset_review.json"
f = open(dataPath,'r') 
f.read()
with open(dataPath) as f:
    for line in f:
        j_content = json.loads(line)
        break