from sys import argv
import json

script, filename1, filename2 = argv

with open(filename2) as f:
    val = json.load(f)

with open(filename1) as f:
    test = json.load(f)

def val_id(x):
    for i in val['values']:
        if i.get('id') == x:
            return i['value']

def recur(s):
    if s.get('values'):
        for i in s.get('values'):
            recur(i)
    if val_id(s.get('id')):        
        s['value'] = val_id(s.get('id'))
    

for i in test['tests']:
    recur(i)

recur(test)

with open('report.json', 'w') as f:
    json.dump(test,f)