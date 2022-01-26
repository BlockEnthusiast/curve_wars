import csv
import os
import json

cwd = os.getcwd()

def read_csv(filename):
    try:
        data = []
        with open(cwd+"/app/data"+ filename+".csv", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
            # for row in transactions:
        return data
    except:
        return False

def write_csv(filename, data):
    try:
        with open(cwd+"/app/data"+ filename+".csv", 'w') as f:
            w = csv.DictWriter(f, data[0].keys())
            w.writeheader()
            for t in data:
                w.writerow(t)
        return True
    except:
        return False

def read_json(filename):
    # print(cwd+"/app/data"+ filename+'.json')
    try:
        with open(cwd+"/app/data"+ filename+'.json') as f:
           data = json.load(f)
        return data
    except:
        return False

def write_json(filename, data):
    print(cwd+"/app/data"+ filename+'.json')
    try:
        with open(cwd+"/app/data"+ filename+'.json', "w") as f:
            json.dump(data, f)
        return True
    except:
        return False
