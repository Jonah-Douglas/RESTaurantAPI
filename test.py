# user that is requesting API on main for information from server via get/post methods

import requests

BASE = "http://127.0.0.1:5000/"


# retrieve testFile data and instantiate data array to use with API
with open("testFile.txt") as f:
    lines = f.readlines()
    count = 0

    for line in lines:
        print(line)
        response = requests.put(BASE + "order/" + str(count), {"order": line})
        print(response)
        count+=1

# input()
# response = requests.get(BASE + "video/2")
# print(response.json())