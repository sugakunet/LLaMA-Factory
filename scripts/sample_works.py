f = open("/home/ubuntu/austrailia-east-1/works_with_references_20241231.json")
lines = [f.readline().strip() for i in range(1000000)]
js = [{"text": line} for line in lines if len(line) < 20000]
import json
import random
json.dump(random.sample(js, 200000), open("/home/ubuntu/austrailia-east-1/works.json","w"))

