# Gets the recent news headline from tageschau and appends it to a file
import requests

# do the api request
def get_headline(index=0):
    try:
        return requests.get("https://www.tagesschau.de/api2u/news").json()["news"][index]["title"]
    except IndexError:
        return ("Index does not exist. Try a smaller number.")
    
# append current headline to file
with open("headlines.txt", "a") as file:
    file.write(get_headline().strip("+") + "\n")

print("Headline appended!")