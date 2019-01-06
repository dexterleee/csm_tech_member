import time
import csv
import sys
import requests, json

def reddit_jokes():
    link = "https://www.reddit.com/r/dadjokes.json"
    r = requests.get(link, headers = {'User-agent': 'your bot 0.1'})
    data = json.loads(r.text)
    titles = []
    punchlines = []
    #print(json.dumps(data, indent=4))
    i = data["data"]
    j = i["children"]
    #print(j[0]["data"]["over_18"])
    for dictionary in j:
        #print(dictionary["data"]["over_18"])
        if (dictionary["data"]["over_18"] == False):
            splitted = (dictionary["data"]["title"]).split()
            if(splitted[0] == "What" or splitted[0] == "How" or splitted[0] == "Why"):
                titles.append(dictionary["data"]["title"])
                punchlines.append(dictionary["data"]["selftext"])
    return titles, punchlines
#print(titles)
#print(punchlines)


def joke_delivery(prompt, punchline):
    print(prompt, flush = True)
    time.sleep(2)
    print(punchline, flush = True)


def read_input():
    while (True):
        a = input('Enter input: ')
        if (a == "next"):
            return True
        elif (a == "quit"):
            return False
        else:
            print("I don't understand")

def joke_reader(file):
    joke_list = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            joke_list.append([row[0],row[1]])
    return joke_list

if __name__ == "__main__":
    #print(len(sys.argv))
    if (len(sys.argv) == 1):
        jokes, punchlines = reddit_jokes()
        joke_delivery(jokes[0], punchlines[0])

        joke_num = 1
        while (joke_num != len(jokes)):
            if (read_input()):
                joke_delivery(jokes[joke_num], punchlines[joke_num])
                joke_num += 1
            else:
                sys.exit()


    else:
        jokes = joke_reader(sys.argv[1]) #second command line input
        joke_delivery(jokes[0][0], jokes[0][1])

        joke_num = 1
        while (joke_num != len(jokes)):
            if (read_input()):
                joke_delivery(jokes[joke_num][0], jokes[joke_num][1])
                joke_num += 1
            else:
                sys.exit()
        print("No more jokes to tell")
        time.sleep(2)
        sys.exit()
