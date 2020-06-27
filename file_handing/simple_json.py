import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json") != 0:
    old_file = open("./ages.json", "r+")
    data = json.load(old_file)
    print("Current age is",data["age"],"-- adding a year.")
    data["age"] = data["age"] + 1
    print("new age is", data["age"])

else:
    old_file = open("./ages.json", "w+")
    data = {"Name": "Nick", "age": 27}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data,"ages.json"))
