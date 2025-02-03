import json
import random

N = 100000

#f = open("/home/ubuntu/austrailia-east-1/works_with_references_20250131.json")
#lines = f.readlines()
#random.shuffle(lines)
#for i in range(len(lines)//N):
    #js = [{"text": line.strip()} for line in lines[i*N: (i+1)*N] if len(line) < 20000]
    #json.dump(js, open(f"/home/ubuntu/austrailia-east-1/works_with_references/file_{i}.json","w"))

f = open("/home/ubuntu/austrailia-east-1/works_20250131.json")
#lines = [f.readline().strip() for i in range(1000000)]
lines = f.readlines()
random.shuffle(lines)
for i in range(len(lines)//N):
    js = [{"text": line.strip()} for line in lines[i*N: (i+1)*N] if len(line) < 10000]
    json.dump(js, open(f"/home/ubuntu/austrailia-east-1/works/file_{i}.json","w"))
