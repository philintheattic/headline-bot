import pytumblr
import os, sys
from datetime import date
from dotenv import load_dotenv

# Is there a better solution than hardcoding?
output_path = f"ready2post/post-{date.today()}.png"

# check if there exists a file to post for the day
if not os.path.exists(output_path):
    sys.exit("File not found! Nothing to post today.")

print(output_path)

# Environment variables
load_dotenv()
API_KEY = os.environ["API_KEY"]
SECRET_KEY = os.environ["SECRET_KEY"]
OAUTH_TOKEN = os.environ["OAUTH_TOKEN"]
OAUTH_SECRET = os.environ["OAUTH_SECRET"]

### TUMBLR API STUFF ###

blog_name = "doom-news.tumblr.com" # use this
uuid = "t:xBX65HaS9V8K-C91Yli7CQ"
taglist = ["doomnews", "automated"]

# Authenticate via OAuth
client = pytumblr.TumblrRestClient(
  API_KEY,
  SECRET_KEY,
  OAUTH_TOKEN,
  OAUTH_SECRET
)

# Make the request
# print(client.blog_info("doom-news"))

client.create_photo(blog_name, state="published", tags=taglist, data=output_path)


# move image into different folder after posting
# Make sure that directory exists
os.makedirs("posted", exist_ok=True)
os.rename(output_path, f"posted/post-{date.today()}.png")