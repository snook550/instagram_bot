# config.py
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve environment variables or use default values
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LOYALTY_GATOR_USER_ID = os.getenv("LOYALTY_GATOR_USER_ID")
LOYALTY_GATOR_PASS = os.getenv("LOYALTY_GATOR_PASS")
LOYALTY_GATOR_ACCOUNT_ID = os.getenv("LOYALTY_GATOR_ACCOUNT_ID")
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN")
LOYALTY_GATOR_USER_PASSWORD = os.getenv("LOYALTY_GATOR_USER_PASSWORD")
LOYALTY_GATOR_CAMPAIGN_ID = os.getenv("LOYALTY_GATOR_CAMPAIGN_ID")
FLASK_VERIFY_TOKEN = os.getenv("FLASK_VERIFY_TOKEN")
