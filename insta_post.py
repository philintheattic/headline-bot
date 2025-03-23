import requests
from dotenv import load_dotenv
import os
from TextGen import *

# Prepare a caption
file = "headlines.txt"
text = import_file_as_list(file)
text = remove_all_symbols(text)
text = remove_short_words(text, maxlength=2)
text = remove_prepositions(text)
text = remove_duplicates(text)
text = remove_all_digits(text)
poem = generate_poem(text, length=3, flags=LOWERCASE)

# Load environment variables
load_dotenv()

# tumblr api stuff
API_KEY = os.getenv("API_KEY")
BLOG_NAME = "doom-news.tumblr.com"

# instagram api stuff
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
INSTAGRAM_ID = os.getenv("BUSINESS_ID")

def get_latest_tumblr_image():
    url = f"https://api.tumblr.com/v2/blog/{BLOG_NAME}/posts/photo?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Extract image URL from latest post
    if "response" in data and "posts" in data["response"]:
        latest_post = data["response"]["posts"][0]  # Get the most recent post
        image_url = latest_post["photos"][0]["original_size"]["url"]
        return image_url
    return None

IMAGE_URL = get_latest_tumblr_image()  # Image must be publicly accessible
CAPTION = " ".join(poem)

# Step 1: Upload the Image
url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_ID}/media"

if IMAGE_URL:
    data = {
        "image_url": IMAGE_URL,
        "caption": CAPTION,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=data)
    media_id = response.json().get("id")
    print("Media ID:", media_id)
else:
    print("No image found!")

# Step 2: Publish the Image
publish_url = f"https://graph.facebook.com/v18.0/{INSTAGRAM_ID}/media_publish"
publish_data = {
    "creation_id": media_id,
    "access_token": ACCESS_TOKEN
}
publish_response = requests.post(publish_url, data=publish_data)

print(publish_response.json())  # Should return success message