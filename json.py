import json
dictionary =[{
    "ID":1000,
    "name" : "John Smith",
    "DOB" : "01/01/2000",
    "Gender" : "F",
    "Age":20,
    "Zipcode" : "08122-2324",
    "Amount" : "1500.20"
    },
    {"ID":2000,
    "name" : "Jim McDonald",
    "DOB" : "02/02/2020",
    "Gender" : "M",
    "Age":25,
    "Zipcode" : "08136-2324",
    "Amount" : "1500.20"
    },
    {"ID":20,
    "name" : "Jim McDonald",
    "DOB" : "02/02/1999",
    "Gender" : "M",
    "Age":25,
    "Zipcode" : "08124-6565",
    "Amount" : "1500.20"
        }]
 
json_object = json.dumps(dictionary, indent = 4)

with open("prob7.json", "w") as outfile:
    outfile.write(json_object)
