import random
import string
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("API_URL")
DB_NAME = os.getenv("DB_NAME")

def get_random_username():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))