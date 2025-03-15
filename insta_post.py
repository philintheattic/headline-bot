import instagrapi
import os, sys
from datetime import date
from dotenv import load_dotenv

# Is there a better solution than hardcoding?
output_path = f"ready2post/post-{date.today()}.png"

# check if there exists a file to post for the day
if not os.path.exists(output_path):
    sys.exit("File not found! Nothing to post today.")

# Load environment variables
load_dotenv()
ACCOUNT_NAME = os.getenv("ACCOUNT_NAME")
ACCOUNT_PASSWORD = os.getenv("ACCOUNT_PASSWORD")

### INSTAGRAM API STUFF ###
client = instagrapi.Client()

client.login(ACCOUNT_NAME, ACCOUNT_PASSWORD)
client.photo_upload(output_path, f"doomnews vom {date.today()}")