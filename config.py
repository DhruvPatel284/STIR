from dotenv import load_dotenv
import os

load_dotenv()

TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
MONGODB_URI = os.getenv('MONGODB_URI')
PROXY_HOST = os.getenv('PROXY_HOST')  # e.g., "us-wa.proxymesh.com"
PROXY_PORT = os.getenv('PROXY_PORT')  # e.g., "31280"
PROXY_USERNAME = os.getenv('PROXY_USERNAME')
PROXY_PASSWORD = os.getenv('PROXY_PASSWORD')