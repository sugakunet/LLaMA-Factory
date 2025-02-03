f = open("/home/ubuntu/austrailia-east-1/works_with_references_20250131.json")
#lines = [f.readline().strip() for i in range(1000000)]
lines = f.readlines()
js = [{"text": line.strip()} for line in lines if len(line) < 20000]
import json
import random
json.dump(random.sample(js, 700000), open("/home/ubuntu/austrailia-east-1/works_with_references.json","w"))

f = open("/home/ubuntu/austrailia-east-1/works_20250131.json")
#lines = [f.readline().strip() for i in range(1000000)]
lines = f.readlines()
js = [{"text": line.strip()} for line in lines if len(line) < 20000]
import json
import random
json.dump(random.sample(js, 3000000), open("/home/ubuntu/austrailia-east-1/works.json","w"))
#random.shuffle(js)
#json.dump(js, open("/home/ubuntu/austrailia-east-1/works.json","w"))
