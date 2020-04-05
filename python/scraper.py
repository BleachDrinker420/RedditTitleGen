import requests
import time
import json
import sys
import os

subreddit = input("Subreddit To Scrape: ")


url = "https://api.pushshift.io/reddit/search/submission/?subreddit=" + subreddit + "&sort=asc&sort_type=created_utc&after=0&before=2147483647&size=1000"

titles = []
page = 1
curTime = 1543199911

while True:

    print("Downloading Page " + str(page) + ".. [" + time.strftime("%d/%m/%y %H:%M:%S", time.gmtime(curTime)) + "]")
    req = requests.get(url)

    content = req.text

    print("Parsing Data..")
    #Debug: uncomment this to save all the json data
    #with open("out" + str(page) + ".json", "w", encoding="utf8") as file:
    #    file.write("\ufeff") #utf8 signature
    #    file.write(content)

    data = json.loads(content)

    if len(data["data"]) == 0:
        if page == 1:
            print("Invalid Subreddit!")
            sys.exit()
        break

    for d in data["data"]:
        titles.append(d["title"])

    page += 1
    curTime = int(data["data"][len(data["data"]) - 1]["created_utc"])
    url = "https://api.pushshift.io/reddit/search/submission/?subreddit=" + subreddit + "&sort=asc&sort_type=created_utc&after=" + str(curTime+1) + "&before=2147483647&size=1000"
    #time.sleep(5) #Uncomment if it scrapes too fast

print("Writing Output..")
with open("titles.txt", "w", encoding="utf8") as file:
    s = ""
    for t in titles : s += t + "\n"

    file.write("\ufeff") #utf8 signature
    file.write(s)
    print("Done! Wrote To \"titles.txt\"")
    


