import requests
import time
import json
import sys
import os

subreddit = input("Subreddit To Scrape: ")
filterRem = True
sort = "asc"
flair = False

# --- Set Removed Filter ---
temp = input("Filter Removed [Y/n]: ").lower()
if temp == "n":
    filterRem = False
elif temp != "y":
    print("..Invalid input, setting to \"True\"\n")

# --- Set Ascending/Descending ---
temp = input("Date Search (Ascend/Descend) [A/d]: ").lower()
if temp == "d":
    sort = "desc"
elif temp != "a":
    print("..Invalid input, setting to \"Ascend\"\n")

# --- Set Flair Setting ---
temp = input("Add Flair To Title [y/N]: ").lower()
if temp == "y":
    flair = True
elif temp != "n":
    print("..Invalid input, setting to \"False\"")

# --- Set Variables ---
url = "https://api.pushshift.io/reddit/search/submission/?subreddit=" + subreddit + "&sort=" + sort + "&sort_type=created_utc&after=0&before=2147483647&size=1000"

titles = []
page = 1
curTime = 0

if sort == "desc":
    curTime = int(time.time()) + 1

# --- Scrape ---
print("\n--- Downloading. (Use Ctrl+C To Stop) ---")
while True:
    try:
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
            #Too lazy to make them in 1 if, sue me
            if filterRem and "selftext" in d and d["selftext"] == "[removed]":
                continue
            if filterRem and "removed_by_category" in d:
                 continue

            if flair and "link_flair_text" in d:
                titles.append("[" + d["link_flair_text"] + "] " + d["title"])
            else:
                titles.append(d["title"])

        page += 1
        curTime = int(data["data"][len(data["data"]) - 1]["created_utc"])
        
        if sort == "desc":
            url = "https://api.pushshift.io/reddit/search/submission/?subreddit=" + subreddit + "&sort=desc&sort_type=created_utc&after=0&before=" + str(curTime-1) + "&size=1000"
        else:
            url = "https://api.pushshift.io/reddit/search/submission/?subreddit=" + subreddit + "&sort=asc&sort_type=created_utc&after=" + str(curTime+1) + "&before=2147483647&size=1000"

        #time.sleep(5) #Uncomment if it scrapes too fast
    except KeyboardInterrupt:
        print("Stopping Scraper..")
        break

print("Writing Output..")
with open("titles-" + subreddit + ".txt", "w", encoding="utf8") as file:
    s = ""
    for t in titles : s += t + "\n"

    file.write("\ufeff") #utf8 signature
    file.write(s)
    print("Done! Wrote To \"titles-" + subreddit + ".txt\"")
    


