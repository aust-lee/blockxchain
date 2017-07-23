import json

with open('data\stream_trump.json') as data_file:    
    data = json.load(data_file)

print data
