import json 
with open("full-synapse-api.json", 'r') as file:
    data = json.load(file)
    sub = "/_matrix/client/v3/rooms/{roomId}/"
    for key in data['paths']:
        if (sub in key): 
            print (key)
    