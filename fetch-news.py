# Gets the recent news headline from tageschau and appends it to a file
import requests

# do the api request
def get_headline(index=0):
    try:
        return requests.get("https://www.tagesschau.de/api2u/news").json()["news"][index]["title"]
    except IndexError:
        return ("Index does not exist. Try a smaller number.")
    
# append current headline to file
with open("headlines.txt", "a", encoding="utf-8") as file:
    file.write(get_headline().strip("+") + "\n")


# keep only n number of lines in that file
def maintain_max_lines(file_path, max_lines=24):
    # Read all lines from the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Keep only the last `max_lines` lines
    lines = lines[-max_lines:]

    # Write back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)

maintain_max_lines("headlines.txt", 24)